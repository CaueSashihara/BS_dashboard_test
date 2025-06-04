
import streamlit as st
import pandas as pd
import plotly.express as px

BS_COLORS = ["#003c71", "#EBF7F9", "#35d2f5", "#feb334", "#77b900", "#008ECC", "#633D7A", "#00AE67"]

st.set_page_config(layout="wide")
st.title("DASHBOARD DE VENDAS – Boston Scientific")

st.sidebar.header("Filtros")
ano = st.sidebar.selectbox("Ano", [2022, 2023, 2024])
mes = st.sidebar.selectbox("Mês", ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"])
tipo_venda = st.sidebar.radio("Tipo da Venda", ["Venda Direta", "Canal Indireto"])

@st.cache_data
def carregar_dados():
    return pd.DataFrame({
        "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
        "Faturamento": [87000, 92000, 98000, 103000, 101000, 95000, 99000, 100000, 97000, 96000, 93000, 94000],
        "Tipo": ["Canal" if i%2==0 else "Direto" for i in range(12)]
    })

df = carregar_dados()

st.subheader("Faturamento Mensal")
fig1 = px.bar(df, x="Mês", y="Faturamento", color="Tipo", color_discrete_sequence=BS_COLORS)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Faturamento por Produto")
df_prod = pd.DataFrame({
    "Produto": ["Produto A", "Produto B", "Produto C"],
    "Vendas": [150000, 120000, 95000]
})
fig2 = px.bar(df_prod, x="Vendas", y="Produto", orientation='h', color="Produto", color_discrete_sequence=BS_COLORS)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Distribuição por Forma de Pagamento")
df_pgmt = pd.DataFrame({
    "Forma": ["Boleto", "Cartão de Crédito", "PIX"],
    "Valor": [70000, 95000, 50000]
})
fig3 = px.pie(df_pgmt, names="Forma", values="Valor", color_discrete_sequence=BS_COLORS)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.caption("Boston Scientific - Dashboard de Vendas | Versão de demonstração")
