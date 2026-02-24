import matplotlib.pyplot as plt
import pandas as pd

file = "empresas_desempenho.csv"
df=pd.read_csv(file)
df.head()
# Grafico
filtro = df["Setor"]=="Comércio"
df_com = df.loc[filtro]
plt.figure(figsize=(8,5))
plt.plot(df_com["Ano"], df_com["Receita"])
plt.title("Grafico de linha Ano x receita")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()
# Grafico de barro
df_grouped = df.groupby("Setor")["Receita"].sum().reset_index
plt.figure(figsize=(8,5))
plt.plot(df_grouped["Ano"], df_grouped["Receita"])
plt.title("Grafico de barra setor x receita")
plt.xlabel("Setor")
plt.ylabel("Receita")
plt.show()
# Grafico de pizza
df_part = df.groupby("Setor")["ParticipacaoMercado"].mean().reset_index
plt.figure(figsize=(8,5))
plt.pie(df_part["ParticipacaoMercado"], autopct="%1.1f%%")
plt.title("Grafico de pizza de participacao de mercado")
plt.show()
