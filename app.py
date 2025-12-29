import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse

# Configuração da Página
st.set_page_config(page_title="DANGELLI Serviços - Diagnóstico Estratégico", layout="centered")

# Estilo Customizado (Executive Dark Mode)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #00c853; color: white; border-radius: 10px; font-weight: bold; width: 100%; }
    h1, h2, h3 { color: #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho
st.title("🛡️ Diagnóstico de Prontidão 2026")
st.subheader("DANGELLI Serviços - Conselho e Estratégia")
st.write("Especialista com **8 anos de parceria com a Fundação Dom Cabral (FDC)**, auxiliando líderes na jornada de transformação.")
st.write("---")

# Formulário de Identificação
with st.form("diagnostico"):
    st.write("### 1. Identificação do Líder")
    nome = st.text_input("Seu Nome Completo")
    empresa = st.text_input("Empresa e CNPJ")
    cargo = st.text_input("Função/Cargo")
    desafio = st.text_area("Qual seu maior desafio estratégico hoje?")
    
    st.write("### 2. Avaliação de Maturidade (Notas 1 a 5)")
    n1 = st.slider("Processos e Governança (FDC/MIT)", 1, 5, 3)
    n2 = st.slider("Presença Digital e Mercado", 1, 5, 3)
    n3 = st.slider("Uso de Inteligência Artificial", 1, 5, 3)
    n4 = st.slider("Cultura de Dados (BI/Analytics)", 1, 5, 3)
    n5 = st.slider("Gestão de Pessoas e Cultura", 1, 5, 3)
    
    enviado = st.form_submit_button("GERAR MEU DIAGNÓSTICO AGORA")

if enviado:
    # Lógica do Gráfico
    df = pd.DataFrame({
        'Área': ["Processos", "Digital", "IA", "Dados", "Gestão"],
        'Nota': [n1, n2, n3, n4, n5]
    })
    
    st.write("### Diagnóstico Concluído")
    fig = px.line_polar(df, r='Nota', theta='Área', line_close=True, range_r=[0,5])
    st.plotly_chart(fig)

    # CONFIGURAÇÃO AUTOMÁTICA DO WHATSAPP (COM O NÚMERO 9)
    # Este é o número que você validou como correto: 55 31 9 8398-4001
    numero_faro = "5531983984001"
    
    mensagem = (
        f"Olá David, sou {nome}, da empresa {empresa}. "
        f"Acabei de fazer o diagnóstico DANGELLI e quero garantir minha vaga "
        f"na aula geral sobre 2026 e receber meu parecer."
    )
    
    # Formatação para URL
    texto_url = urllib.parse.quote(mensagem)
    link_final = f"https://api.whatsapp.com/send?phone={numero_faro}&text={texto_url}"

    st.success("Tudo pronto! Agora envie seus dados para análise personalizada.")
    st.link_button("✅ ENVIAR PARA ANÁLISE NO WHATSAPP", link_final)
