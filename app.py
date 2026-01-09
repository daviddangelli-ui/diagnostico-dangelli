import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Diagnóstico de Maturidade DANGELLI", layout="wide")

# Título
st.title("🏛️ Diagnóstico de Maturidade: Reforma Tributária vs. Governança")

# --- FORMULÁRIO ---
with st.form("diagnostico_form"):
    st.subheader("📋 Identificação")
    nome = st.text_input("Seu Nome Completo:")
    empresa = st.text_input("Nome da sua Empresa:")
    
    st.divider()
    st.subheader("📊 Responda às 21 questões fundamentais (Nível 1 a 5):")
    
    # Pilares (VALOR INICIAL 1)
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
    
    submitted = st.form_submit_button("📊 GERAR MEU GRÁFICO")

if submitted:
    if nome and empresa:
        m_gov = (q1+q2+q3+q4+q5+q6)/6
        m_blind = (q7+q8+q9+q10+q11)/5
        m_estrat = (q12+q13+q14+q15+q16)/5
        m_reforma = (q17+q18+q19+q20+q21)/5
        
        # Gráfico
        df_radar = pd.DataFrame({
            'Pilar': ['Governança', 'Blindagem', 'Estratégia', 'Reforma 2026'],
            'Nível': [m_gov, m_blind, m_estrat, m_reforma]
        })
        fig = px.line_polar(df_radar, r='Nível', theta='Pilar', line_close=True, range_r=[0,5])
        st.plotly_chart(fig)
        
        # --- BLOCO FINAL ---
        st.warning("⚠️ **ÚLTIMO PASSO OBRIGATÓRIO:**")
        
        # Link do WhatsApp formatado sem caracteres especiais perigosos
        msg = f"NOVO DIAGNÓSTICO DANGELLI%0A👤 Nome: {nome}%0A🏢 Empresa: {empresa}%0A%0A📊 Médias:%0AGov: {m_gov:.1f}%0ABlind: {m_blind:.1f}%0AEstrat: {m_estrat:.1f}%0ARef: {m_reforma:.1f}%0A%0A📝 Respostas: Q1:{q1}, Q2:{q2}, Q3:{q3}, Q4:{q4}, Q5:{q5}, Q6:{q6}, Q7:{q7}, Q8:{q8}, Q9:{q9}, Q10:{q10}, Q11:{q11}, Q12:{q12}, Q13:{q13}, Q14:{q14}, Q15:{q15}, Q16:{q16}, Q17:{q17}, Q18:{q18}, Q19:{q19}, Q20:{q20}, Q21:{q21}"
        link_final = f"https://wa.me/5531983984001?text={msg}"
        
        # Botão link padrão (seguro contra TypeError)
        st.link_button("🚀 CLIQUE AQUI PARA CONCLUIR E ENVIAR DIAGNÓSTICO", link_final, use_container_width=True)
        
        st.divider()
        st.success(f"Análise processada para {nome}!")
        st.info(f"""
        **O que acontece após você clicar no botão de envio acima?**
        1. Seus dados chegam à nossa central técnica para análise detalhada da **{empresa}**.
        2. Um consultor da **DANGELLI** entrará em contato para sua devolutiva.
        3. Você receberá o convite para nossa **Master Class sobre Governança**.
        """)
    else:
        st.error("Por favor, preencha o Nome e a Empresa no topo.")
