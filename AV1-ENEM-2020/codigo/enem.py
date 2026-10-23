from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CAMINHO_DADOS = BASE_DIR / "dados" / "dados_enem_2020.xlsx"
PASTA_RESULTADOS = BASE_DIR / "resultados"
PASTA_RESULTADOS.mkdir(parents=True, exist_ok=True)

import pandas as pd
import matplotlib.pyplot as plt




df = pd.read_excel(CAMINHO_DADOS)




provas_objetivas = [
    "Nota da prova de Ciências da Natureza",
    "Nota da prova de Ciências Humanas",
    "Nota da prova de Linguagens e Códigos",
    "Nota da prova de Matemática"
]




def calcular_medidas(coluna):

    dados = df[coluna].dropna()

    moda = dados.mode()

    if len(moda) > 0:
        moda = ", ".join(map(str, moda.tolist()))
    else:
        moda = "Sem moda"

    q1 = dados.quantile(0.25)
    q3 = dados.quantile(0.75)

    return {
        "Variável": coluna,
        "Média": dados.mean(),
        "Mediana": dados.median(),
        "Moda": moda,
        "Desvio Padrão": dados.std(),
        "Mínimo": dados.min(),
        "Q1": q1,
        "Q3": q3,
        "Máximo": dados.max(),
        "Amplitude": dados.max() - dados.min(),
        "IQR": q3 - q1,
        "Variância": dados.var()
    }




resultados_objetivas = []

for prova in provas_objetivas:
    resultados_objetivas.append(
        calcular_medidas(prova)
    )

tabela_objetivas = pd.DataFrame(resultados_objetivas)


colunas_numericas = [
    "Média",
    "Mediana",
    "Desvio Padrão",
    "Mínimo",
    "Q1",
    "Q3",
    "Máximo",
    "Amplitude",
    "IQR",
    "Variância"
]

tabela_objetivas[colunas_numericas] = (
    tabela_objetivas[colunas_numericas].round(2)
)




redacao = "Nota da prova de redação"

tabela_redacao = pd.DataFrame([
    calcular_medidas(redacao)
])

tabela_redacao[colunas_numericas] = (
    tabela_redacao[colunas_numericas].round(2)
)




print("\n")
print("=" * 80)
print("4.5.1 - MEDIDAS DE POSIÇÃO E DISPERSÃO")
print("NOTAS DAS PROVAS OBJETIVAS")
print("=" * 80)

print(tabela_objetivas.to_string(index=False))


print("\n")
print("=" * 80)
print("4.5.2 - MEDIDAS DE POSIÇÃO E DISPERSÃO")
print("NOTA DA PROVA DE REDAÇÃO")
print("=" * 80)

print(tabela_redacao.to_string(index=False))




tv = "Na sua residência tem TV por assinatura?"
internet = "Na sua residência tem acesso à Internet?"

tabela_tv_internet = pd.crosstab(
    df[tv],
    df[internet]
)


print("\n")
print("=" * 80)
print("TV POR ASSINATURA × INTERNET")
print("=" * 80)

print(tabela_tv_internet)



escola = "Tipo de escola do Ensino Médio"
lingua = "Língua Estrangeira "

tabela_escola_lingua = pd.crosstab(
    df[escola],
    df[lingua]
)


print("\n")
print("=" * 80)
print("ESCOLA × LÍNGUA ESTRANGEIRA")
print("=" * 80)

print(tabela_escola_lingua)




with pd.ExcelWriter(PASTA_RESULTADOS / "resultados_enem.xlsx") as writer:

    tabela_objetivas.to_excel(
        writer,
        sheet_name="Provas Objetivas",
        index=False
    )

    tabela_redacao.to_excel(
        writer,
        sheet_name="Redação",
        index=False
    )

    tabela_tv_internet.to_excel(
        writer,
        sheet_name="TV x Internet"
    )

    tabela_escola_lingua.to_excel(
        writer,
        sheet_name="Escola x Lingua"
    )


print("\n")
print("Arquivo 'resultados_enem.xlsx' criado com sucesso!")




plt.figure(figsize=(10, 6))

plt.hist(
    df["Nota da prova de Matemática"].dropna(),
    bins=20,
    edgecolor="black"
)

plt.title("Histograma - Nota da prova de Matemática")
plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.grid(axis="y", alpha=0.3)

plt.show()



plt.figure(figsize=(10, 6))

plt.hist(
    df["Nota da prova de redação"].dropna(),
    bins=20,
    edgecolor="black"
)

plt.title("Histograma - Nota da prova de Redação")
plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.grid(axis="y", alpha=0.3)

plt.show()




plt.figure(figsize=(8, 6))

plt.boxplot(
    df["Nota da prova de Matemática"].dropna()
)

plt.title("Box Plot - Nota da prova de Matemática")
plt.ylabel("Nota")
plt.grid(axis="y", alpha=0.3)

plt.show()




plt.figure(figsize=(8, 6))

plt.boxplot(
    df["Nota da prova de redação"].dropna()
)

plt.title("Box Plot - Nota da prova de Redação")
plt.ylabel("Nota")
plt.grid(axis="y", alpha=0.3)

plt.show()