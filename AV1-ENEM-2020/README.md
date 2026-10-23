# AV1 — Análise Descritiva dos Dados do ENEM 2020

Projeto acadêmico desenvolvido na disciplina de **Métodos Quantitativos em Computação**, do curso de **Ciência da Computação da Universidade de Fortaleza (UNIFOR)**, no semestre 2026.2.

## Objetivo

Realizar uma análise estatística descritiva de uma amostra dos dados do ENEM 2020, investigando o perfil socioeconômico dos participantes e a distribuição das notas por meio de tabelas, gráficos e medidas estatísticas.

## Tecnologias Utilizadas

- **Python:** linguagem de programação utilizada na análise.
- **Pandas:** manipulação e análise dos dados.
- **Matplotlib:** criação de gráficos estatísticos.
- **OpenPyXL:** leitura e geração de arquivos Excel.

## Estrutura do Projeto

```text
AV1-ENEM-2020/
├── codigo/
│   ├── enem.py
│   └── tabelas_graficos_enem.py
├── dados/
│   └── dados_enem_2020.xlsx
├── relatorio/
│   └── relatorio_enem_2020.pdf
├── resultados/
│   ├── graficos/
│   └── tabelas/
├── .gitignore
├── README.md
└── requirements.txt
```

## Como Executar

### 1. Criar um ambiente virtual

Na pasta `AV1-ENEM-2020`, execute:

```bash
python -m venv .venv
```

### 2. Ativar o ambiente virtual

No Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Executar os scripts

Para gerar as tabelas de frequência, tabelas cruzadas e gráficos:

```bash
python codigo/tabelas_graficos_enem.py
```

Para executar a análise das notas, incluindo histogramas, boxplots e medidas estatísticas:

```bash
python codigo/enem.py
```

O segundo script exibe os gráficos em janelas e pode gerar o arquivo `resultados_enem.xlsx`, que não precisa estar armazenado no repositório.

## Metodologia

A análise estatística contempla:

- Tabelas de frequência absoluta e relativa.
- Tabelas cruzadas de variáveis socioeconômicas.
- Gráficos de barras e setores.
- Histogramas e boxplots.
- Medidas de posição e dispersão.

Os resultados são interpretados de forma descritiva, considerando a amostra utilizada.

## Resultados

As tabelas e os gráficos gerados estão organizados na pasta `resultados/`.

O relatório acadêmico completo, contendo a apresentação e interpretação dos resultados, está disponível em `relatorio/relatorio_enem_2020.pdf`.

## Fonte dos Dados

**Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)** — Microdados do ENEM 2020, conforme base disponibilizada para a disciplina.

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
