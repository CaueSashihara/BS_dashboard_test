
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(layout="wide", page_title="Dashboard Canal Indireto | Boston Scientific")

# --- LOGO + TÍTULO ---
col_logo, col_title = st.columns([1, 10])
with col_logo:
    st.image("images/logo boston.png", width=60)
with col_title:
    st.markdown("""
        <h2 style='margin-bottom: 0;'>Boston Scientific LatAm</h2>
        <h5 style='color: gray; margin-top: 0;'>Dashboard de Canal Indireto</h5>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("🎛️ Filtros")
pais = st.sidebar.multiselect("País:", options=["Brasil", "México", "Argentina", "Colômbia", "Chile", "Peru", "Outros"], default=["Brasil"])
bu = st.sidebar.multiselect("Unidade de Negócio:", [
    "Cardiologia Intervencionista", "Neuromodulação",
    "Urologia", "Gastroenterologia", "Pulmonar", "Oncologia"
])
tier = st.sidebar.selectbox("Tier:", ["Silver", "Gold", "Platinum"])
vendas_min = st.sidebar.slider("Valor Mínimo de Vendas (BRL):", 0, 300000000, 50000000)

# --- MINI ICONES DE BU ---
bu_images = {
    "Cardiologia Intervencionista": "images/SYNERGY BP DES Hero.png",
    "Neuromodulação": "images/Illumina 3D™ portfolio.png",
    "Urologia": "images/GreenLight XPS™ Laser Therapy System.jpg",
    "Gastroenterologia": "images/SpyGlass DS Direct Visualization System.jpg",
    "Pulmonar": "images/TS atomsphere nobg.png",
    "Oncologia": "images/Mantis_new_angle_CU.png",
}

if bu:
    st.markdown("**Unidades Selecionadas:**")
    bu_cols = st.columns(len(bu))
    for i, unidade in enumerate(bu):
        if unidade in bu_images:
            with bu_cols[i]:
                st.image(bu_images[unidade], width=60, caption=unidade)

# --- NOVOS DADOS ---
canal_data = pd.DataFrame({
    "País": ["Brasil", "México", "Argentina", "Colômbia", "Chile", "Peru", "Outros"],
    "Parceiros": [52, 36, 8, 7, 6, 5, 6],
    "Faturamento (BRL milhões)": [138, 90, 20, 18, 14, 12, 8]
})

# --- MÉTRICAS ---
st.markdown("""
<style>
.metric-box {background-color:#003c71; padding:18px; border-radius:8px; color:white; text-align:center; width:100%}
</style>
<div style='display: flex; gap: 20px;'>
  <div class='metric-box'><h5>Total de Parceiros</h5><h3>120</h3></div>
  <div class='metric-box'><h5>Faturamento Estimado</h5><h3>R$ 300 milhões</h3></div>
  <div class='metric-box'><h5>Média BSC Score</h5><h3>84%</h3></div>
</div>
""", unsafe_allow_html=True)

# --- GRÁFICOS ---
st.subheader("Distribuição de Canais por País")
fig = px.bar(canal_data, x="País", y="Parceiros", color="País", color_discrete_sequence=px.colors.qualitative.Safe)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Participação no Faturamento por País")
fig2 = px.pie(canal_data, names="País", values="Faturamento (BRL milhões)", color_discrete_sequence=px.colors.qualitative.Prism)
st.plotly_chart(fig2, use_container_width=True)

# --- PROJETOS ESTRATÉGICOS ---
st.subheader("📊 Andamento dos Projetos Estratégicos - Plano de 90 Dias")
st.markdown("""
**Fase 1: Alinhamento e Diagnóstico (0-30 dias)**
- Workshops com BUs e Distribuidores
- Integração inicial dos dados sell-out/inventário
- Implementação de gestão à vista e priorização de rupturas

**Fase 2: Padronização e Capacitação (31-60 dias)**
- Framework BSC + CPFR piloto com parceiros
- Treinamento e política de precificação
- Implantação da jornada do parceiro e scorecard

**Fase 3: Escala e Execução (61-90 dias)**
- Análises preditivas
- Campanhas de ativação em produtos estratégicos
- Programa de incentivos BS4P
""")

st.markdown("---")
st.caption("Dashboard exclusivo para gestão do canal indireto LatAm | Boston Scientific")
