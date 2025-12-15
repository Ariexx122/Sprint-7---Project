import streamlit as st
import plotly.graph_objects as go
import pandas as pd

car_data = pd.read_csv("vehicles_us.csv")

st.header("Smart car recommender")
st.write("Answer a few questions and get a car recommendation!")

# Formulario de preferencias
with st.form("car_preferences"):
    col1, col2 = st.columns(2)

    with col1:
        max_price = st.number_input("Presupuesto máximo ($)",
                                    min_value=1000, max_value=50000, value=15000)
        car_type = st.selectbox("Tipo de vehículo preferido",
                                ['Any type'] + list(car_data['type'].dropna().unique()))
        min_cylinders = st.selectbox("Cilindros mínimos",
                                     [4.0, 6.0, 8.0], index=0)

    with col2:
        max_odometer = st.number_input("Millaje máximo",
                                       min_value=10000, max_value=300000, value=150000)
        min_condition = st.selectbox("Condición mínima",
                                     ['salvage', 'fair', 'good', 'like new', 'excellent'])

    submit_button = st.form_submit_button("🔍 Buscar Recomendaciones")

if submit_button:
    # Filtrar datos según preferencias
    filtered_cars = car_data[
        (car_data['price'] <= max_price) &
        (car_data['odometer'] <= max_odometer) &
        (car_data['cylinders'] >= min_cylinders)
    ]

    filtered_cars = filtered_cars.dropna(
        subset=['model_year', 'price', 'odometer'])
    filtered_cars['model_year'] = filtered_cars['model_year'].astype(int)
    filtered_cars = filtered_cars[filtered_cars['price'] >= 500]

    if car_type != 'Any type':
        filtered_cars = filtered_cars[filtered_cars['type'] == car_type]

    condition_order = ['salvage', 'fair', 'good', 'like new', 'excellent']
    filtered_cars = filtered_cars[
        filtered_cars['condition'].isin(
            condition_order[condition_order.index(min_condition):])
    ]

    # Mostrar resultados
    st.subheader("Recomendaciones de Autos")
    if not filtered_cars.empty:
        for index, row in filtered_cars.head(10).iterrows():
            st.markdown(f"**{row['model_year']}  {row['model']}**")
            st.markdown(f"- Precio: ${row['price']}")
            st.markdown(f"- Millaje: {row['odometer']} millas")
            st.markdown(f"- Condición: {row['condition'].capitalize()}")
            st.markdown("---")
    else:
        st.write("No se encontraron autos que coincidan con tus preferencias.")
