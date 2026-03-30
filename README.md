# Análise Estatística de Empréstimos com Correlação e Regressão Linear

Este projeto apresenta uma análise estatística aplicada a um dataset de empréstimos, com foco em investigar a relação entre a **idade do cliente** e sua **renda anual**, utilizando técnicas de **correlação** e **regressão linear**.

O estudo inclui etapas de preparação e exploração dos dados, tratamento de variáveis numéricas armazenadas como texto e aplicação de um modelo de **Regressão Linear** para estimar a renda anual com base na idade.

---

## Objetivo

Analisar a relação entre **Idade (customer_age)** e **Renda Anual (customer_income)**, identificando o nível de correlação entre essas variáveis e aplicando um modelo de regressão linear para realizar previsões.

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

Foram realizadas pesquisas e explicações de códigos para melhor aproveitamento em um documento Word:  
<a href="https://docs.google.com/document/d/1XJDvGfE2ZGKXhorBunMIHLWPjxcNI8a7Oa0neyupel4/edit?usp=sharing">Acesse o Documento</a>

---

## Dataset

O dataset utilizado foi obtido no Kaggle:  
https://www.kaggle.com/datasets/prakashraushan/loan-dataset

---

## Visualização

O projeto gera um gráfico de dispersão entre idade e renda anual, exibindo a reta da regressão linear em vermelho, permitindo analisar visualmente a tendência entre as variáveis.

---

## Resultados Obtidos

A análise estatística indicou uma **correlação positiva fraca** entre idade e renda anual:

- Correlação (Idade x Renda Anual): **r = 0.173 (17.31%)**
- Correlação manual (validação): **r = 0.173 (17.31%)**

A equação obtida pelo modelo de Regressão Linear foi:

\[
y = 1686.375x + 19308.536
\]

O modelo estima que a renda anual aumenta aproximadamente **£1686** para cada ano adicional de idade.

### Métricas do Modelo

- **MAE** = 29861.50  
- **MSE** = 3726389901.22  
- **RMSE** = 61044.16  
- **R²** = 0.030  

---

## Conclusão

Os resultados mostram que, apesar de existir uma tendência positiva, a variável **idade possui baixo poder explicativo sobre a renda anual**, pois o modelo apresentou **R² = 0.030**, indicando que apenas **3% da variação da renda** é explicada pela idade.

Isso sugere que outras variáveis do dataset (ex: tempo de emprego, histórico de crédito, valor do empréstimo) devem ser consideradas para aumentar o poder preditivo do modelo.

---
