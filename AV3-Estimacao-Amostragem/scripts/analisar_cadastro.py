
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_DADOS = BASE_DIR / "dados"
PASTA_RESULTADOS = BASE_DIR / "resultados"

PASTA_RESULTADOS.mkdir(exist_ok=True)

arquivo = PASTA_DADOS / (
    "dados-cadastrais-revendedores-varejistas-"
    "combustiveis-automoveis.csv"
)

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig",
    dtype=str,
    low_memory=False
)

fortaleza = df[
    (df["UF"].str.strip().str.upper() == "CE") &
    (df["MUNICIPIO"].str.strip().str.upper() == "FORTALEZA")
].copy()

fortaleza["CNPJ"] = (
    fortaleza["CNPJ"]
    .fillna("")
    .str.replace(r"\D", "", regex=True)
    .str.zfill(14)
)

fortaleza = fortaleza[
    fortaleza["CNPJ"].str.fullmatch(r"\d{14}")
]

populacao = fortaleza["CNPJ"].nunique()

amostra = 47

if populacao == 0:
    raise ValueError("Nenhum posto encontrado em Fortaleza.")

fracao_amostral = (amostra / populacao) * 100

print("\n===== POPULAÇÃO DE FORTALEZA =====")
print(f"Postos cadastrados: {populacao}")
print(f"Postos pesquisados por semana: {amostra}")
print(f"Fração amostral de referência: {fracao_amostral:.2f}%")

fortaleza.to_csv(
    PASTA_RESULTADOS / "cadastro_postos_fortaleza.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nArquivo gerado:")
print("- cadastro_postos_fortaleza.csv")
