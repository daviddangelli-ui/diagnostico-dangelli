import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Diagnóstico de Maturidade DANGELLI", layout="wide")

# --- FUNÇÃO DE APOIO: FINALIZAÇÃO (WHATSAPP) ---
def oferecer_proximos_passos(nome, empresa, resumo_msg):
    st.warning("⚠️ **ÚLTIMO PASSO OBRIGATÓRIO:**")
    link_final = f"https://wa.me/5531983984001?text={resumo_msg}"
    st.link_button("🚀 CLIQUE AQUI PARA CONCLUIR E ENVIAR DIAGNÓSTICO", link_final, use_container_width=True)
    st.divider()
    st.success(f"Análise processada para {nome}!")
    st.info(f"Obrigado! Seus dados foram enviados para a central técnica da DANGELLI.")

# --- OPÇÃO 1: MATURIDADE DANGELLI ORIGINAL (21 QUESTÕES) ---
def diagnostico_original_dangelli():
    st.header("🏛️ Diagnóstico de Maturidade: Reforma Tributária vs. Governança")
    with st.form("diagnostico_form"):
        st.subheader("📋 Identificação")
        nome = st.text_input("Seu Nome Completo:")
        empresa = st.text_input("Nome da sua Empresa:")
        st.divider()
        st.subheader("📊 Avaliação de Maturidade (Nível 1 a 5):")
        st.info("Pilar 1: Governança e Longevidade")
        q1 = st.slider("1. Existe um Acordo de Sócios formalizado?", 1, 5, 1)
        q2 = st.slider("2. As reuniões de diretoria são formalizadas em atas?", 1, 5, 1)
        q3 = st.slider("3. Há um plano de sucessão definido?", 1, 5, 1)
        q4 = st.slider("4. Patrimônio pessoal separado do da empresa?", 1, 5, 1)
        q5 = st.slider("5. Existe conselho consultivo independente?", 1, 5, 1)
        q6 = st.slider("6. O Código de Ética é conhecido por todos?", 1, 5, 1)
        st.info("Pilar 2: Blindagem e Proteção Patrimonial")
        q7 = st.slider("7. Possui holding patrimonial constituída?", 1, 5, 1)
        q8 = st.slider("8. Ativos protegidos contra riscos cíveis?", 1, 5, 1)
        q9 = st.slider("9. Há seguro D&O para diretores?", 1, 5, 1)
        q10 = st.slider("10. Estrutura de capital otimizada?", 1, 5, 1)
        q11 = st.slider("11. Cláusulas de impenhorabilidade nos bens?", 1, 5, 1)
        st.info("Pilar 3: Estratégia e Valuation")
        q12 = st.slider("12. Possui planejamento estratégico (5 anos)?", 1, 5, 1)
        q13 = st.slider("13. EBITDA monitorado mensalmente?", 1, 5, 1)
        q14 = st.slider("14. Fez Valuation nos últimos 2 anos?", 1, 5, 1)
        q15 = st.slider("15. Possui auditoria independente?", 1, 5, 1)
        q16 = st.slider("16. Processos internos mapeados?", 1, 5, 1)
        st.info("Pilar 4: Prontidão para a Reforma Tributária 2026")
        q17 = st.slider("17. Mapeou impacto do IBS/CBS no caixa?", 1, 5, 1)
        q18 = st.slider("18. Setor contábil treinado para IVA?", 1, 5, 1)
        q19 = st.slider("19. Estratégia para o Split Payment?", 1, 5, 1)
        q20 = st.slider("20. Cláusulas de revisão tributária em contratos?", 1, 5, 1)
        q21 = st.slider("21. Participa de comitês sobre a transição?", 1, 5, 1)
        submitted = st.form_submit_button("📊 GERAR GRÁFICO")
    if submitted:
        if nome and empresa:
            m_gov = (q1+q2+q3+q4+q5+q6)/6
            m_blind = (q7+q8+q9+q10+q11)/5
            m_estrat = (q12+q13+q14+q15+q16)/5
            m_reforma = (q17+q18+q19+q20+q21)/5
            df_radar = pd.DataFrame({'Pilar': ['Governança', 'Blindagem', 'Estratégia', 'Reforma 2026'], 'Nível': [m_gov, m_blind, m_estrat, m_reforma]})
            st.plotly_chart(px.line_polar(df_radar, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
            resumo_wa = f"MATURIDADE ORIGINAL%0A👤 Nome: {nome}%0A🏢 Empresa: {empresa}%0A📊 Médias: Gov:{m_gov:.1f}, Blind:{m_blind:.1f}, Est:{m_estrat:.1f}, Ref:{m_reforma:.1f}"
            oferecer_proximos_passos(nome, empresa, resumo_wa)

# --- OPÇÃO 2: GOVERNANÇA, ESTRATÉGIA E VALUATION ---
def diagnostico_valuation_ma():
    st.header("📈 Diagnóstico: Governança, Estratégia e Valuation")
    nome = st.text_input("Nome Completo:")
    empresa = st.text_input("Empresa:")
    
    tabs = st.tabs(["🏛️ Governança", "🛡️ Proteção", "🎯 Estratégia", "💰 Valuation"])
    
    with tabs[0]:
        st.subheader("Governança e Longevidade")
        g1 = st.slider("Existe um Acordo de Sócios formalizado?", 1, 5, 1)
        g2 = st.slider("As reuniões de diretoria são formalizadas em atas?", 1, 5, 1)
        g3 = st.slider("Há um plano de sucessão definido e programa de formação?", 1, 5, 1)
        g4 = st.slider("Existe Conselho Consultivo e Conselho de Família?", 1, 5, 1)
        g5 = st.slider("Código de Ética formalizado e assinado por
