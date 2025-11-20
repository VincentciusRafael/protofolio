import streamlit as st

with open("home.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=800)
