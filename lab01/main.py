import os
import csv
import requests
from datetime import datetime, timezone

URL = "https://api.github.com/graphql"
CSV_FILE = "repos_populares_1000.csv"

# STEP 1: busca leve, só para identificar os repositórios
QUERY_SEARCH = """
query($queryString: String!, $first: Int!, $after: String) {
  search(query: $queryString, type: REPOSITORY, first: $first, after: $after) {
    pageInfo {
      endCursor
      hasNextPage
    }
    nodes {
      ... on Repository {
        nameWithOwner
        stargazerCount
      }
    }
  }
}
"""

# STEP 2: busca detalhada de cada repositório
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

def build_batch_repo_query(repo_batch):
    query_parts = []

    for index, item in enumerate(repo_batch):
        owner, name = item["nameWithOwner"].split("/", 1)

        query_parts.append(f"""
        repo{index}: repository(owner: "{owner}", name: "{name}") {{
            nameWithOwner
            createdAt
            pushedAt
            stargazerCount
            primaryLanguage {{ name }}
            releases {{ totalCount }}
            pullRequests(states: MERGED) {{ totalCount }}
            issuesOpen: issues(states: OPEN) {{ totalCount }}
            issuesClosed: issues(states: CLOSED) {{ totalCount }}
        }}
        """)

    return "query {\n" + "\n".join(query_parts) + "\n}"

def post_gql(token, query, variables):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "gh-metrics-script",
    }

    response = requests.post(
        URL,
        json={"query": query, "variables": variables},
        headers=headers,
        timeout=30
    )

    if response.status_code != 200:
        raise Exception(f"HTTP {response.status_code}: {(response.text or '')[:200]}")

    data = response.json()

    if "errors" in data:
        raise Exception(f"GraphQL errors: {data['errors']}")

    return data

def fetch_repo_names(token, query_string, total=1000, page_size=100):
    repos = []
    cursor = None

    while len(repos) < total:
        variables = {
            "queryString": query_string,
            "first": min(page_size, total - len(repos)),
            "after": cursor
        }

        payload = post_gql(token, QUERY_SEARCH, variables)
        search = payload["data"]["search"]

        repos.extend(search["nodes"])

        page_info = search["pageInfo"]
        cursor = page_info["endCursor"]

        if not page_info["hasNextPage"]:
            break

    return repos[:total]

def build_repo_row(repo_data, now):
    created = datetime.fromisoformat(repo_data["createdAt"].replace("Z", "+00:00"))
    pushed = (
        datetime.fromisoformat(repo_data["pushedAt"].replace("Z", "+00:00"))
        if repo_data["pushedAt"] else None
    )

    age_years = round((now - created).days / 365.25, 2)
    days_since_update = (now - pushed).days if pushed else None

    issues_open = repo_data["issuesOpen"]["totalCount"]
    issues_closed = repo_data["issuesClosed"]["totalCount"]
    issues_total = issues_open + issues_closed
    issues_closed_ratio = round(issues_closed / issues_total, 4) if issues_total > 0 else 0.0

    primary_language = (
        repo_data["primaryLanguage"]["name"]
        if repo_data["primaryLanguage"] else "None"
    )

    return {
        "repo": repo_data["nameWithOwner"],
        "stars": repo_data["stargazerCount"],
        "created_at": repo_data["createdAt"],
        "pushed_at": repo_data["pushedAt"],
        "age_years": age_years,
        "days_since_last_update": days_since_update,
        "merged_prs": repo_data["pullRequests"]["totalCount"],
        "releases": repo_data["releases"]["totalCount"],
        "primary_language": primary_language,
        "issues_open": issues_open,
        "issues_closed": issues_closed,
        "issues_total": issues_total,
        "issues_closed_ratio": issues_closed_ratio,
    }

def chunk_list(items, chunk_size):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def save_to_csv(rows, filename):
    fieldnames = [
        "repo",
        "stars",
        "created_at",
        "pushed_at",
        "age_years",
        "days_since_last_update",
        "merged_prs",
        "releases",
        "primary_language",
        "issues_open",
        "issues_closed",
        "issues_total",
        "issues_closed_ratio",
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise Exception("Defina GITHUB_TOKEN no .env")

    now = datetime.now(timezone.utc)
    query_string = "stars:>5000 sort:stars-desc"

    print("Buscando nomes dos 1000 repositórios...")
    repos_list = fetch_repo_names(token, query_string, total=1000, page_size=100)
    print(f"Repositórios encontrados: {len(repos_list)}")

    rows = []

    for index, item in enumerate(repos_list, start=1):
        owner, name = item["nameWithOwner"].split("/", 1)
        repo_payload = post_gql(token, QUERY_REPO, {"owner": owner, "name": name})
        repo_data = repo_payload["data"]["repository"]

        row = build_repo_row(repo_data, now)
        rows.append(row)

        print(f"[{index}/1000] {row['repo']}")

    save_to_csv(rows, CSV_FILE)
    print(f"\nCSV gerado com sucesso: {CSV_FILE}")

if __name__ == "__main__":
    main()