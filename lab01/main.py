import os
import requests
from datetime import datetime, timezone

URL = "https://api.github.com/graphql"

QUERY_SEARCH = """
query($queryString: String!, $first: Int!) {
  search(query: $queryString, type: REPOSITORY, first: $first) {
    nodes {
      ... on Repository {
        nameWithOwner
        stargazerCount
      }
    }
  }
}
"""

QUERY_REPO = """
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    nameWithOwner
    createdAt
    pushedAt
    stargazerCount
    primaryLanguage { name }
    releases { totalCount }
    pullRequests(states: MERGED) { totalCount }
    issuesOpen: issues(states: OPEN) { totalCount }
    issuesClosed: issues(states: CLOSED) { totalCount }
  }
}
"""

def post_gql(token, query, variables, max_retries=5):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "gh-metrics-script",
    }

    r = requests.post(URL, json={"query": query, "variables": variables}, headers=headers, timeout=30)

    if r.status_code != 200:
        raise Exception(f"HTTP {r.status_code}: {(r.text or '')[:200]}")
    return r.json()

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise Exception("Defina GITHUB_TOKEN no .env")

    #STEP 1: pega top 100 populares
    search_vars = {"queryString": "stars:>5000 sort:stars-desc", "first": 100}
    search_data = post_gql(token, QUERY_SEARCH, search_vars)

    repos_list = search_data["data"]["search"]["nodes"]
    now = datetime.now(timezone.utc)

    print(f"Repos encontrados: {len(repos_list)}")

    #STEP 2: para cada repo, puxa métricas e printa
    for item in repos_list:
        owner, name = item["nameWithOwner"].split("/", 1)
        repo_data = post_gql(token, QUERY_REPO, {"owner": owner, "name": name})["data"]["repository"]

        created = datetime.fromisoformat(repo_data["createdAt"].replace("Z", "+00:00"))
        pushed = datetime.fromisoformat(repo_data["pushedAt"].replace("Z", "+00:00")) if repo_data["pushedAt"] else None

        age_years = (now - created).days / 365.25
        days_since_update = (now - pushed).days if pushed else None

        issues_open = repo_data["issuesOpen"]["totalCount"]
        issues_closed = repo_data["issuesClosed"]["totalCount"]
        issues_total = issues_open + issues_closed
        issues_ratio = (issues_closed / issues_total) if issues_total > 0 else 0

        lang = repo_data["primaryLanguage"]["name"] if repo_data["primaryLanguage"] else "None"

        print("=" * 60)
        print("Repo:", repo_data["nameWithOwner"])
        print("Stars:", repo_data["stargazerCount"])
        print("Idade (anos):", round(age_years, 2))  # RQ01
        print("PRs aceitas (merged):", repo_data["pullRequests"]["totalCount"])  # RQ02
        print("Total releases:", repo_data["releases"]["totalCount"])  # RQ03
        print("Dias desde última atualização:", days_since_update)  # RQ04
        print("Linguagem primária:", lang)  # RQ05
        print("Percentual issues fechadas:", round(issues_ratio * 100, 2), "%")  # RQ06

if __name__ == "__main__":
    main()