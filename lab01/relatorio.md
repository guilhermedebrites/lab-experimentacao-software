# Laboratório 01 — Características de Repositórios Populares
## Lab01S02 — Relatório de Análise

### Introdução

Este experimento tem como objetivo analisar características de repositórios populares no GitHub, utilizando métricas extraídas via GitHub GraphQL API. Foram coletados dados de 1000 repositórios populares (ordenados por número de estrelas) e analisadas métricas relacionadas à maturidade, contribuição externa, frequência de releases, atividade recente, linguagem utilizada e resolução de issues.

A popularidade foi definida utilizando o número de estrelas do GitHub como proxy.

---

Hipóteses Informais

Antes da coleta de dados, foram estabelecidas as seguintes hipóteses
baseadas em observações da comunidade open-source:

H1 - Repositórios populares tendem a ser mais antigos e maduros.

H2 - Repositórios populares recebem grande volume de contribuições externas.

H3 - Projetos populares tendem a lançar releases com frequência.

H4 - Projetos populares apresentam atividade recente e manutenção ativa.

H5 - A maioria dos repositórios populares utiliza linguagens amplamente
adotadas pela comunidade de desenvolvimento.

H6 - Projetos populares possuem alta taxa de resolução de issues.

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

## RQ07 — Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?

Para investigar essa questão, os resultados das RQs 02, 03 e 04 foram analisados separadamente de acordo com a linguagem primária dos repositórios. Foram consideradas as linguagens mais frequentes identificadas na RQ05.

A tabela abaixo apresenta uma visão comparativa considerando três métricas:

- número de pull requests aceitas (contribuição externa)
- número de releases
- dias desde a última atualização

Foram consideradas apenas as linguagens com maior frequência entre os 1000 repositórios analisados.

| Linguagem | Mediana de PRs Aceitas | Mediana de Releases | Mediana de Dias desde Última Atualização |
|----------|-----------------------|--------------------|-------------------------------------------|
| Python | alta | alta | muito baixa |
| TypeScript | alta | alta | muito baixa |
| JavaScript | alta | média | baixa |
| Go | média | média | baixa |
| Rust | média | média | baixa |
| Java | média | média | baixa |
| C++ | média | baixa | média |

Interpretação:

Os resultados indicam que repositórios escritos em linguagens amplamente utilizadas pela comunidade, como Python, TypeScript e JavaScript, tendem a receber maior volume de contribuições externas, refletido pelo número elevado de pull requests aceitas.

Esses projetos também apresentam maior número de releases e menor tempo desde a última atualização, indicando ciclos de desenvolvimento mais ativos.

Por outro lado, linguagens como C++ e Java apresentam valores intermediários ou menores em algumas dessas métricas, o que pode refletir diferentes estilos de desenvolvimento ou menor volume de contribuição comunitária em comparação com ecossistemas mais modernos.

De forma geral, os dados sugerem que linguagens populares tendem a estar associadas a projetos mais ativos, com maior participação da comunidade e ciclos de atualização mais frequentes.

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