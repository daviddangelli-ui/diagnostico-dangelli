import streamlit as st
import urllib.parse
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="DANGELLI - Diagnóstico de Maturidade", layout="centered")

# ESTILIZAÇÃO CSS (Efeito Blur e Botão)
st.markdown("""
    <style>
    .blur-container { filter: blur(8px); -webkit-filter: blur(8px); pointer-events: none; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #25D366; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Diagnóstico de Maturidade: Reforma Tributária vs. Governança")

# 1. IDENTIFICAÇÃO
with st.container():
    nome = st.text_input("Seu Nome Completo:")
    empresa = st.text_input("Nome da sua Empresa:")

st.divider()

# 2. TODAS AS PERGUNTAS DA VERSÃO ANTERIOR
st.subheader("Responda sobre a situação atual da sua empresa:")

def get_val(text): return int(text.split('(')[-1].split(')')[0])

# GOVERNANÇA (Expandido)
st.markdown("### 🏛️ Governança Corporativa")
g1 = st.radio("Possui Acordo de Sócios/Quotas?", ["Não possui (0)", "Em discussão (5)", "Sim, registrado (10)"])
g2 = st.radio("Existe separação entre gestão e propriedade?", ["Não (0)", "Parcialmente (5)", "Sim, total (10)"])
g3 = st.radio("Há reuniões de conselho ou diretoria mensais?", ["Não (0)", "Eventuais (5)", "Sim, sistemáticas (10)"])

# BLINDAGEM (Expandido)
st.markdown("### 🛡️ Blindagem Patrimonial")
b1 = st.radio("O patrimônio pessoal está em nome da PJ operacional?", ["Sim (0)", "Parte dele (5)", "Não, está segregado (10)"])
b2 = st.radio("Utiliza estruturas de Holding Patrimonial?", ["Não (0)", "Em estudo (5)", "Sim, operacional (10)"])
b3 = st.radio("Possui seguro de responsabilidade civil para diretores?", ["Não (0)", "Em cotação (5)", "Sim (10)"])

# ESTRATÉGIA (Expandido)
st.markdown("### 📈 Estratégia Tributária")
e1 = st.radio("Realiza Planejamento Tributário preventivo?", ["Não (0)", "Às vezes (5)", "Sim, anualmente (10)"])
e2 = st.radio("Aproveita todos os benefícios fiscais do setor?", ["Não sei (0)", "Alguns (5)", "Sim, mapeados (10)"])

# REFORMA (Expandido)
st.markdown("### ⚡ Reforma Tributária")
r1 = st.radio("Já quantificou o aumento de carga com CBS/IBS?", ["Não (0)", "Previsão superficial (5)", "Sim, estudo completo (10)"])
r2 = st.radio("Seu sistema ERP está pronto para o split payment?", ["Não (0)", "Em atualização (5)", "Sim (10)"])

# CÁLCULOS DAS MÉDIAS
m_gov = (get_val(g1) + get_val(g2) + get_val(g3)) / 3
m_bli = (get_val(b1) + get_val(b2) + get_val(b3)) / 3
m_est = (get_val(e1) + get_val(e2)) / 2
m_ref = (get_val(r1) + get_val(r2)) / 2

if st.button("ANALISAR MATURIDADE DO NEGÓCIO"):
    if not nome or not empresa:
        st.error("Por favor, preencha nome e empresa.")
    else:
        # SALVAR NO GOOGLE SHEETS
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            novo_lead = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "NOME": nome,
                "EMPRESA": empresa,
                "GOVERNANÇA": round(m_gov, 1),
                "BLINDAGEM": round(m_bli, 1),
                "ESTRATÉGIA": round(m_est, 1),
                "REFORMA": round(m_ref, 1)
            }])
            conn.create(data=novo_lead)
        except Exception as e:
            print(f"Erro técnico: {e}")

        # GRÁFICO DE RADAR
        categories = ['Governança', 'Blindagem', 'Estratégia', 'Reforma']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[m_gov, m_bli, m_est, m_ref], theta=categories, fill='toself', line_color='#1f77b4'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=False)

        st.subheader(f"Diagnóstico de {nome}")
        st.markdown('<div class="blur-container">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # WHATSAPP COM DETALHES DO RESULTADO
        whatsapp_real = "5531983984001"
        msg = (f"Olá! Acabei de realizar o Diagnóstico DANGELLI.\n\n"
               f"*Empresa:* {empresa}\n"
               f"*Resultados:*\n"
               f"- Governança: {m_gov:.1f}/10\n"
               f"- Blindagem: {m_bli:.1f}/10\n"
               f"- Estratégia: {m_est:.1f}/10\n"
               f"- Reforma: {m_ref:.1f}/10\n\n"
               f"Quero liberar minha análise detalhada.")
        
        link_wa = f"https://wa.me/{whatsapp_real}?text={urllib.parse.quote(msg)}"
        st.markdown(f'<a href="{link_wa}" target="_blank"><button>🔓 LIBERAR ANÁLISE COMPLETA</button></a>', unsafe_allow_html=True)
