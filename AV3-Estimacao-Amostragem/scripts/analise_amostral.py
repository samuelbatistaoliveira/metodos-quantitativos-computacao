
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_DADOS = BASE_DIR / "dados"
PASTA_RESULTADOS = BASE_DIR / "resultados"

PASTA_RESULTADOS.mkdir(exist_ok=True)

arquivos = sorted(PASTA_DADOS.glob("*.xlsx"))

if len(arquivos) != 4:
    raise ValueError("É necessário ter as 4 planilhas de outubro.")

dados = []
conjuntos_postos = []

for arquivo in arquivos:
    df = pd.read_excel(
        arquivo,
        sheet_name="POSTOS REVENDEDORES",
        header=9,
        dtype={"CNPJ": str}
    )

    df = df[
        (df["MUNICÍPIO"].astype(str).str.strip().str.upper() == "FORTALEZA") &
        (df["ESTADO"].astype(str).str.strip().str.upper() == "CEARA")
    ].copy()

    df = df[
        df["PRODUTO"].astype(str).str.strip().str.upper() != "GLP"
    ].copy()

    df["CNPJ"] = df["CNPJ"].str.replace(
        r"\D", "", regex=True
    ).str.zfill(14)

    df = df.dropna(subset=["CNPJ"])

    semana = pd.to_datetime(df["DATA DA COLETA"]).min()

    if pd.isna(semana):
        raise ValueError(f"Sem dados de Fortaleza em {arquivo.name}")

    semana_label = semana.strftime("%d/%m/%Y")

    postos = set(df["CNPJ"].unique())
    conjuntos_postos.append(postos)

    dados.append({
        "Semana": semana_label,
        "Postos distintos": len(postos),
        "Registros de preços": len(df)
    })

    print(f"\nArquivo: {arquivo.name}")
    print(f"Semana iniciada em: {semana_label}")
    print(f"Postos distintos: {len(postos)}")
    print(f"Registros de preços: {len(df)}")

resumo = pd.DataFrame(dados)

todos_postos = set.union(*conjuntos_postos)
postos_recorrentes = set.intersection(*conjuntos_postos)

print("\n===== RESULTADO CONSOLIDADO =====")
print(resumo.to_string(index=False))

print(f"\nPostos distintos no mês: {len(todos_postos)}")
print(f"Postos presentes nas 4 semanas: {len(postos_recorrentes)}")

resumo.to_csv(
    PASTA_RESULTADOS / "resumo_amostral.csv",
    index=False,
    encoding="utf-8-sig"
)

plt.figure(figsize=(10, 6))

barras = plt.bar(
    resumo["Semana"],
    resumo["Postos distintos"]
)

plt.bar_label(barras)

plt.title("Postos pesquisados em Fortaleza - Outubro/2026")
plt.xlabel("Semana (primeira data de coleta)")
plt.ylabel("Quantidade de postos distintos")

plt.ylim(0, resumo["Postos distintos"].max() * 1.2)
plt.tight_layout()

plt.savefig(
    PASTA_RESULTADOS / "postos_por_semana.png",
    dpi=300
)

plt.close()

print("\nArquivos gerados na pasta resultados:")
print("- resumo_amostral.csv")
print("- postos_por_semana.png")

from collections import Counter

frequencia = Counter()

for postos in conjuntos_postos:
    frequencia.update(postos)

recorrencia = Counter(frequencia.values())

semanas = [1, 2, 3, 4]
quantidades = [recorrencia.get(n, 0) for n in semanas]

plt.figure(figsize=(9, 5))

barras = plt.bar(semanas, quantidades)
plt.bar_label(barras)

plt.title("Recorrência dos postos - Fortaleza, outubro/2026")
plt.xlabel("Quantidade de semanas em que o posto apareceu")
plt.ylabel("Quantidade de postos")
plt.xticks(semanas)

plt.tight_layout()

plt.savefig(
    PASTA_RESULTADOS / "recorrencia_postos.png",
    dpi=300
)

plt.close()

print("\n===== RECORRÊNCIA DOS POSTOS =====")

for n, quantidade in zip(semanas, quantidades):
    print(f"{n} semana(s): {quantidade} postos")