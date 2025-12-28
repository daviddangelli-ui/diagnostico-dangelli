import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse

st.set_page_config(page_title="DANGELLI - Diagnóstico 2026", layout="centered")

st.title("🛡️ Diagnóstico de Prontidão 2026")
st.write("Avalie o nível de maturidade da sua empresa para os desafios de 2026.")

with st.form("diagnostico"):
    nome = st.text_input("Seu Nome Completo")
    empresa = st.text_input("Nome da sua Empresa")
    
    st.write("### Dê uma nota de 1 a 5 para cada área:")
    n1 = st.slider("Processos (FDC/MIT)", 1, 5, 3)
    n2 = st.slider("Presença Digital", 1, 5, 3)
    n3 = st.slider("Uso de IA", 1, 5, 3)
    n4 = st.slider("Cultura de Dados", 1, 5, 3)
    n5 = st.slider("Gestão de Pessoas", 1, 5, 3)
    
    enviado = st.form_submit_button("GERAR MEU DIAGNÓSTICO")

if enviado:
    # Criação do Gráfico
    df = pd.DataFrame({
        'Área': ["Processos", "Digital", "IA", "Dados", "Gestão"],
        'Nota': [n1, n2, n3, n4, n5]
    })
    fig = px.line_polar(df, r='Nota', theta='Área', line_close=True, range_r=[0,5])
    fig.update_traces(fill='toself')
    st.plotly_chart(fig)

    # Configuração do link (Usando o número que funcionou no seu teste!)
    numero_valido = "553183984001"
    
    # Texto da mensagem (Sem acentos para garantir 100% de sucesso)
    texto = f"Ola David! Fiz o Diagnostico 2026.\n\nNome: {nome}\nEmpresa: {empresa}\n\nNotas:\n- Processos: {n1}\n- Digital: {n2}\n- IA: {n3}\n- Dados: {n4}\n- Gestao: {n5}"
    
    # Codificação para URL
    texto_codificado = urllib.parse.quote(texto)
    link_final = f"https://wa.me/{numero_valido}?text={texto_codificado}"

    st.success("Diagnóstico gerado com sucesso!")
    st.write("Clique abaixo para enviar seu resultado e confirmar sua vaga:")
    st.link_button("✅ CONFIRMAR VAGA NA MASTERCLASS", link_final)
