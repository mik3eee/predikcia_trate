import streamlit as st
import pandas as pd
import joblib

# Načítanie natrénovaných modelov
model_M = joblib.load('model_M.pkl')
model_L = joblib.load('model_L.pkl')

# Vytvorenie formulára pre vstupy
st.title("Predikcia času víťaza")

length = st.number_input("Dĺžka trate (km)", min_value=0.0)
elevation = st.number_input("Prevýšenie (m)", min_value=0.0)
difficulty = st.number_input("Obtiažnosť (1-5)", min_value=1, max_value=5)
race_type = st.selectbox("Druh preteku", ['M', 'L'])

if st.button("Predikovať čas"):
    # Výpočet pomeru prevýšenie/dĺžka trate
    pomer_prevysenie_dlzka = elevation / length

    # Vytvorenie dátového rámca pre predikciu
    input_data = pd.DataFrame([[length, elevation, difficulty, pomer_prevysenie_dlzka]], 
                              columns=['trate', 'prevýšenie', 'Obtiažnosť', 'pomer_prevysenie_dlzka'])

    # Výber modelu podľa druhu trate
    if race_type == 'M':
        predicted_time = model_M.predict(input_data)[0]
    elif race_type == 'L':
        predicted_time = model_L.predict(input_data)[0]

    st.success(f"Predpokladaný čas víťaza: {predicted_time:.2f} minút")