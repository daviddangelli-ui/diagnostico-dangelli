import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse

# Configuração da Página
st.set_page_config(page_title="DANGELLI - Diagnóstico Estratégico", layout="centered")

# Estilo Customizado
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #00c853; color: white; border-radius: 10px; font-weight: bold; width: 100%; }
    h1, h2, h3 { color: #d4af37; }
    .parecer-box { background-color: #1e2130; padding: 20px; border-radius: 10px; border-left: 5px solid #d4af37; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho
st.title("🛡️ Diagnóstico de Prontidão 2026")
st.subheader("DANGELLI Serviços - Conselho e Estratégia")
st.write("Especialista com **8 anos de parceria com a Fundação Dom Cabral (FDC)**.")
st.write("---")

# Formulário
with st.form("diagnostico"):
    st.write("### 1. Identificação do Líder")
    nome = st.text_input("Seu Nome Completo")
    empresa = st.text_input("Empresa")
    desafio = st.text_area("Qual seu maior desafio estratégico hoje?")
    
    st.write("### 2. Avaliação (Notas 1 a 5)")
    n1 = st.slider("Processos e Governança", 1, 5, 3)
    n2 = st.slider("Presença Digital", 1, 5, 3)
    n3 = st.slider("Uso de IA", 1, 5, 3)
    n4 = st.slider("Cultura de Dados", 1, 5, 3)
    n5 = st.slider("Gestão de Pessoas", 1, 5, 3)
    
    enviado = st.form_submit_button("GERAR MEU DIAGNÓSTICO E PARECER")

if enviado:
    media = (n1 + n2 + n3 + n4 + n5) / 5
    
    # Gráfico
    df = pd.DataFrame({
        'Área': ["Processos", "Digital", "IA", "Dados", "Gestão"],
        'Nota': [n1, n2, n3, n4, n5]
    })
    fig = px.line_polar(df, r='Nota', theta='Área', line_close=True, range_r=[0,5])
    st.plotly_chart(fig)

    # Lógica de Parecer sugerida por você
    if media <= 2.9:
        nivel = "PRIMEIRO NÍVEL (Iniciante)"
        parecer = "Atenção: Sua estrutura atual apresenta riscos de sustentabilidade para 2026. É necessário fortalecer processos básicos e governança antes de acelerar."
    elif media <= 4.9:
        nivel = "NÍVEL MÉDIO (Intermediário)"
        parecer = "Bom desempenho: Sua empresa já possui maturidade, mas ainda há 'gargalos' digitais ou de pessoas que impedem a escala plena rumo a 2026."
    else:
        nivel = "NÍVEL EXCELÊNCIA"
        parecer = "Parabéns: Você está no topo do mercado. O desafio agora é manter a vanguarda e utilizar a IA para criar novos oceanos azuis."

    # Exibição do Parecer na Tela
    st.markdown(f"""
        <div class="parecer-box">
            <h3>📋 Seu Parecer Preliminar</h3>
            <p><b>Status:</b> {nivel}</p>
            <p>{parecer}</p>
        </div>
    """, unsafe_allow_html=True)

    # Configuração do WhatsApp
    numero_faro = "5531983984001"
    resumo_notas = f"Proc:{n1}, Dig:{n2}, IA:{n3}, Dados:{n4}, Gestão:{n5} (Média: {media})"
    
    mensagem = (
        f"Olá David, sou {nome} da {empresa}.\n"
        f"Fiz o diagnóstico DANGELLI.\n"
        f"📊 Notas: {resumo_notas}\n"
        f"🎯 Desafio: {desafio}\n"
        f"Quero garantir minha vaga na aula geral."
    )
    
    texto_url = urllib.parse.quote(mensagem)
    link_final = f"https://api.whatsapp.com/send?phone={numero_faro}&text={texto_url}"

    st.link_button("✅ ENVIAR RESULTADOS PARA ANÁLISE DO DAVID", link_final)
