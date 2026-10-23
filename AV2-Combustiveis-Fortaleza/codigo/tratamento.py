import pandas as pd

# 1. Ler o arquivo (separador ; e decimal ,)
df = pd.read_csv("dados/ANP_Fortaleza_gasolina_etanol_2025 (1).csv",
                 sep=";", decimal=",", encoding="utf-8-sig")

# 2. Ficar só com as colunas que importam
df = df[["Revenda", "Bairro", "Produto", "Data da Coleta", "Valor de Venda", "Bandeira"]]

# 3. Converter a data
df["Data da Coleta"] = pd.to_datetime(df["Data da Coleta"], format="%d/%m/%Y")

# 4. Ver se tem valores faltando ou duplicados
print(df.isna().sum())
print(df.duplicated().sum())

# 5. Média diária de cada combustível
tabela = df.pivot_table(index="Data da Coleta",
                        columns="Produto",
                        values="Valor de Venda",
                        aggfunc="mean")

# 6. Renomear e tirar datas sem os dois produtos
tabela = tabela.rename(columns={"ETANOL": "etanol", "GASOLINA": "gasolina"})
tabela = tabela.dropna()

# 7. Salvar para o resto da equipe usar
tabela.to_csv("dados/dados_tratados.csv")

print(tabela.describe())
print(len(tabela), "datas")