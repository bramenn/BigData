import streamlit as st

valor = st.slider('valor')
st.write(valor, 'El cuadrado es: ', valor*valor)
