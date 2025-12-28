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
    # Exibir o gráfico
    st.plotly_chart(fig)

    # Configuração do WhatsApp
    meu_whats = "5531983984001"
    
    # Criar a mensagem que você vai receber
    texto_whats = f"Olá David! Acabei de fazer o Diagnóstico 2026.\n\nMeu Nome: {nome}\nEmpresa: {empresa}\n\nResultados:\n- Processos: {notas[0]}\n- Digital: {notas[1]}\n- IA: {notas[2]}\n- Dados: {notas[3]}\n- Gestão: {notas[4]}"
    
    # Codificar a mensagem para o link funcionar sem erros
    import urllib.parse
    mensagem_url = urllib.parse.quote(texto_whats)
    link_final = f"https://wa.me/{meu_whats}?text={mensagem_url}"

    st.markdown("---")
    st.subheader("Próximo Passo:")
    st.write("Para receber sua análise detalhada e garantir sua vaga na Masterclass, clique no botão abaixo:")
    
    # O BOTÃO QUE ESTAVA FALTANDO OU ERRADO
    st.link_button("✅ CONFIRMAR VAGA NA MASTERCLASS", link_final)
