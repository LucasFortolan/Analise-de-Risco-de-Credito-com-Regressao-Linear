import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ==========================================================
# Dataset: Loan Dataset (Kaggle)
# https://www.kaggle.com/datasets/prakashraushan/loan-dataset
#
# Objetivo:
# Analisar a relação entre idade do cliente e renda anual
# aplicando correlação e regressão linear.
# ==========================================================

# Leitura do dataset
df = pd.read_csv("LoanDatasetLoansDatasest.csv")

# Seleção das colunas de interesse
print("Amostra do DataFrame:")
print(df[['customer_age', 'customer_income']].rename(
    columns={'customer_age': 'Idade', 'customer_income': 'Salario Anual'}
).head(3))

# ===========================
# Limpeza e transformação
# ===========================

df['customer_age'] = df['customer_age'].astype(int)

df['customer_income'] = (
    df['customer_income']
    .str.replace(',', '', regex=False)
    .astype(float)
)

df['loan_amnt'] = (
    df['loan_amnt']
    .str.replace('£', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

# ===========================
# Correlação
# ===========================

print("\nTabela de Correlacao:")
colunas_corr = ['customer_age', 'employment_duration', 'customer_income',
                'loan_amnt', 'term_years', 'cred_hist_length']

correlacao = df[colunas_corr].corr()
print(correlacao)

# Correlação específica entre idade e renda
corr_idade_renda = df['customer_age'].corr(df['customer_income'])
print(f"\nCorrelacao (Idade x Renda Anual): r = {corr_idade_renda:.3f} = {corr_idade_renda*100:.2f}%")

# ===========================
# Cálculo manual da correlação (validação)
# ===========================

x_vals = df['customer_age']
y_vals = df['customer_income']
n = len(df)

somaX = x_vals.sum()
somaY = y_vals.sum()
XX = (x_vals ** 2).sum()
YY = (y_vals ** 2).sum()
somaXY = (x_vals * y_vals).sum()

r_manual = (n * somaXY - somaX * somaY) / math.sqrt((n * XX - somaX**2) * (n * YY - somaY**2))

print(f"Correlacao manual (validacao): r = {r_manual:.3f} = {r_manual*100:.2f}%")

# ===========================
# Regressão Linear
# ===========================

X = df[['customer_age']]
y = df['customer_income']

modelo = LinearRegression()
modelo.fit(X, y)

y_pred = modelo.predict(X)

# Coeficientes
coef_angular = modelo.coef_[0]
coef_linear = modelo.intercept_

print("\nEquacao da Regressao Linear:")
print(f"y = {coef_angular:.3f}x + {coef_linear:.3f}")

# ===========================
# Avaliação do modelo
# ===========================

mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = math.sqrt(mse)
r2 = r2_score(y, y_pred)

print("\nMetricas do Modelo:")
print(f"MAE  = {mae:.2f}")
print(f"MSE  = {mse:.2f}")
print(f"RMSE = {rmse:.2f}")
print(f"R**2   = {r2:.3f}")

# ===========================
# Visualização
# ===========================

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.4)
plt.plot(X, y_pred, color='red', linewidth=2)
plt.title("Regressao Linear: Idade x Renda Anual (£)")
plt.xlabel("Idade")
plt.ylabel("Renda Anual (£)")
plt.grid(True)
plt.show()