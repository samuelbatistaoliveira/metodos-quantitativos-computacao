from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import het_breuschpagan 

# Caminhos do projeto
pasta_av2 = Path(__file__).resolve().parent.parent
arquivo = pasta_av2 / "dados" / "dados_tratados.csv"

pasta_graficos = pasta_av2 / "resultados" / "graficos"
pasta_tabelas = pasta_av2 / "resultados" / "tabelas"

pasta_graficos.mkdir(parents=True, exist_ok=True)
pasta_tabelas.mkdir(parents=True, exist_ok=True)

# Carregar os dados
dados = pd.read_csv(arquivo)

x = dados["etanol"]
y = dados["gasolina"]

# Ajustar a regressão linear
X = sm.add_constant(x)
modelo = sm.OLS(y, X).fit()

# Modelo com fórmula, necessário para a ANOVA
modelo_anova = sm.formula.ols(
    "gasolina ~ etanol",
    data=dados
).fit()

valores_estimados = modelo.fittedvalues
residuos = modelo.resid


# 1. Gráfico dos resíduos
plt.figure()
plt.scatter(valores_estimados, residuos)
plt.axhline(y=0, color="red", linestyle="--")
plt.title("Resíduos versus valores estimados")
plt.xlabel("Valores estimados da gasolina (R$/L)")
plt.ylabel("Resíduos (R$/L)")
plt.grid(True)

plt.savefig(
    pasta_graficos / "residuos_valores_estimados.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# 2. Histograma dos resíduos
plt.figure()
plt.hist(residuos, bins="auto", edgecolor="black")
plt.title("Distribuição dos resíduos")
plt.xlabel("Resíduos (R$/L)")
plt.ylabel("Frequência")
plt.grid(True)

plt.savefig(
    pasta_graficos / "histograma_residuos.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# 3. Gráfico Q-Q para avaliar normalidade
fig = sm.qqplot(residuos, line="45", fit=True)
plt.title("Gráfico Q-Q dos resíduos")
fig.savefig(
    pasta_graficos / "qqplot_residuos.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close(fig)


# 4. Teste de normalidade de Shapiro-Wilk
# O teste é aplicado aos resíduos do modelo.
if 3 <= len(residuos) <= 5000:
    estatistica_shapiro, p_shapiro = shapiro(residuos)
    normalidade = (
        "Sem evidência suficiente contra a normalidade"
        if p_shapiro >= 0.05
        else "Evidência de desvio da normalidade"
    )
else:
    estatistica_shapiro = float("nan")
    p_shapiro = float("nan")
    normalidade = (
        "Teste de Shapiro-Wilk não executado: "
        "amostra fora do intervalo de 3 a 5000 observações"
    )


# 5. Teste de homocedasticidade de Breusch-Pagan
bp = het_breuschpagan(residuos, X)
estatistica_bp = bp[0]
p_bp = bp[1]

homocedasticidade = (
    "Sem evidência suficiente de heterocedasticidade"
    if p_bp >= 0.05
    else "Evidência de heterocedasticidade"
)


# 6. ANOVA da regressão
tabela_anova = sm.stats.anova_lm(modelo_anova, typ=1)
tabela_anova.to_csv(
    pasta_tabelas / "anova_regressao.csv",
    index=True
)


# 7. Resumo dos testes
resultados = pd.DataFrame({
    "Indicador": [
        "Número de observações",
        "R² do modelo",
        "Estatística F",
        "Valor-p da regressão",
        "Estatística de Shapiro-Wilk",
        "Valor-p de Shapiro-Wilk",
        "Interpretação da normalidade",
        "Estatística de Breusch-Pagan",
        "Valor-p de Breusch-Pagan",
        "Interpretação da variância dos resíduos"
    ],
    "Valor": [
        len(dados),
        modelo.rsquared,
        modelo.fvalue,
        modelo.f_pvalue,
        estatistica_shapiro,
        p_shapiro,
        normalidade,
        estatistica_bp,
        p_bp,
        homocedasticidade
    ]
})

resultados.to_csv(
    pasta_tabelas / "validacao_modelo.csv",
    index=False
)

print("Validação concluída!")
print("\nANOVA da regressão:")
print(tabela_anova)
print("\nResultados dos testes:")
print(resultados.to_string(index=False))
print(f"\nGráficos salvos em: {pasta_graficos}")
print(f"Tabelas salvas em: {pasta_tabelas}")