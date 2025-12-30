import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse

st.set_page_config(page_title="DANGELLI - Diagnóstico Estratégico", layout="centered")

# Estilo Customizado
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #00c853; color: white; border-radius: 10px; font-weight: bold; width: 100%; }
    h1, h2, h3 { color: #d4af37; }
    .section-box { background-color: #1e2130; padding: 15px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Diagnóstico de Prontidão Estratégica")
st.subheader("DANGELLI Serviços - Conselho e Estratégia")
st.write("Especialista com **8 anos de parceria com a Fundação Dom Cabral (FDC)**.")
st.write("---")

with st.form("diagnostico_profundo"):
    st.write("### 1. Identificação")
    nome = st.text_input("Seu Nome Completo")
    empresa = st.text_input("Sua Empresa")
    desafio = st.text_area("Qual seu maior desafio estratégico hoje?")

    # SEÇÃO GOVERNANÇA
    st.markdown('<div class="section-box">### 🏛️ Governança e Sucessão</div>', unsafe_allow_html=True)
    g1 = st.slider("A empresa possui Tag Along ou acordos de sócios claros?", 1, 5, 1)
    g2 = st.slider("Existe um plano de sucessão ou conselho consultivo?", 1, 5, 1)
    
    # SEÇÃO TRIBUTÁRIA E CENÁRIO
    st.markdown('<div class="section-box">### ⚖️ Cenário e Reforma Tributária</div>', unsafe_allow_html=True)
    t1 = st.slider("Preparação para os impactos da Reforma Tributária?", 1, 5, 1)
    t2 = st.slider("Planejamento tributário e eficiência financeira?", 1, 5, 1)
    
    # SEÇÃO TECNOLOGIA E IA
    st.markdown('<div class="section-box">### 🤖 IA e Transformação Digital</div>', unsafe_allow_html=True)
    i1 = st.slider("Uso de Inteligência Artificial nos processos atuais?", 1, 5, 1)
    i2 = st.slider("Presença digital e automação de marketing/vendas?", 1, 5, 1)

    # SEÇÃO PESSOAS E CULTURA
    st.markdown('<div class="section-box">### 👥 Pessoas e Cultura de Dados</div>', unsafe_allow_html=True)
    p1 = st.slider("Cultura organizacional baseada em dados e métricas?", 1, 5, 1)
    p2 = st.slider("Engajamento e retenção de talentos-chave?", 1, 5, 1)

    enviado = st.form_submit_button("GERAR DIAGNÓSTICO COMPLETO")

if enviado:
    if not nome or not empresa:
        st.error("Por favor, preencha os dados de identificação.")
    else:
        # Médias para o Gráfico
        media_gov = (g1 + g2) / 2
        media_trib = (t1 + t2) / 2
        media_ia = (i1 + i2) / 2
        media_rh = (p1 + p2) / 2
        geral = (media_gov + media_trib + media_ia + media_rh) / 4

        df = pd.DataFrame({
            'Área': ["Governança", "Tributário", "IA/Digital", "Pessoas"],
            'Nota': [media_gov, media_trib, media_ia, media_rh]
        })
        fig = px.line_polar(df, r='Nota', theta='Área', line_close=True, range_r=[0,5])
        st.plotly_chart(fig)

        # Parecer baseado na média geral
        if geral <= 2.9:
            status, msg = "PRIMEIRO NÍVEL", "Risco de sustentabilidade. Foco urgente em estruturação."
        elif geral <= 4.5:
            status, msg = "NÍVEL MÉDIO", "Maturidade existente, mas com gargalos de escala para 2026."
        else:
            status, msg = "EXCELÊNCIA", "Prontidão para vanguarda e oceanos azuis."

        st.success(f"**Nível: {status}** - {msg}")

        # WhatsApp Detalhado
        mensagem = (
            f"Olá David, sou {nome} da {empresa}.\n"
            f"Fiz o diagnóstico completo DANGELLI.\n"
            f"📊 MÉDIAS:\n- Gov: {media_gov}\n- Trib: {media_trib}\n- IA: {media_ia}\n- RH: {media_rh}\n"
            f"🎯 DESAFIO: {desafio}"
        )
        
        texto_url = urllib.parse.quote(mensagem)
        link = f"https://api.whatsapp.com/send?phone=5531983984001&text={texto_url}"
        st.link_button("🚀 ENVIAR PARECER PARA ANÁLISE DO DAVID", link)
