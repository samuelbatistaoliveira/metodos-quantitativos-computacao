
import os
from pathlib import Path
import unicodedata

import pandas as pd
import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parents[1]

CAMINHO_ARQUIVO = str(BASE_DIR / "dados" / "dados_enem_2020.xlsx")

SEP = ";"
ENCODING = "latin-1"

COLUNAS = {
    "estado_civil": "Estado Civil",
    "dependencia_administrativa": "Dependência administrativa (Escola)",
    "renda_familiar": "Qual é a renda mensal de sua família?",
    "internet": "Na sua residência tem acesso à Internet?",
    "lingua_estrangeira": "Língua Estrangeira",
    "escola_ensino_medio": "Tipo de escola do Ensino Médio",
    "telefone_celular": "Na sua residência tem telefone celular?",
}

PASTA_SAIDA = str(BASE_DIR / "resultados")

os.makedirs(PASTA_SAIDA, exist_ok=True)
os.makedirs(os.path.join(PASTA_SAIDA, "tabelas"), exist_ok=True)
os.makedirs(os.path.join(PASTA_SAIDA, "graficos"), exist_ok=True)


def _normalizar(texto):
    texto = str(texto).strip().lower()
    texto = "".join(
        c for c in unicodedata.normalize("NFKD", texto)
        if not unicodedata.combining(c)
    )
    return texto


def carregar_dados():
    if CAMINHO_ARQUIVO.endswith((".xlsx", ".xls")):
        df_bruto = pd.read_excel(CAMINHO_ARQUIVO)
    else:
        df_bruto = pd.read_csv(
            CAMINHO_ARQUIVO,
            sep=SEP,
            encoding=ENCODING
        )

    normalizado_para_real = {
        _normalizar(c): c for c in df_bruto.columns
    }

    colunas_encontradas = {}
    colunas_faltando = []

    for chave, nome_desejado in COLUNAS.items():
        alvo = _normalizar(nome_desejado)

        if alvo in normalizado_para_real:
            colunas_encontradas[chave] = normalizado_para_real[alvo]
        else:
            colunas_faltando.append((chave, nome_desejado))

    if colunas_faltando:
        print(
            "\n[AVISO] Estas colunas do COLUNAS não bateram "
            "com nenhuma coluna do arquivo:"
        )

        for chave, nome_desejado in colunas_faltando:
            print(f'  - {chave}: procurando por "{nome_desejado}"')

        print("\nColunas realmente disponíveis no arquivo:")

        for c in df_bruto.columns:
            print(f"  - {c}")

    df = df_bruto[list(colunas_encontradas.values())].copy()

    df = df.rename(
        columns={v: k for k, v in colunas_encontradas.items()}
    )

    df = df.dropna(how="all")
    df = df.replace("", pd.NA)

    if "estado_civil" in df.columns:
        print(
            "\nValores encontrados em estado_civil:"
        )
        print(
            df["estado_civil"].value_counts(dropna=False)
        )

    df["estado_civil"] = df["estado_civil"].replace({
    4: "Viúvo(a)",
    "4": "Viúvo(a)"
    })

    return df


def tabela_frequencia(df, coluna, titulo, numero):
    serie = df[coluna].dropna()

    freq_abs = serie.value_counts()
    freq_pct = (
        serie.value_counts(normalize=True)
        .mul(100)
        .round(2)
    )

    tabela = pd.DataFrame({
        "Frequência": freq_abs,
        "Percentual (%)": freq_pct
    })

    print(f"\nTabela {numero} — {titulo}")
    print(tabela)
    print("Fonte: Microdados ENEM 2020 (INEP)")

    caminho = os.path.join(
        PASTA_SAIDA,
        "tabelas",
        f"tabela_{numero}_{coluna}.csv"
    )

    tabela.to_csv(caminho)

    return tabela


