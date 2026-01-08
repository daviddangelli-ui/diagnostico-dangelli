import streamlit as st
import urllib.parse
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="DANGELLI - Diagnóstico de Maturidade", layout="centered")

# ESTILIZAÇÃO CSS
st.markdown("""
    <style>
    .blur-container { filter: blur(8px); -webkit-filter: blur(8px); }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #25D366; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Diagnóstico de Maturidade: Reforma Tributária vs. Governança")

# 1. IDENTIFICAÇÃO
with st.container():
    nome = st.text_input("Seu Nome Completo:")
    empresa = st.text_input("Nome da sua Empresa:")

st.divider()

# 2. PERGUNTAS DETALHADAS (SISTEMA DE PONTOS)
st.subheader("Responda com sinceridade sobre sua operação atual:")

# Bloco Governança
st.markdown("### 🏛️ Governança Corporativa")
g1 = st.radio("A empresa possui acordo de sócios ou conselho consultivo?", ["Não possui (0)", "Em fase de implementação (5)", "Sim, estruturado (10)"])
g2 = st.radio("Os processos de decisão são documentados e claros?", ["Informais (0)", "Parcialmente (5)", "Totalmente (10)"])

# Bloco Blindagem
st.markdown("### 🛡️ Blindagem Patrimonial")
b1 = st.radio("Existe separação clara entre patrimônio físico e da pessoa jurídica?", ["Nenhuma (0)", "Iniciando separação (5)", "Totalmente segregados (10)"])
b2 = st.radio("Possui estrutura de Holding ou proteção legal ativa?", ["Não (0)", "Em planejamento (5)", "Sim, operacional (10)"])

# Bloco Estratégia
st.markdown("### 📈 Estratégia Tributária")
e1 = st.radio("A empresa revisa créditos tributários anualmente?", ["Nunca (0)", "Às vezes (5)", "Sim, rotina anual (10)"])
e2 = st.radio("O regime tributário atual é o mais econômico comprovadamente?", ["Não sei (0)", "Acredito que sim (5)", "Sim, validado por auditoria (10)"])

# Bloco Reforma
st.markdown("### ⚡ Reforma Tributária")
r1 = st.radio("A empresa já mapeou o impacto do IBS/CBS no seu setor?", ["Não (0)", "Estudando o tema (5)", "Sim, impacto calculado (10)"])
r2 = st.radio("Existe plano de transição para o novo modelo de IVA?", ["Não (0)", "Em discussão (5)", "Sim, plano pronto (10)"])

# Função para extrair número do texto do radio
def get_val(text):
    return int(text.split('(')[-1].split(')')[0])

# CÁLCULO DAS MÉDIAS
score_gov = (get_val(g1) + get_val(g2)) / 2
score_bli = (get_val(b1) + get_val(b2)) / 2
score_est = (get_val(e1) + get_val(e2)) / 2
score_ref = (get_val(r1) + get_val(r2)) / 2

if st.button("ANALISAR MATURIDADE"):
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
                "GOVERNANÇA": score_gov,
                "BLINDAGEM": score_bli,
                "ESTRATÉGIA": score_est,
                "REFORMA": score_ref
            }])
            conn.create(data=novo_lead)
        except Exception as e:
            print(f"Erro no salvamento: {e}")

        # GRÁFICO DE RADAR
        categories = ['Governança', 'Blindagem', 'Estratégia', 'Reforma']
        values = [score_gov, score_bli, score_est, score_ref]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=values, theta=categories, fill='toself', line_color='#1f77b4'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=False)

        st.subheader("Seu Resultado Preliminar")
        st.markdown('<div class="blur-container">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.warning("⚠️ Resultado sob proteção. Clique abaixo para liberar a análise técnica completa.")
        
        # AJUSTE SEU WHATSAPP AQUI
        whatsapp_real = "5531983984001"
        texto_whats = f"Olá! Fiz o Diagnóstico DANGELLI.\nNome: {nome}\nEmpresa: {empresa}\n\nQuero liberar meu resultado completo."
        link_final = f"https://wa.me/{whatsapp_real}?text={urllib.parse.quote(texto_whats)}"
        
        st.markdown(f'<a href="{link_final}" target="_blank"><button>🔓 LIBERAR MEU RESULTADO AGORA</button></a>', unsafe_allow_html=True)
