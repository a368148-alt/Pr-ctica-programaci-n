import streamlit as st
st.title("Mi aplicación para calcular el área de un círculo 🤓")
import math
radio = st.slider("Selecciona el radio", 0.0, 10.0, 5.0)
area = math.pi*radio**2
st.write(f"El área del cículo con radio {radio} es:{area:.2t}")
