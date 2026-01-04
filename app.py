import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse
st.set_page_config(page_title="DANGELLI - Diagnóstico", layout="wide")

# ABERTURA IMPACTANTE (Baseada no seu Print 1)
st.markdown("""# O que garante a **perenidade** de uma média empresa em tempos de transformações profundas?""")
st.info("""Governança e Estratégia precisam estar completamente integradas sempre na moderna visão da perenidade dos negócios. Isso torna-se mais crítico agora com a chegada da Reforma Tributária.""")

with st.form("diagnostico_dangelli"):
    nome = st.text_input("Seu Nome Completo")
    empresa = st.text_input("Sua Empresa")

    # NÍVEL 1: GOVERNANÇA (Baseada no seu Print 2)
    st.markdown("### 🏛️ Nível 1: Fundamentos da Governança")
    g1 = st.select_slider("1. Sua empresa possui um Acordo de Sócios formalizado e atualizado?", options=["Inexistente", "2", "3", "4", "Pleno"])
    g2 = st.select_slider("2. Existe um plano de sucessão estruturado para posições-chave?", options=["Inexistente", "2", "3", "4", "Pleno"])
    g3 = st.select_slider("3. Há uma separação rigorosa entre contas pessoais (PF) e empresariais (PJ)?", options=["Inexistente", "2", "3", "4", "Pleno"])

    # NÍVEL 2: BLINDAGEM
    st.markdown("### 🛡️ Nível 2: Blindagem Técnica")
    b1 = st.select_slider("Cláusulas Tag Along e Shotgun implementadas?", options=["1", "2", "3", "4", "5"])

    # NÍVEL 3: REFORMA TRIBUTÁRIA (Suas novas perguntas de impacto)
    st.markdown("### ⚖️ REFORMA TRIBUTÁRIA 2026")
    st.write("A Reforma é um processo multidisciplinar que exige ajustes profundos. Avalie sua prontidão:")
    
    t1 = st.select_slider("Consciência: As alterações irão atingir diversas áreas além da fiscal?", options=["1", "2", "3", "4", "5"])
    t2 = st.select_slider("Estratégia: Ciente da necessidade de reavaliar cadeias de valor e precificação?", options=["1", "2", "3", "4", "5"])
    t3 = st.select_slider("Contratos: Ciente da necessidade de renegociar contratos de longo prazo?", options=["1", "2", "3", "4", "5"])
    t4 = st.select_slider("Propostas: Ciente da necessidade de reavaliar custos para garantir margens?", options=["1", "2", "3", "4", "5"])
    t5 = st.select_slider("Finanças: Impacto do Split Payment na Necessidade de Capital de Giro (NCG)?", options=["1", "2", "3", "4", "5"])
    t6 = st.select_slider("Tecnologia: Ciente da necessidade de adequação urgente de sistemas (ERP)?", options=["1", "2", "3", "4", "5"])

    enviado = st.form_submit_button("GERAR DIAGNÓSTICO E FALAR COM DAVID")

if enviado:
    if not nome or not empresa:
        st.error("Por favor, preencha seu nome e empresa para continuar.")
    else:
        st.success("Diagnóstico concluído! Clique abaixo para conversarmos.")
        msg = f"Olá David! Sou {nome} da {empresa}. Concluí meu diagnóstico de perenidade."
        url_wa = f"https://api.whatsapp.com/send?phone=5531983984001&text={urllib.parse.quote(msg)}"
        st.link_button("🚀 ENVIAR VIA WHATSAPP", url_wa)
        st.link_button("🔗 PERFIL LINKEDIN", "https://www.linkedin.com/in/daviddangelli/")
