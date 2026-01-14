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

# --- OPÇÃO 1: MATURIDADE DANGELLI ORIGINAL (RESTAURADA - 21 QUESTÕES) ---
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

# --- OPÇÃO 2: GOVERNANÇA, ESTRATÉGIA E VALUATION (COMPLETO) ---
def diagnostico_valuation_ma():
    st.header("📈 Diagnóstico: Governança, Estratégia e Valuation")
    nome = st.text_input("Nome Completo:"); empresa = st.text_input("Empresa:")
    t1, t2, t3, t4 = st.tabs(["🏛️ Governança", "🛡️ Proteção", "🎯 Estratégia", "💰 Valuation"])
    with t1:
        g1 = st.slider("Existe um Acordo de Sócios formalizado?", 1, 5, 1)
        g2 = st.slider("As reuniões de diretoria são formalizadas em atas?", 1, 5, 1)
        g3 = st.slider("Plano de sucessão e programa de formação definido?", 1, 5, 1)
        g4 = st.slider("Existe Conselho Consultivo e de Família?", 1, 5, 1)
        g5 = st.slider("Código de Ética assinado por todos?", 1, 5, 1)
        g6 = st.slider("Regras de sucessão por morte e exclusão de sócios?", 1, 5, 1)
        g7 = st.slider("Política de distribuição de lucros definida?", 1, 5, 1)
    with t2:
        p1 = st.slider("Holding para o negócio e para cada acionista?", 1, 5, 1)
        p2 = st.slider("Acordo de Acionistas na Holding e núcleos familiares?", 1, 5, 1)
        p3 = st.slider("Ativos protegidos contra riscos cíveis?", 1, 5, 1)
        p4 = st.slider("Seguros contratados (D&O e Sucessão)?", 1, 5, 1)
    with t3:
        e1 = st.slider("Planejamento Estratégico para 5 anos?", 1, 5, 1)
        e2 = st.slider("Reuniões mensais de acompanhamento de KPIs?", 1, 5, 1)
        e3 = st.slider("Monitoramento mensal de DRE e EBITDA?", 1, 5, 1)
        e4 = st.slider("Ações alinhadas à Reforma Tributária?", 1, 5, 1)
    with t4:
        v1 = st.slider("Fez Valuation nos últimos 2 anos?", 1, 5, 1)
        v2 = st.slider("Modelagem financeira (BP) para o crescimento?", 1, 5, 1)
        v3 = st.slider("Visão clara da estratégia de Funding?", 1, 5, 1)
        v4 = st.slider("Preparação para venda ou assédio do mercado?", 1, 5, 1)
        v5 = st.slider("Domínio das variáveis chave geradoras de valor?", 1, 5, 1)
    if st.button("📊 ANALISAR VALUATION"):
        m_gov=(g1+g2+g3+g4+g5+g6+g7)/7; m_prot=(p1+p2+p3+p4)/4; m_est=(e1+e2+e3+e4)/4; m_val=(v1+v2+v3+v4+v5)/5
        df = pd.DataFrame({'Pilar':['Gov','Prot','Est','Val'],'Nível':[m_gov,m_prot,m_est,m_val]})
        st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
        oferecer_proximos_passos(nome, empresa, f"VALUATION%0ANome: {nome}")

# --- OPÇÃO 3: CORPORATIVO COMPLETO (TABELA MASTER) ---
def diagnostico_corporativo_completo():
    st.header("🏢 Diagnóstico Corporativo Profundo")
    nome = st.text_input("Executivo:"); emp = st.text_input("Empresa:")
    tabs = st.tabs(["Estratégia", "Financeiro", "Cadeia", "Governança", "Tecnologia"])
    with tabs[0]:
        c1 = st.slider("Agilidade para dois regimes simultâneos?", 1, 5, 1); c2 = st.slider("Perenidade sem benefícios fiscais?", 1, 5, 1)
        c3 = st.slider("Estrutura de decisão robusta?", 1, 5, 1); c4 = st.slider("Cultura de reação rápida?", 1, 5, 1)
        c5 = st.slider("Painel de cenários H1, H2, H3?", 1, 5, 1); c6 = st.slider("Orquestrador vs Obsoleto?", 1, 5, 1)
    with tabs[1]:
        f1 = st.slider("Previsão de impacto no Fluxo de Caixa?", 1, 5, 1); f2 = st.slider("Mapeamento de prejuízo em produtos?", 1, 5, 1)
        f3 = st.slider("Gestão preditiva de EBITDA?", 1, 5, 1); f4 = st.slider("Controle de Margem Líquida?", 1, 5, 1)
        f5 = st.slider("Orçamento para conformidade?", 1, 5, 1); f6 = st.slider("Integridade de dados em tempo real?", 1, 5, 1)
    with tabs[2]:
        v1 = st.slider("Defesa de preço por Proposta de Valor?", 1, 5, 1); v2 = st.slider("
