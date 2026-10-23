import pandas as pd

df = pd.read_csv("dados/ANP_Fortaleza_gasolina_etanol_2025 (1).csv",
                 sep=";", decimal=",", encoding="utf-8-sig")

df = df[["Revenda", "Bairro", "Produto", "Data da Coleta", "Valor de Venda", "Bandeira"]]

df["Data da Coleta"] = pd.to_datetime(df["Data da Coleta"], format="%d/%m/%Y")

print(df.isna().sum())
print(df.duplicated().sum())

tabela = df.pivot_table(index="Data da Coleta",
                        columns="Produto",
                        values="Valor de Venda",
                        aggfunc="mean")

tabela = tabela.rename(columns={"ETANOL": "etanol", "GASOLINA": "gasolina"})
tabela = tabela.dropna()

tabela.to_csv("dados/dados_tratados.csv")

print(tabela.describe())
print(len(tabela), "datas")