import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Diagnóstico de Maturidade DANGELLI", layout="wide")

# --- FUNÇÃO DE APOIO: FINALIZAÇÃO, WHATSAPP E MASTERCLASS ---
def oferecer_proximos_passos(nome, empresa, resumo_msg):
    st.divider()
    st.subheader("🎓 Próximos Passos: Masterclass DANGELLI")
    st.write(f"Parabéns, **{nome}**! Você deu o primeiro passo para a perenidade da **{empresa}**.")
    st.info("💡 **DICA ESTRATÉGICA:** Não pare apenas no gráfico. Assista à nossa Masterclass exclusiva sobre Governança e a Nova Reforma Tributária.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("📺 ASSISTIR MASTERCLASS GRATUITA", "https://youtube.com/@dangelliconsultoria", use_container_width=True)
    with col2:
        # Link do WhatsApp com todas as notas detalhadas
        link_final = f"https://wa.me/5531983984001?text={resumo_msg}"
        st.link_button("🚀 ENVIAR RESULTADOS PARA ANÁLISE TÉCNICA", link_final, use_container_width=True)
    
    st.warning("⚠️ **ATENÇÃO:** Para validar seu diagnóstico e receber a análise, clique no botão acima para enviar os dados.")

# --- OPÇÃO 1: MATURIDADE DANGELLI ORIGINAL (21 QUESTÕES) ---
def diagnostico_original_dangelli():
    st.header("🏛️ Diagnóstico de Maturidade: Reforma Tributária vs. Governança")
    with st.form("diagnostico_form"):
        nome = st.text_input("Seu Nome Completo:")
        empresa = st.text_input("Nome da sua Empresa:")
        st.divider()
        st.subheader("📊 Avaliação (1 a 5):")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Governança**")
            q1 = st.slider("1. Acordo de Sócios?", 1, 5, 1)
            q2 = st.slider("2. Atas de Diretoria?", 1, 5, 1)
            q3 = st.slider("3. Plano de Sucessão?", 1, 5, 1)
            q4 = st.slider("4. Separação Patrimonial?", 1, 5, 1)
            q5 = st.slider("5. Conselho Independente?", 1, 5, 1)
            q6 = st.slider("6. Código de Ética?", 1, 5, 1)
            st.markdown("**Blindagem**")
            q7 = st.slider("7. Holding constituída?", 1, 5, 1)
            q8 = st.slider("8. Proteção Cível?", 1, 5, 1)
            q9 = st.slider("9. Seguro D&O?", 1, 5, 1)
            q10 = st.slider("10. Estrutura de Capital?", 1, 5, 1)
            q11 = st.slider("11. Impenhorabilidade?", 1, 5, 1)
        with c2:
            st.markdown("**Estratégia**")
            q12 = st.slider("12. Planejamento 5 anos?", 1, 5, 1)
            q13 = st.slider("13. EBITDA mensal?", 1, 5, 1)
            q14 = st.slider("14. Valuation 2 anos?", 1, 5, 1)
            q15 = st.slider("15. Auditoria?", 1, 5, 1)
            q16 = st.slider("16. Processos mapeados?", 1, 5, 1)
            st.markdown("**Reforma 2026**")
            q17 = st.slider("17. Impacto no Caixa?", 1, 5, 1)
            q18 = st.slider("18. Time treinado IVA?", 1, 5, 1)
            q19 = st.slider("19. Split Payment?", 1, 5, 1)
            q20 = st.slider("20. Revisão Contratos?", 1, 5, 1)
            q21 = st.slider("21. Comitês Transição?", 1, 5, 1)
        
        submitted = st.form_submit_button("🚀 GERAR DIAGNÓSTICO CORPORATIVO")
        
    if submitted:
        if nome and empresa:
            m_gov = (q1+q2+q3+q4+q5+q6)/6
            m_blind = (q7+q8+q9+q10+q11)/5
            m_estrat = (q12+q13+q14+q15+q16)/5
            m_reforma = (q17+q18+q19+q20+q21)/5
            df_radar = pd.DataFrame({'Pilar': ['Governança', 'Blindagem', 'Estratégia', 'Reforma 2026'], 'Nível': [m_gov, m_blind, m_estrat, m_reforma]})
            st.plotly_chart(px.line_polar(df_radar, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
            
            # Detalhamento para WhatsApp
            notas = f"Gov: {q1},{q2},{q3},{q4},{q5},{q6} | Blind: {q7},{q8},{q9},{q10},{q11} | Est: {q12},{q13},{q14},{q15},{q16} | Ref: {q17},{q18},{q19},{q20},{q21}"
            resumo_wa = f"DIAG_MATURIDADE%0A👤 Nome: {nome}%0A🏢 Empresa: {empresa}%0A📝 Notas Detalhadas: {notas}%0A📊 Médias: G:{m_gov:.1f}, B:{m_blind:.1f}, E:{m_estrat:.1f}, R:{m_reforma:.1f}"
            oferecer_proximos_passos(nome, empresa, resumo_wa)

# --- OPÇÃO 2: GOVERNANÇA, ESTRATÉGIA E VALUATION ---
def diagnostico_valuation_ma():
    st.header("📈 Diagnóstico: Governança, Estratégia e Valuation")
    nome = st.text_input("Nome Completo:"); empresa = st.text_input("Empresa:")
    t1, t2, t3, t4 = st.tabs(["🏛️ Governança", "🛡️ Proteção", "🎯 Estratégia", "💰 Valuation"])
    with t1:
        g1=st.slider("Acordo Sócios?",1,5,1); g2=st.slider("Atas?",1,5,1); g3=st.slider("Sucessão?",1,5,1); g4=st.slider("Conselhos?",1,5,1); g5=st.slider("Ética?",1,5,1); g6=st.slider("Regras Morte?",1,5,1); g7=st.slider("Lucros?",1,5,1)
    with t2:
        p1=st.slider("Holding?",1,5,1); p2=st.slider("Acordo Holding?",1,5,1); p3=st.slider("Proteção Cível?",1,5,1); p4=st.slider("Seguros?",1,5,1)
    with t3:
        e1=st.slider("Plano 5 anos?",1,5,1); e2=st.slider("KPIs?",1,5,1); e3=st.slider("DRE/EBITDA?",1,5,1); e4=st.slider("Reforma?",1,5,1)
    with t4:
        v1=st.slider("Valuation 2 anos?",1,5,1); v2=st.slider("Modelagem BP?",1,5,1); v3=st.slider("Funding?",1,5,1); v4=st.slider("M&A Ready?",1,5,1); v5=st.slider("Value Drivers?",1,5,1)
            
    if st.button("🚀 GERAR DIAGNÓSTICO CORPORATIVO"):
        if nome and empresa:
            m_gov=(g1+g2+g3+g4+g5+g6+g7)/7; m_val=(v1+v2+v3+v4+v5)/5
            df = pd.DataFrame({'P