def gerar_todas_as_tabelas(df):
    variaveis = [
        ("estado_civil", "Estado civil"),
        (
            "dependencia_administrativa",
            "Dependência administrativa (escola)"
        ),
        ("renda_familiar", "Renda mensal familiar"),
        ("internet", "Acesso à internet na residência"),
        ("lingua_estrangeira", "Tipo de língua estrangeira"),
        ("escola_ensino_medio", "Tipo de escola do Ensino Médio"),
    ]

    tabelas = {}

    for i, (coluna, titulo) in enumerate(variaveis, start=1):
        if coluna in df.columns:
            tabelas[coluna] = tabela_frequencia(
                df,
                coluna,
                titulo,
                i
            )
        else:
            print(
                f"[AVISO] Coluna '{coluna}' não encontrada."
            )

    return tabelas


def tabela_cruzada_renda_internet(df):
    if (
        "renda_familiar" not in df.columns
        or "internet" not in df.columns
    ):
        print(
            "[AVISO] Não foi possível montar a tabela cruzada."
        )
        return None

    cruzada = pd.crosstab(
        df["renda_familiar"],
        df["internet"],
        margins=True,
        margins_name="Total"
    )

    cruzada_pct = (
        pd.crosstab(
            df["renda_familiar"],
            df["internet"],
            normalize="index"
        )
        .mul(100)
        .round(2)
    )

    print(
        "\nTabela 7 — Renda mensal familiar "
        "x Acesso à internet (frequência)"
    )
    print(cruzada)

    print(
        "\nTabela 7b — Renda mensal familiar "
        "x Acesso à internet (% por linha)"
    )
    print(cruzada_pct)

    print("Fonte: Microdados ENEM 2020 (INEP)")

    cruzada.to_csv(
        os.path.join(
            PASTA_SAIDA,
            "tabelas",
            "tabela_7_renda_x_internet.csv"
        )
    )

    cruzada_pct.to_csv(
        os.path.join(
            PASTA_SAIDA,
            "tabelas",
            "tabela_7b_renda_x_internet_pct.csv"
        )
    )

    return cruzada


ORDEM_RENDA = [
    "Nenhuma Renda",
    "Até R$ 1.045,00",
    "De R$ 1.045,01 até R$ 1.567,50",
    "De R$ 1.567,51 até R$ 2.090,00",
    "De R$ 2.090,01 até R$ 2.612,50",
    "De R$ 2.612,51 até R$ 3.135,00",
    "De R$ 3.135,01 até R$ 4180,00",
    "De R$ 4180,01 até R$ 5.225,00",
    "De R$ 5.225,01 até R$ 6.270,00",
    "De R$ 6.270,01 até R$ 7.315,00",
    "De R$ 7.315,01 até R$ 8.360,00",
    "De R$ 8.360,01 até R$ 9.405,00",
    "De R$ 9.405,01 até R$ 10.450,00",
    "De R$ 10.450,01 até R$ 12.540,00",
    "De R$ 12.540,01 até R$ 15.675,00",
    "De R$ 15.675,01 até R$ 20.900,00",
    "Acima de R$ 20.900,00",
]

plt.style.use("seaborn-v0_8-whitegrid")


def _texto_seguro(texto):
    return str(texto).replace("$", r"\$")


