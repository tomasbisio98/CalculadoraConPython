import streamlit as st
from src.calculator import add, subtract, multiply, divide

st.title("Calculadora")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Primer número", value=0.0, format="%g")
with col2:
    b = st.number_input("Segundo número", value=0.0, format="%g")

st.write("")

col1, col2, col3, col4 = st.columns(4)
operation = None
if col1.button("➕ Sumar", use_container_width=True):
    operation = ("add", add(a, b))
if col2.button("➖ Restar", use_container_width=True):
    operation = ("subtract", subtract(a, b))
if col3.button("✖️ Multiplicar", use_container_width=True):
    operation = ("multiply", multiply(a, b))
if col4.button("➗ Dividir", use_container_width=True):
    try:
        operation = ("divide", divide(a, b))
    except ValueError:
        st.error("Burrooooooo")

if operation:
    st.markdown(f"## Resultado: {operation[1]:g}")
