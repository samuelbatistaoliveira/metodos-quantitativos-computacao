from scipy.stats import pearsonr, linregress
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


pasta_av2 = Path(__file__).resolve().parent.parent
arquivo = pasta_av2 / "dados" / "dados_tratados.csv"

dados = pd.read_csv(arquivo)

print("Dados carregados com sucesso!")
print(dados.head())

x = dados["etanol"]
y = dados["gasolina"]

correlacao, p_valor = pearsonr(x, y)

print(f"Correlação de Pearson: {correlacao:.4f}")
print(f"Valor-p: {p_valor:.4f}")

modelo = linregress(x, y)

coeficiente_angular = modelo.slope
intercepto = modelo.intercept
r_quadrado = modelo.rvalue ** 2

print(f"Coeficiente angular: {coeficiente_angular:.4f}")
print(f"Intercepto: {intercepto:.4f}")
print(f"R²: {r_quadrado:.4f}")
print(f"Equação: gasolina = {intercepto:.4f} "
      f"+ ({coeficiente_angular:.4f} × etanol)")

plt.scatter(x, y)

x_ordenado = x.sort_values()
y_estimado = intercepto + coeficiente_angular * x_ordenado

plt.plot(x_ordenado, y_estimado, color="red", label="Regressão linear")
plt.legend()

plt.title("Preços de combustíveis em Fortaleza - 2025")
plt.xlabel("Preço médio do etanol (R$/L)")
plt.ylabel("Preço médio da gasolina (R$/L)")

pasta_graficos = pasta_av2 / "resultados" / "graficos"
pasta_graficos.mkdir(parents=True, exist_ok=True)

plt.grid(True)


plt.savefig(
    pasta_graficos / "dispersao_regressao.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

pasta_tabelas = pasta_av2 / "resultados" / "tabelas"
pasta_tabelas.mkdir(parents=True, exist_ok=True)

resultados = pd.DataFrame({
    "Indicador": [
        "Correlação de Pearson",
        "Valor-p",
        "Coeficiente angular",
        "Intercepto",
        "R²"
    ],
    "Valor": [
        correlacao,
        p_valor,
        coeficiente_angular,
        intercepto,
        r_quadrado
    ]
})

resultados.to_csv(
    pasta_tabelas / "resultados_estatisticos.csv",
    index=False
)

print("Resultados estatísticos salvos com sucesso!")