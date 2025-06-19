from turtledemo.penrose import start

import streamlit as st

st.header("Lanzar una moneda")

number_of_trials = st.slider("¿Numero de intentos?", 1 , 1000, 10)
start_botton = st.button("Ejecutar")

if start_botton:
    st.write(f"Experimento con {number_of_trials} intentos en curso.")

st.write("Esta aplicacion aun no es funcional. En construccion.")