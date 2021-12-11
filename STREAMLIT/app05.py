import streamlit as st

st.title('Barra lateral')

seleccion = st.sidebar.selectbox('Seleccionar si o no: ',
        ['Si', 'No'])

st.write(f'Has seleccionado {seleccion}')
