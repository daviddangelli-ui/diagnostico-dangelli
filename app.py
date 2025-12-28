import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse

# Configuração com o nome da sua marca
st.set_page_config(page_title="DANGELLI Conselho e Estratégia", layout="centered")

# Título e Autoridade
st.title("🛡️ Diagnóstico de Prontidão 2026")
st.subheader("DANGELLI Conselho e Estratégia")
st.markdown("---")
st.write("Especialista com **8 anos de parceria com a Fundação Dom Cabral (FDC)**, auxiliando líderes na jornada de transformação e crescimento.")

with st.form("diagnostico"):
    st.write("### 1. Identificação do Líder")
    nome = st.text_input("Seu Nome Completo")
    empresa = st.text_input("Empresa e CNPJ")
    cargo = st.text_input("Função/Cargo")
    desafio = st.text_area("Qual seu maior desafio estratégico hoje?")
    
    st.markdown("---")
    st.write("### 2. Avaliação de Maturidade (Notas de 1 a 5)")
    n1 = st.slider("Processos (Metodologia FDC/MIT)", 1, 5, 3)
    n2 = st.slider("Presença Digital e Mercado", 1, 5, 3)
    n3 = st.slider("Uso de Inteligência Artificial", 1, 5, 3)
    n4 = st.slider("Cultura de Dados", 1, 5, 3)
    n5 = st.slider("Gestão de Pessoas e Cultura", 1, 5, 3)
    
    enviado = st.form_submit_button("GERAR MEU DIAGNÓSTICO")

if enviado:
    df = pd.DataFrame({
        'Área': ["Processos", "Digital", "IA", "Dados", "Gestão"],
        'Nota': [n1, n2, n3, n4, n5]
    })
    fig = px.line_polar(df, r='Nota', theta='Área', line_close=True, range_r=[0,5])
    fig.update_traces(fill='toself', line_color='#1f77b4')
    st.plotly_chart(fig)

    # Link do WhatsApp - Formato validado sem o 9
    numero_valido = "553183984001"
    
    texto = f"Ola David! Fiz o Diagnostico DANGELLI.\n\nNome: {nome}\nEmpresa: {empresa}\nDesafio: {desafio}\n\nNotas:\n- Processos: {n1}\n- Digital: {n2}\n- IA: {n3}\n- Dados: {n4}\n- Gestao: {n5}"
    
    texto_codificado = urllib.parse.quote(texto)
    link_final = f"https://wa.me/{numero_valido}?text={texto_codificado}"

    st.success("Diagnóstico concluído com sucesso!")
    st.link_button("✅ ENVIAR RESULTADO PARA ANÁLISE", link_final)
