# Análise de Risco de Crédito com Correlação e Regressão Linear

Este projeto apresenta uma análise estatística aplicada a um dataset de empréstimos, com foco em investigar a relação entre a **idade do cliente** e sua **renda anual**, utilizando técnicas de **correlação** e **regressão linear**.

O estudo inclui etapas de preparação e exploração dos dados, tratamento de variáveis numéricas armazenadas como texto e aplicação de um modelo de **Regressão Linear** para estimar a renda anual com base na idade.

---

## Objetivo

Analisar a relação entre **Idade (customer_age)** e **Renda Anual (customer_income)**, identificando o nível de correlação entre essas variáveis e aplicando um modelo de regressão para realizar previsões.

---

## Etapas do Projeto

- Leitura e carregamento do dataset
- Limpeza e transformação de variáveis numéricas
- Construção da matriz de correlação entre variáveis relevantes
- Cálculo de correlação utilizando Pandas e validação manual
- Aplicação de Regressão Linear com Scikit-learn
- Avaliação do modelo utilizando métricas estatísticas
- Visualização gráfica da reta de regressão sobre os dados reais

---

## Avaliação do Modelo

O modelo de regressão linear foi avaliado utilizando as seguintes métricas:

- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² (Coeficiente de Determinação)

---

## Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Scikit-learn

---

## Documentação Complementar

Foi realizado pesquisas e explicações de códigos para melhor aproveitamento em um documento Word.  
<a href="https://docs.google.com/document/d/1XJDvGfE2ZGKXhorBunMIHLWPjxcNI8a7Oa0neyupel4/edit?usp=sharing">Acesse o Documento</a>

---

## Dataset

O dataset utilizado foi obtido no Kaggle:  
https://www.kaggle.com/datasets/prakashraushan/loan-dataset

---

## Visualização

O projeto gera um gráfico de dispersão entre idade e renda anual, exibindo a reta da regressão linear em vermelho, permitindo analisar visualmente o comportamento e tendência dos dados.

---
