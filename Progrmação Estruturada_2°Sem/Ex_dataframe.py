import pandas as pd

file = "imoveis_brasil.csv"
df = pd.read_csv(file)
#  1. 
df.head(5)
df.tail(5)
df.sample(5)
#  2.
df.shape
#  3.
df.columns
#  4.
df.dtypes
#  5.
df.describe()
#  6. 
df.info()
#  7.
df["Tipo_Imovel"].unique()
#  8.
filtro = df["Valor_Imovel"]>1000000
df.loc[filtro]
#  9.
coluna = ['Cidade', 'Bairro', 'Valor_Imovel']
df[coluna]
#  10.
filtro = df["Cidade"] =="Curitiba"
df.loc[filtro]
#  11.
df.isnull().sum()
#  12.
df.sort_values("Valor_Imovel", ascending=False)
#  13.
df["Valor_Imovel"].mean()
#  14.
df["Valor_Imovel"].medium()
#  15.
df["Valor_Imovel"].std()
#  16.
df["Area_m2"].min()
df["Area_m2"].max()
#  17.
media = df["Valor_Imovel"].mean()
filtro = df["Valor_Imovel"]>media
df.loc[filtro]
#  18.
valor = df["Valor_Imovel"]
area = df["Area_m2"]
df["valor_m2"] = valor / area
#  19.
dic = {"Cidade": "Teste", "Valor_Imovel":999, "Area_m2":100}
df.loc[len(df)] = dic
#  20.
df.isnull().sum()
#  21.
filtro = df["Numero_Quartos"]!=5
df = df.loc[filtro]
#  22.
df.drop(columns=["ID_Imovel"])
#  23.
filtro = df["Cidade"]!="Teste"
df = df.loc[filtro]
#  24.
