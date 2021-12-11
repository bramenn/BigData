import streamlit as st
import pandas as pd
import numpy as np


st.title('Gráficos')

gr_datos = pd.DataFrame(np.random.randn(10,2),
        columns=[f'Col{i+1}' for i in range(2)])

st.line_chart(gr_datos)
