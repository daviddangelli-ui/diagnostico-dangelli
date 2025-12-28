import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da Página
st.set_page_config(page_title="DANGELLI Serviços - Diagnóstico Estratégico", layout="centered")

# Estilo Customizado (Executive Dark Mode)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #gold; color: black; border-radius: 10px; font-weight: bold; width: 100%; }
    h1, h2, h3 { color: #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho
st.title("🛡️ Diagnóstico de Prontidão 2026")
st.subheader("DANGELLI Serviços - Conselho e Estratégia")
st.write("---")

# Tela de Identificação
st.markdown("### 1. Identificação do Líder")
with st.form("id_form"):
    nome = st.text_input("Seu Nome Completo")
    empresa = st.text_input("Empresa e CNPJ")
    cargo = st.text_input("Função/Cargo")
    necessidade = st.text_area("Qual seu maior desafio estratégico hoje?")
    
    st.markdown("---")
    st.markdown("### 2. Avaliação de Maturidade")
    p1 = st.slider("Governança: Possuem Acordo de Sócios e Conselho ativo?", 0, 10, 5)
    p2 = st.slider("Reforma Tributária: Já possuem plano de transição para o IVA?", 0, 10, 5)
    p3 = st.slider("Estratégia: O planejamento atual considera cenários de microeconomia?", 0, 10, 5)
    p4 = st.slider("Valuation: A empresa está preparada para uma auditoria ou M&A?", 0, 10, 5)
    
    submit = st.form_submit_button("GERAR MEU DIAGNÓSTICO")

if submit:
    # Lógica do Gráfico de Radar
    df = pd.DataFrame(dict(
        r=[p1, p2, p3, p4],
        theta=['Governança','Reforma 2026','Estratégia','Valuation/M&A']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself', line_color='#d4af37')
    
    st.markdown("## Seu Scorecard Estratégico")
    st.plotly_chart(fig)
    meu_whats = "553183984001"
    # Parecer Consultivo (Baseado em David D'Angelli / FDC / MITx)
    st.markdown("### 🚩 Parecer Preliminar")
    if p2 < 6:
        st.warning(f"Atenção {nome}: A baixa prontidão para a Reforma 2026 representa um risco microeconômico de perda de margem direta.")
    else:
        st.success("Sua estrutura demonstra resiliência para as mudanças tributárias.")
        
    st.info("Para receber o relatório completo e o convite para a Masterclass, clique no botão abaixo.")

    # Botão WhatsApp
    # Substitua o número abaixo pelo seu número real (com 55 + DDD)
    meu_whats = "5511999999999" 
    texto_whats = f"Olá David, sou {nome} da empresa {empresa}. Fiz o diagnóstico e quero meu relatório completo e vaga na Masterclass."
    link_whats = f"https://wa.me/{meu_whats}?text={texto_whats.replace(' ', '%20')}"
    
    st.markdown(f'<a href="{link_whats}" target="_blank"><button style="width:100%; height:50px; background-color:#25D366; color:white; border:none; border-radius:10px; font-weight:bold; cursor:pointer;">✅ CONFIRMAR VAGA NA MASTERCLASS E RECEBER PDF</button></a>', unsafe_allow_html=True)
