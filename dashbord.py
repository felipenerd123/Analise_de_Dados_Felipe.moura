import streamlit as st
import pandas as pd

st.title("O")
st.text("i")
st.button("a")
st.slider("Idade", 0 ,100, 25)
df = pd.read_csv("ai")
st.dataframe(df)

import matplotlib.pyplot as plt
import pandas as pd

file = ""
df = pd.read.csv(file)
#grafico de barra