def grafico_barras(df, coluna, titulo, numero, ordem=None):
    if coluna not in df.columns:
        print(
            f"[AVISO] Coluna '{coluna}' "
            f"não encontrada para o gráfico {numero}."
        )
        return

    contagem = df[coluna].value_counts()

    if ordem:
        contagem = contagem.reindex(
            [c for c in ordem if c in contagem.index]
        )
    else:
        contagem = contagem.sort_index()

    total = contagem.sum()

    rotulos = [
        _texto_seguro(c) for c in contagem.index
    ]

    fig, ax = plt.subplots(figsize=(10, 6))

    barras = ax.bar(
        rotulos,
        contagem.values,
        color="#4C72B0",
        edgecolor="white",
        linewidth=0.8
    )

    for barra, valor in zip(barras, contagem.values):
        pct = valor / total * 100

        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height(),
            f"{valor}\n({pct:.1f}%)",
            ha="center",
            va="bottom",
            fontsize=8
        )

    ax.set_title(
        f"Gráfico {numero} — {titulo}",
        fontsize=14,
        fontweight="bold",
        pad=15
    )

    ax.set_xlabel(titulo, fontsize=11)
    ax.set_ylabel("Frequência", fontsize=11)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.margins(y=0.12)

    plt.xticks(
        rotation=40,
        ha="right",
        fontsize=9
    )

    plt.tight_layout()

    caminho = os.path.join(
        PASTA_SAIDA,
        "graficos",
        f"grafico_{numero}_{coluna}_barras.png"
    )

    plt.savefig(caminho, dpi=220)
    plt.close(fig)

    print(
        f"Gráfico {numero} salvo em: {caminho} "
        "(Fonte: Microdados ENEM 2020 - INEP)"
    )


def grafico_pizza(df, coluna, titulo, numero):
    if coluna not in df.columns:
        print(
            f"[AVISO] Coluna '{coluna}' "
            f"não encontrada para o gráfico {numero}."
        )
        return

    contagem = df[coluna].value_counts()

    percentual = (
        df[coluna]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )

    print(
        f"\nGráfico {numero} — {titulo} (percentuais)"
    )

    for categoria in contagem.index:
        print(
            f"  {categoria}: "
            f"{contagem[categoria]} "
            f"({percentual[categoria]}%)"
        )

    cores = plt.get_cmap("Set2").colors

    fig, ax = plt.subplots(figsize=(8, 7))

    wedges, _, autotexts = ax.pie(
        contagem.values,
        autopct="%1.1f%%",
        startangle=90,
        colors=cores,
        pctdistance=0.75,
        wedgeprops={
            "edgecolor": "white",
            "linewidth": 1.5
        }
    )

    for texto in autotexts:
        texto.set_fontsize(9)
        texto.set_fontweight("bold")
        texto.set_color("white")

    ax.legend(
        wedges,
        contagem.index,
        title=titulo,
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        fontsize=9,
        title_fontsize=10
    )

    ax.set_title(
        f"Gráfico {numero} — {titulo}",
        fontsize=14,
        fontweight="bold",
        pad=15
    )

    plt.tight_layout()

    caminho = os.path.join(
        PASTA_SAIDA,
        "graficos",
        f"grafico_{numero}_{coluna}_pizza.png"
    )

    plt.savefig(
        caminho,
        dpi=220,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(
        f"Gráfico {numero} salvo em: {caminho} "
        "(Fonte: Microdados ENEM 2020 - INEP)"
    )


if __name__ == "__main__":
    df = carregar_dados()

    print(
        f"Base carregada: {len(df)} registros, "
        f"colunas: {list(df.columns)}"
    )

    gerar_todas_as_tabelas(df)

    tabela_cruzada_renda_internet(df)

    grafico_barras(
        df,
        "renda_familiar",
        "Renda mensal familiar",
        numero=1,
        ordem=ORDEM_RENDA
    )

    grafico_barras(
        df,
        "internet",
        "Acesso à internet na residência",
        numero=2
    )

    grafico_pizza(
        df,
        "internet",
        "Acesso à internet na residência",
        numero=3
    )

    grafico_pizza(
        df,
        "telefone_celular",
        "Telefone celular na residência",
        numero=4
    )

    print(
        "\nPronto! Tabelas (.csv) e gráficos (.png) "
        "estão na pasta 'resultados/'."
    )

    print(
        "Lembrete: escreva a análise de cada tabela/gráfico "
        "usando os números impressos acima"
    )

    print(
        "e verbos impessoais "
        "(ex: 'Entende-se, pela Tabela 1, que...')."
    )
