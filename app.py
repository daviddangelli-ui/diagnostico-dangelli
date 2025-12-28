import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="DANGELLI - Diagnóstico 2026", layout="centered")

st.title("🛡️ Diagnóstico de Prontidão 2026")
st.write("Avalie o nível de maturidade da sua empresa.")

with st.form("diagnostico"):
    nome = st.text_input("Seu Nome Completo")
    empresa = st.text_input("Nome da sua Empresa")
    
    st.write("### Notas de 1 a 5:")
    n1 = st.slider("Processos (FDC/MIT)", 1, 5, 3)
    n2 = st.slider("Presença Digital", 1, 5, 3)
    n3 = st.slider("Uso de IA", 1, 5, 3)
    n4 = st.slider("Cultura de Dados", 1, 5, 3)
    n5 = st.slider("Gestão de Pessoas", 1, 5, 3)
    
    enviado = st.form_submit_button("GERAR MEU DIAGNÓSTICO")

if enviado:
    # Gráfico
    df = pd.DataFrame({
        'Área': ["Processos", "Digital", "IA", "Dados", "Gestão"],
        'Nota': [n1, n2, n3, n4, n5]
    })
    fig = px.line_polar(df, r='Nota', theta='Área', line_close=True, range_r=[0,5])
    fig.update_traces(fill='toself')
    st.plotly_chart(fig)

    # LINK DO WHATSAPP SEM O 9 (TESTE DEFINITIVO)
    # Formato: 55 + DDD (31) + Número (83984001)
    numero_valido = "553183984001"
    link_final = f"https://wa.me/{numero_valido}"

    st.success("Diagnóstico gerado com sucesso!")
    st.write("Clique no botão abaixo para falar com o David:")
    st.link_button("✅ CONFIRMAR VAGA NA MASTERCLASS", link_final)
