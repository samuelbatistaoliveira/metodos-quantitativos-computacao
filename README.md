
# Métodos Quantitativos em Computação

Repositório acadêmico destinado ao desenvolvimento de projetos de **análise de dados, estatística descritiva, modelagem estatística, estimação e amostragem com Python**, realizados na disciplina de **Métodos Quantitativos em Computação**, do curso de Ciência da Computação da Universidade de Fortaleza (UNIFOR).

## Sobre o Repositório

Este repositório reúne os projetos desenvolvidos durante o semestre 2026.2, com o objetivo de aplicar conceitos estatísticos e computacionais na exploração, visualização e interpretação de dados reais.

As atividades envolvem processamento de bases de dados, construção de tabelas e gráficos, análise de medidas estatísticas e aplicação de métodos quantitativos.

## Projetos

### AV1 — Análise Descritiva dos Dados do ENEM 2020

**Status:** Desenvolvido

Análise estatística de uma amostra de **5.798 registros do ENEM 2020**, explorando características socioeconômicas dos participantes e a distribuição das notas.

**Principais análises:**

- Distribuições de frequência absoluta e relativa.
- Medidas de posição e dispersão.
- Tabelas cruzadas de variáveis socioeconômicas.
- Histogramas e boxplots.
- Gráficos de barras e setores.
- Análise da relação entre renda familiar e acesso à internet.

**Resultados:** scripts Python, tabelas CSV, gráficos PNG e relatório acadêmico.

**[Acessar projeto AV1](./AV1-ENEM-2020)**

### AV2 — Análise de Preços de Combustíveis em Fortaleza

**Status:** Desenvolvido

Análise estatística da relação entre os preços médios da gasolina e do etanol em Fortaleza, utilizando dados públicos da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP), referentes a 2025.

A base original contém **4.751 registros**, posteriormente organizados em **102 observações pareadas** para aplicação dos métodos estatísticos.

**Principais análises:**

- Tratamento e organização dos dados.
- Estatísticas descritivas.
- Diagrama de dispersão.
- Correlação de Pearson.
- Regressão linear simples.
- Coeficiente de determinação (R²).
- Análise de resíduos e normalidade.
- ANOVA e validação do modelo.
- Estimativas de preços e limitações.

**Principais resultados:**

- **Correlação de Pearson:** 0,6275.
- **Equação de regressão:** Gasolina = 4,6925 + 0,3233 × Etanol.
- **Coeficiente de determinação (R²):** 39,37%.
- **Significância estatística:** valor-p inferior a 0,05.

Os resultados indicam uma associação linear positiva moderada entre os preços dos combustíveis, embora o modelo apresente limitações identificadas na análise dos resíduos.

**[Acessar projeto AV2](./AV2-Combustiveis-Fortaleza)**

### AV3 — Estimação e Amostragem

**Status:** Desenvolvido

Análise metodológica do Levantamento de Preços de Combustíveis da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP), considerando os postos revendedores de Fortaleza durante outubro de 2026.

O projeto busca avaliar os procedimentos amostrais, a representatividade da amostra, a confiabilidade dos resultados e as limitações metodológicas da pesquisa.

**Principais análises:**

- Caracterização da população-alvo.
- Identificação e avaliação da técnica de amostragem.
- Análise do tamanho da amostra.
- Cálculo da fração amostral.
- Análise da recorrência dos postos pesquisados.
- Discussão sobre nível de confiança e margem de erro.
- Identificação de limitações e possíveis vieses amostrais.
- Sugestões de melhorias metodológicas.

**Principais resultados:**

- **População de referência:** 314 postos cadastrados.
- **Amostra semanal:** 47 postos.
- **Postos distintos no período:** 52.
- **Registros de preços:** 727.
- **Fração amostral semanal de referência:** 14,97%.
- **Postos presentes nas quatro semanas:** 34 (65,38%).

**Resultados:** scripts Python, tabelas CSV, gráficos PNG e relatório acadêmico.

**[Acessar projeto AV3](./AV3-Estimacao-Amostragem)**

## Tecnologias e Ferramentas

| Tecnologia | Aplicação |
|---|---|
| Python | Processamento e análise estatística |
| Pandas | Manipulação e organização de dados |
| NumPy | Operações numéricas |
| SciPy | Correlação, regressão e testes estatísticos |
| Matplotlib | Visualização de dados |
| OpenPyXL | Manipulação de planilhas Excel |
| Git e GitHub | Versionamento e documentação |


## Estrutura do Repositório

    metodos-quantitativos-computacao/
    ├── AV1-ENEM-2020/
    │   ├── codigo/
    │   ├── dados/
    │   ├── relatorio/
    │   ├── resultados/
    │   ├── .gitignore
    │   ├── README.md
    │   └── requirements.txt
    ├── AV2-Combustiveis-Fortaleza/
    │   ├── codigo/
    │   ├── dados/
    │   ├── relatorio/
    │   ├── resultados/
    │   └── README.md
    ├── AV3-Estimacao-Amostragem/
    │   ├── dados/
    │   ├── resultados/
    │   └── scripts/
    ├── .gitignore
    └── README.md

Cada projeto possui seus próprios scripts, dados e resultados, permitindo sua execução e consulta de maneira independente.
Cada projeto possui seus próprios scripts, dados e resultados, permitindo sua execução e consulta de maneira independente.

Cada projeto possui sua própria documentação, scripts, dados e resultados, permitindo sua execução e consulta de maneira independente.



## Equipe

Projetos acadêmicos desenvolvidos por:

- **Pedro Lucas de Oliveira Duarte**
- **Maria Eduarda Teles de Melo**
- **Samuel Batista Oliveira**

## Informações Acadêmicas

- **Instituição:** Universidade de Fortaleza (UNIFOR)
- **Curso:** Ciência da Computação
- **Disciplina:** Métodos Quantitativos em Computação
- **Professor:** Cledinaldo Castro Araújo
- **Semestre:** 2026.2

## Finalidade

Este repositório possui finalidade acadêmica e educacional, buscando documentar a aplicação prática de métodos quantitativos em problemas de análise de dados, com organização, reprodutibilidade e transparência dos resultados.