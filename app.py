import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Diagnóstico de Maturidade DANGELLI", layout="wide")

# Título e Descrição
st.title("🏛️ Diagnóstico de Maturidade: Reforma Tributária vs. Governança")
st.markdown("""
Este diagnóstico avalia a prontidão da sua empresa para os desafios de 2026 e sua solidez estrutural.
**Responda com sinceridade para obter um raio-x preciso.**
""")

# --- 21 PERGUNTAS MANTIDAS INTEGRALMENTE ---
with st.form("diagnostico_form"):
    st.subheader("📊 Responda às 21 questões fundamentais:")
    
    # Pilares e Perguntas (Mantendo sua estrutura exata)
    st.info("Pilar 1: Governança e Longevidade")
    q1 = st.slider("1. Existe um Acordo de Sócios formalizado e atualizado?", 1, 5, 1)
    q2 = st.slider("2. As reuniões de diretoria são formalizadas em atas?", 1, 5, 1)
    q3 = st.slider("3. Há um plano de sucessão definido para os cargos-chave?", 1, 5, 1)
    q4 = st.slider("4. O patrimônio pessoal dos sócios está separado do patrimônio da empresa?", 1, 5, 1)
    q5 = st.slider("5. Existe um conselho consultivo ou diretoria independente?", 1, 5, 1)
    q6 = st.slider("6. O Código de Ética e Conduta é conhecido por todos?", 1, 5, 1)
    
    st.info("Pilar 2: Blindagem e Proteção Patrimonial")
    q7 = st.slider("7. A empresa possui holding patrimonial constituída?", 1, 5, 1)
    q8 = st.slider("8. Os ativos operacionais estão protegidos contra riscos cíveis/trabalhistas?", 1, 5, 1)
    q9 = st.slider("9. Há seguro de responsabilidade para diretores (D&O)?", 1, 5, 1)
    q10 = st.slider("10. A estrutura de capital é otimizada para proteção de ativos?", 1, 5, 1)
    q11 = st.slider("11. Existem cláusulas de inalienabilidade e impenhorabilidade nos bens principais?", 1, 5, 1)
    
    st.info("Pilar 3: Estratégia e Valuation")
    q12 = st.slider("12. A empresa possui um planejamento estratégico para os próximos 5 anos?", 1, 5, 1)
    q13 = st.slider("13. O EBITDA é monitorado mensalmente com metas claras?", 1, 5, 1)
    q14 = st.slider("14. Já foi realizado um estudo de Valuation profissional nos últimos 2 anos?", 1, 5, 1)
    q15 = st.slider("15. A empresa possui auditoria externa independente?", 1, 5, 1)
    q16 = st.slider("16. Os processos internos são mapeados e certificados?", 1, 5, 1)
    
    st.info("Pilar 4: Prontidão para a Reforma Tributária 2026")
    q17 = st.slider("17. A empresa já mapeou o impacto do IBS/CBS no seu fluxo de caixa?", 1, 5, 1)
    q18 = st.slider("18. O setor contábil já está treinado para o novo modelo de créditos do IVA?", 1, 5, 1)
    q19 = st.slider("19. Existe estratégia para lidar com o Split Payment (retenção automática)?", 1, 5, 1)
    q20 = st.slider("20. Os contratos de longo prazo possuem cláusulas de revisão tributária?", 1, 5, 1)
    q21 = st.slider("21. A empresa participa de comitês ou consultorias sobre a transição?", 1, 5, 1)
    
    # Dados do Lead
    st.divider()
    nome = st.text_input("Seu Nome Completo:")
    empresa = st.text_input("Nome da sua Empresa:")
    
    submitted = st.form_submit_button("🚀 LIBERAR ANÁLISE COMPLETA")

if submitted:
    if nome and empresa:
        # Cálculos de Médias
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
        
        # --- NOVO BLOCO DE MENSAGEM FINAL PARA O CLIENTE ---
        st.success(f"✅ **Análise concluída com sucesso, {nome}!**")
        st.info(f"""
        **Próximos Passos:**
        1. Seus dados foram enviados para nossa central técnica.
        2. A equipe **DANGELLI** entrará em contato em breve para apresentar o detalhamento do seu diagnóstico.
        3. Você receberá também um convite exclusivo para nossa **Master Class sobre Governança e Reforma Tributária**.
        
        Aguarde nosso contato via WhatsApp ou E-mail.
        """)
        
        # Mensagem para o WhatsApp (Invisível no site, mas gera o link)
        texto_whats = f"Diagnóstico DANGELLI: {nome} (Empresa: {empresa}) - Médias: Gov: {m_gov:.1f}, Blind: {m_blind:.1f}, Estrat: {m_estrat:.1f}, Ref: {m_reforma:.1f}. Detalhes: Q1:{q1}, Q2:{q2}, Q3:{q3}, Q4:{q4}, Q5:{q5}, Q6:{q6}, Q7:{q7}, Q8:{q8}, Q9:{q9}, Q10:{q10}, Q11:{q11}, Q12:{q12}, Q13:{q13}, Q14:{q14}, Q15:{q15}, Q16:{q16}, Q17:{q17}, Q18:{q18}, Q19:{q19}, Q20:{q20}, Q21:{q21}"
        link_whats = f"https://wa.me/5511974411211?text={texto_whats.replace(' ', '%20')}"
        
        st.markdown(f'[📲 CLIQUE AQUI PARA NOTIFICAR O CONSULTOR NO WHATSAPP]({link_whats})')
        
    else:
        st.error("Por favor, preencha seu nome e o nome da empresa antes de liberar a análise.")
