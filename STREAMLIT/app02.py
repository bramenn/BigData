import streamlit as st
import pandas as pd


st.title('Ejemplo de tabla')
df = pd.DataFrame({'A':[2,4,6,8], 'B':[1,5,4,3]})
st.write(df)
