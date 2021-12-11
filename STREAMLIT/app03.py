import streamlit as st


st.title('Seleccion multiple')

caja1 = st.checkbox('1')
caja2 = st.checkbox('2')

valor = 0

if caja1:
   valor = 1
elif caja2:
   valor = 2
else:
   valor = 0

st.write('Se ha seleccionado: ', valor)
