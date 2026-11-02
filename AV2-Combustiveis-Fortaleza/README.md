
# AV2 — Análise de Preços de Combustíveis em Fortaleza

Projeto acadêmico desenvolvido na disciplina de **Métodos Quantitativos em Computação**, do curso de **Ciência da Computação da Universidade de Fortaleza (UNIFOR)**, no semestre 2026.2.

## Objetivo

Realizar uma análise estatística da relação entre os preços da gasolina e do etanol em Fortaleza, utilizando dados de 2025 para investigar a correlação entre as variáveis e construir um modelo de regressão linear simples.

## Tecnologias Utilizadas

- **Python:** linguagem de programação utilizada na análise.
- **Pandas:** manipulação, tratamento e organização dos dados.
- **SciPy:** cálculos estatísticos, correlação e regressão linear.
- **Matplotlib:** criação de gráficos estatísticos.

## Estrutura do Projeto


## Estrutura do Projeto

```text
AV2-Combustiveis-Fortaleza/
├── codigo/
│   ├── analise_estatistica.py
│   ├── tratamento.py
│   └── validacao_modelo.py
├── dados/
│   ├── ANP_Fortaleza_gasolina_etanol_20...
│   └── dados_tratados.csv
├── relatorio/
│   └── Relatório - Regressão Linear.pdf
├── resultados/
│   ├── graficos/
│   │   ├── dispersao_regressao.png
│   │   ├── histograma_residuos.png
│   │   ├── qqplot_residuos.png
│   │   └── residuos_valores_estimados.png
│   └── tabelas/
│       ├── anova_regressao.csv
│       ├── resultados_estatisticos.csv
│       └── validacao_modelo.csv
└── README.md
```


## Como Executar

### 1. Criar um ambiente virtual

Na pasta `AV2-Combustiveis-Fortaleza`, execute:

```bash
python -m venv .venv
```

### 2. Ativar o ambiente virtual

No Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

No Linux:

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
python -m pip install pandas scipy matplotlib
```

### 4. Executar os scripts

Para realizar o tratamento e a preparação dos dados:

```bash
python codigo/tratamento.py
```

Para executar a análise estatística, incluindo correlação e regressão linear:

```bash
python codigo/analise_estatistica.py
```

Para executar a validação do modelo estatístico:

```bash
python codigo/validacao_modelo.py
```

Os comandos consideram a execução a partir da pasta principal da AV2. Caso os scripts utilizem caminhos relativos diferentes, poderá ser necessário ajustá-los.

## Metodologia

A análise estatística contempla:

- Tratamento e organização dos dados disponibilizados pela ANP.
- Cálculo de medidas estatísticas descritivas.
- Construção de diagramas de dispersão.
- Cálculo do coeficiente de correlação de Pearson.
- Estimativa da equação de regressão linear simples.
- Cálculo e interpretação do coeficiente de determinação (R²).
- Análise dos resíduos e verificação da normalidade.
- Análise de variância (ANOVA).
- Estimativas de preços com base no modelo ajustado.

Os resultados são interpretados considerando a significância estatística e as limitações do modelo.

## Resultados

A base original contém **4.751 registros**, sendo 2.383 de etanol e 2.368 de gasolina. Após o tratamento dos dados, foram utilizadas **102 observações pareadas**.

Os principais resultados obtidos foram:

- **Correlação de Pearson:** 0,6275.
- **Equação de regressão:** Gasolina = 4,6925 + 0,3233 × Etanol.
- **Coeficiente de determinação (R²):** 39,37%.
- **Estatística F (ANOVA):** 64,9375.
- **Valor-p:** aproximadamente 1,70 × 10⁻¹².

Os resultados indicam uma associação linear positiva moderada entre os preços médios da gasolina e do etanol.

O modelo de regressão explica aproximadamente 39,37% da variação observada nos preços médios da gasolina, apresentando significância estatística, embora existam limitações identificadas na análise dos resíduos.

As tabelas e os gráficos gerados estão organizados na pasta `resultados/`.

O relatório acadêmico completo, contendo a apresentação e interpretação dos resultados, está disponível em [Relatório — Regressão Linear](relatorio/Relat%C3%B3rio%20-%20Regress%C3%A3o%20Linear.pdf).

## Fonte dos Dados

**Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)** — Dados de preços de combustíveis referentes ao município de Fortaleza, Ceará, no ano de 2025.

## Equipe de Desenvolvimento

Projeto desenvolvido pelos estudantes:

- **Pedro Lucas de Oliveira Duarte**
- **Maria Eduarda Teles de Melo**
- **Samuel Batista Oliveira**

### Informações Acadêmicas

- **Universidade:** Universidade de Fortaleza (UNIFOR)
- **Curso:** Ciência da Computação
- **Disciplina:** Métodos Quantitativos em Computação
- **Professor:** Cledinaldo Castro Araújo
- **Semestre:** 2026.2
