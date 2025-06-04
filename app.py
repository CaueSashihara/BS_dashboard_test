
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Cockpit Executivo – Canal Indireto | Boston Scientific")

# --- HEADER ---
col_logo, col_title = st.columns([1, 10])
with col_logo:
    st.image("images/logo boston.png", width=60)
with col_title:
    st.markdown("""
        <h2 style='margin-bottom: 0;'>Cockpit Executivo - LATAM</h2>
        <h5 style='color: gray; margin-top: 0;'>Canal Indireto | Boston Scientific</h5>
    """, unsafe_allow_html=True)

# --- SIMULAÇÃO DE DADOS ---
df = pd.DataFrame({
    "País": ["Brasil", "México", "Argentina", "Colômbia", "Chile", "Peru", "Outros"],
    "Canais": [52, 36, 8, 7, 6, 5, 6],
    "Faturamento (MM BRL)": [138, 90, 20, 18, 14, 12, 8],
    "BSC Score": [87, 82, 79, 80, 81, 76, 78],
})

# --- MÉTRICAS GERAIS ---
total_canais = int(df["Canais"].sum())
total_faturamento = df["Faturamento (MM BRL)"].sum()
media_score = round(df["BSC Score"].mean(), 1)

st.markdown("""
<style>
.metric-box {background-color:#003c71; padding:20px; border-radius:8px; color:white; text-align:center; width:100%}
</style>
<div style='display: flex; gap: 20px;'>
  <div class='metric-box'><h4>Parceiros Ativos</h4><h2>{}</h2></div>
  <div class='metric-box'><h4>Faturamento Total</h4><h2>R$ {:.1f}M</h2></div>
  <div class='metric-box'><h4>Média BSC Score</h4><h2>{}%</h2></div>
</div>
""".format(total_canais, total_faturamento, media_score), unsafe_allow_html=True)

# --- DISTRIBUIÇÃO VISUAL ---
col1, col2 = st.columns(2)
with col1:
    fig = px.bar(df, x="País", y="Canais", color="País", title="Distribuição de Parceiros por País",
                 color_discrete_sequence=px.colors.qualitative.Safe)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig2 = px.pie(df, names="País", values="Faturamento (MM BRL)", title="Faturamento por País",
                  color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig2, use_container_width=True)

# --- SCORECARD ---
st.subheader("📈 Scorecard por País")
st.dataframe(df.style.format({"Faturamento (MM BRL)": "R$ {:.1f}M", "BSC Score": "{:.0f}%"}))

# --- FINAL ---
st.markdown("---")
st.caption("Visão executiva LATAM – Canal Indireto | Atualizado semanalmente")
