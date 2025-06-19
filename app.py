from turtledemo.penrose import start

import streamlit as st
import scipy.stats
import time

st.header("Lanzar una moneda")

chart = st.line_chart([0.5])

def toss_coin(n): #funcion que emula el lanzamiento de un moneda

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size = n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count/outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

        return mean

number_of_trials = st.slider("¿Numero de intentos?", 1 , 1000, 10)
start_botton = st.button("Ejecutar")

if start_botton:
    st.write(f"Experimento con {number_of_trials} intentos en curso.")
    mean = toss_coin(number_of_trials)

# st.write("Esta aplicacion aun no es funcional. En construccion.")