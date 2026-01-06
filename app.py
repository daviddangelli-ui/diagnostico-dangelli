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
    .blur-container {
        filter: blur(8px);
        -webkit-filter: blur(8px);
        pointer-events: none;
        user-select: none;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #25D366;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Diagnóstico de Maturidade: Reforma Tributária vs. Governança")
st.write("Avalie os pilares da sua empresa e receba uma análise estratégica.")

# FORMULÁRIO DE IDENTIFICAÇÃO
with st.container():
    nome = st.text_input("Seu Nome Completo:")
    empresa = st.text_input("Nome da sua Empresa:")

st.divider()

# PERGUNTAS DO DIAGNÓSTICO
st.subheader("Avalie sua empresa (0 a 10)")

g_score = st.slider("Governança Corporativa", 0, 10, 5)
b_score = st.slider("Blindagem Patrimonial", 0, 10, 5)
e_score = st.slider("Estratégia Tributária", 0, 10, 5)
r_score = st.slider("Preparação para Reforma Tributária", 0, 10, 5)

# SALVAR SCORES NA MEMÓRIA
st.session_state['score_governanca'] = g_score
st.session_state['score_blindagem'] = b_score
st.session_state['score_estrategia'] = e_score
st.session_state['score_reforma'] = r_score

if st.button("ANALISAR MATURIDADE"):
    if not nome or not empresa:
        st.error("Por favor, preencha seu nome e o nome da empresa.")
    else:
        # 1. SALVAR NO GOOGLE SHEETS
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            novo_lead = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "NOME": nome,
                "EMPRESA": empresa,
                "GOVERNANÇA": g_score,
                "BLINDAGEM": b_score,
                "ESTRATÉGIA": e_score,
                "REFORMA": r_score
            }])
            conn.create(data=novo_lead)
        except Exception as e:
            print(f"Erro no salvamento: {e}")

        # 2. GERAR GRÁFICO DE RADAR COM EFEITO BLUR
        categories = ['Governança', 'Blindagem', 'Estratégia', 'Reforma']
        values = [g_score, b_score, e_score, r_score]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Maturidade Atual',
            line_color='#1f77b4'
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            showlegend=False,
            margin=dict(l=20, r=20, t=20, b=20)
        )

        st.subheader("Resultado do seu Diagnóstico")
        
        # APLICA O EFEITO DE DESFOQUE NO GRÁFICO
        st.markdown('<div class="blur-container">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 3. CHAMADA PARA AÇÃO (WHATSAPP)
        st.warning("⚠️ Seu resultado está disponível! Para visualizar a análise detalhada e remover o desfoque, clique no botão abaixo para falar com nossa equipe.")
        
        texto_whatsapp = f"Olá! Acabei de realizar o Diagnóstico de Maturidade.\n\n*Nome:* {nome}\n*Empresa:* {empresa}\n\nGostaria de liberar meu resultado completo e agendar uma análise."
        link_whatsapp = f"https://wa.me/SEU_NUMERO_AQUI?text={urllib.parse.quote(texto_whatsapp)}"
        
        st.markdown(f'<a href="{link_whatsapp}" target="_blank"><button style="width:100%; height:50px; background-color:#25D366; color:white; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">🔓 LIBERAR MEU RESULTADO AGORA</button></a>', unsafe_allow_html=True)
