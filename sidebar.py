import streamlit as st
import pandas as pd
import numpy as np

# Crear titulo de la app web
st.title('Streamlit con Sidebar')

sidebar = st.sidebar
sidebar.title('Titulo de la barra lateral')

sidebar.write('Información de mi sidebar')

st.header('Header de mi app')
st.write('Información de mi app')

if sidebar.checkbox('Show Dataframe'):
    chart_data = pd.DataFrame(
        np.random.randint(1, 10, size=(20,3)),
        columns=['a', 'b', 'c'])

    st.dataframe(chart_data)

