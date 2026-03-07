# Laboratório 01 — Características de Repositórios Populares
## Lab01S02 — Relatório de Análise

### Introdução

Este experimento tem como objetivo analisar características de repositórios populares no GitHub, utilizando métricas extraídas via GitHub GraphQL API. Foram coletados dados de 1000 repositórios populares (ordenados por número de estrelas) e analisadas métricas relacionadas à maturidade, contribuição externa, frequência de releases, atividade recente, linguagem utilizada e resolução de issues.

A popularidade foi definida utilizando o número de estrelas do GitHub como proxy.

---

# Metodologia

A coleta de dados foi realizada utilizando a GitHub GraphQL API.

O processo foi dividido em duas etapas:

1. Busca dos 1000 repositórios populares utilizando a operação `search`.
2. Consulta detalhada das métricas de cada repositório.

Os dados foram armazenados em um arquivo CSV contendo as seguintes variáveis:

- Nome do repositório
- Número de estrelas
- Data de criação
- Data do último push
- Idade do repositório (anos)
- Dias desde a última atualização
- Número de pull requests aceitas
- Número de releases
- Linguagem primária
- Número de issues abertas
- Número de issues fechadas
- Percentual de issues fechadas

Para análise quantitativa foram utilizadas **medianas**, conforme solicitado no enunciado do laboratório.

---

# Resultados

## RQ01 — Sistemas populares são maduros/antigos?

Métrica utilizada: idade do repositório (anos)

**Mediana da idade dos repositórios:**

8,37 anos

Interpretação:

Repositórios populares tendem a ser relativamente antigos. Isso sugere que projetos que alcançam alta popularidade geralmente passam por um período longo de desenvolvimento e adoção pela comunidade.

---

## RQ02 — Sistemas populares recebem muita contribuição externa?

Métrica utilizada: número de pull requests aceitas.

**Mediana de PRs aceitas:**

743 pull requests

Interpretação:

Projetos populares apresentam um alto volume de pull requests aceitas, indicando participação ativa da comunidade no desenvolvimento e manutenção desses projetos.

---

## RQ03 — Sistemas populares lançam releases com frequência?

Métrica utilizada: número total de releases.

**Mediana de releases:**

40 releases

Interpretação:

Repositórios populares frequentemente disponibilizam novas versões, indicando ciclos de desenvolvimento contínuos e evolução constante do software.

---

## RQ04 — Sistemas populares são atualizados com frequência?

Métrica utilizada: dias desde a última atualização.

**Mediana de dias desde o último update:**

2 dias

Interpretação:

A maioria dos projetos populares apresenta atividade recente, sugerindo manutenção ativa e desenvolvimento contínuo.

---

## RQ05 — Sistemas populares são escritos nas linguagens mais populares?

Métrica utilizada: linguagem primária.

As linguagens mais frequentes foram:

| Linguagem | Repositórios |
|----------|-------------|
| Python | 201 |
| TypeScript | 160 |
| JavaScript | 114 |
| Go | 76 |
| Rust | 54 |
| Java | 47 |
| C++ | 46 |

Interpretação:

A predominância de linguagens como Python, TypeScript e JavaScript sugere forte relação entre popularidade da linguagem e popularidade dos projetos desenvolvidos nela.

---

## RQ06 — Sistemas populares possuem alto percentual de issues fechadas?

Métrica utilizada: percentual de issues fechadas.

**Mediana do percentual de issues fechadas:**

86,8%

Interpretação:

Projetos populares tendem a manter boa gestão de issues, com grande parte sendo resolvida ou fechada.

---

# Discussão

Os resultados indicam que repositórios populares apresentam algumas características recorrentes:

- Alta maturidade (idade relativamente elevada)
- Grande volume de contribuições externas
- Releases frequentes
- Atualizações recentes
- Uso predominante de linguagens amplamente adotadas
- Alta taxa de resolução de issues

Esses fatores sugerem que popularidade no GitHub está associada a projetos maduros, ativos e com forte participação da comunidade.

---

# Conclusão

A análise de 1000 repositórios populares no GitHub demonstrou que popularidade está relacionada a:

- tempo de maturação do projeto
- participação ativa da comunidade
- manutenção frequente
- uso de linguagens amplamente adotadas

Esses resultados reforçam a importância da atividade contínua e da colaboração aberta para o sucesso de projetos de software em plataformas como o GitHub.

---

# Limitações

Algumas limitações deste estudo incluem:

- uso do número de estrelas como única métrica de popularidade
- possíveis limitações da API do GitHub
- ausência de análise temporal detalhada das contribuições

Estudos futuros podem explorar outras métricas como forks, watchers e análise temporal de commits.