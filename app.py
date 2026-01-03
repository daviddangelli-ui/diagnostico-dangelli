import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse
st.set_page_config(page_title="DANGELLI - Diagnóstico", layout="wide")
st.markdown("<h1>O que garante a perenidade de uma média empresa?</h1>", unsafe_allow_html=True)
with st.form("diagnostico_completo"):
  nome = st.text_input("Seu Nome Completo")
  empresa = st.text_input("Sua Empresa")
  st.markdown("### 🏛️ Nível 1: Governança") 
  g1 = st.select_slider("Acordo de Sócios formalizado?", options=["1", "2", "3", "4", "5"])
  st.markdown("### 🛡️ Nível 2: Blindagem Técnica") 
    b1 = st.select_slider("Cláusulas Tag Along e Shotgun?", options=["1", "2", "3", "4", "5"])
  st.markdown("### ⚖️ Reforma Tributária 2026") 
    t1 = st.select_slider("Simulação para 2026-2033?", options=["1", "2", "3", "4", "5"])
  enviado = st.form_submit_button("GERAR DIAGNÓSTICO")
if enviado:
    if not nome or not empresa:
        st.error("Preencha a identificação.")
    else:
        st.success("Diagnóstico concluído!")
        msg = f"Olá David! Sou {nome} da {empresa}. Concluí meu diagnóstico."
        url_wa = f"https://api.whatsapp.com/send?phone=5531983984001&text={urllib.parse.quote(msg)}"
        st.link_button("🚀 WHATSAPP DO DAVID", url_wa)
        st.link_button("🔗 MEU LINKEDIN", "https://www.linkedin.com/in/daviddangelli/")
