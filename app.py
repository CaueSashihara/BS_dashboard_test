
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- CONFIG ---
st.set_page_config(layout="wide", page_title="Dashboard Canal Indireto | Boston Scientific")

# --- LOGO ---
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("images/logo boston.png", width=120)
with col_title:
    st.title("Boston Scientific LatAm - Dashboard de Canal Indireto")

# --- SIDEBAR ---
st.sidebar.header("Filtros")
pais = st.sidebar.multiselect("País:", options=["Brasil", "Argentina", "México"], default="Brasil")
bu = st.sidebar.multiselect("Unidade de Negócio:", [
    "Cardiologia Intervencionista", "Neuromodulação",
    "Urologia", "Gastroenterologia", "Pulmonar", "Oncologia"
])
tier = st.sidebar.selectbox("Tier:", ["Silver", "Gold", "Platinum"])
vendas_min = st.sidebar.slider("Valor Mínimo de Vendas (USD):", 0, 10000000, 2500000)
st.sidebar.button("Aplicar Filtros")

# --- IMAGEM POR BU ---
bu_images = {
    "Cardiologia Intervencionista": "images/SYNERGY BP DES Hero.png",
    "Neuromodulação": "images/Illumina 3D™ portfolio.png",
    "Urologia": "images/GreenLight XPS™ Laser Therapy System.jpg",
    "Gastroenterologia": "images/SpyGlass DS Direct Visualization System.jpg",
    "Pulmonar": "images/TS atomsphere nobg.png",
    "Oncologia": "images/Mantis_new_angle_CU.png",
}

if bu:
    for unidade in bu:
        if unidade in bu_images:
            st.image(bu_images[unidade], use_column_width=True)

# --- METRICAS (mock) ---
st.markdown("""
<div style='display: flex; justify-content: space-around;'>
    <div style='background-color:#003c71; padding:20px; border-radius:10px; color:white;'>
        <h4>Total de Parceiros</h4><h2>48</h2></div>
    <div style='background-color:#003c71; padding:20px; border-radius:10px; color:white;'>
        <h4>Vendas Totais</h4><h2>$3.450.000</h2></div>
    <div style='background-color:#003c71; padding:20px; border-radius:10px; color:white;'>
        <h4>Média BSC Score</h4><h2>84%</h2></div>
</div>
""", unsafe_allow_html=True)

# --- GRÁFICO MOCK ---
df_mock = pd.DataFrame({
    "País": ["Brasil", "Argentina", "México"],
    "Parceiros": [21, 15, 12]
})
fig = px.bar(df_mock, x="País", y="Parceiros", title="Distribuição de Parceiros por País",
             color_discrete_sequence=["#003c71"])
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("Dashboard de uso exclusivo para gestão do canal indireto na América Latina.")
