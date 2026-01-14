import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Diagnóstico de Maturidade DANGELLI", layout="wide")

# --- FUNÇÃO DE APOIO: FINALIZAÇÃO (WHATSAPP) ---
def oferecer_proximos_passos(nome, empresa, resumo_msg):
    st.warning("⚠️ **ÚLTIMO PASSO OBRIGATÓRIO:**")
    link_final = f"https://wa.me/5531983984001?text={resumo_msg}"
    st.link_button("🚀 CLIQUE AQUI PARA CONCLUIR E ENVIAR DIAGNÓSTICO", link_final, use_container_width=True)
    st.divider()
    st.success(f"Análise processada para {nome}!")
    st.info(f"Obrigado! Seus dados foram enviados para a central técnica da DANGELLI para análise de Valuation e Governança.")

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
        q1 = st.slider("1. Existe um Acordo de Sócios formalizado?", 1, 5, 1); q2 = st.slider("2. As reuniões de diretoria são formalizadas em atas?", 1, 5, 1); q3 = st.slider("3. Há um plano de sucessão definido?", 1, 5, 1); q4 = st.slider("4. Patrimônio pessoal separado do da empresa?", 1, 5, 1); q5 = st.slider("5. Existe conselho consultivo independente?", 1, 5, 1); q6 = st.slider("6. O Código de Ética é conhecido por todos?", 1, 5, 1)
        st.info("Pilar 2: Blindagem e Proteção Patrimonial")
        q7 = st.slider("7. Possui holding patrimonial constituída?", 1, 5, 1); q8 = st.slider("8. Ativos protegidos contra riscos cíveis?", 1, 5, 1); q9 = st.slider("9. Há seguro D&O para diretores?", 1, 5, 1); q10 = st.slider("10. Estrutura de capital otimizada?", 1, 5, 1); q11 = st.slider("11. Cláusulas de impenhorabilidade nos bens?", 1, 5, 1)
        st.info("Pilar 3: Estratégia e Valuation")
        q12 = st.slider("12. Possui planejamento estratégico (5 anos)?", 1, 5, 1); q13 = st.slider("13. EBITDA monitorado mensalmente?", 1, 5, 1); q14 = st.slider("14. Fez Valuation nos últimos 2 anos?", 1, 5, 1); q15 = st.slider("15. Possui auditoria independente?", 1, 5, 1); q16 = st.slider("16. Processos internos mapeados?", 1, 5, 1)
        st.info("Pilar 4: Prontidão para a Reforma Tributária 2026")
        q17 = st.slider("17. Mapeou impacto do IBS/CBS no caixa?", 1, 5, 1); q18 = st.slider("18. Setor contábil treinado para IVA?", 1, 5, 1); q19 = st.slider("19. Estratégia para o Split Payment?", 1, 5, 1); q20 = st.slider("20. Cláusulas de revisão tributária em contratos?", 1, 5, 1); q21 = st.slider("21. Participa de comitês sobre a transição?", 1, 5, 1)
        submitted = st.form_submit_button("📊 GERAR GRÁFICO")
    if submitted:
        if nome and empresa:
            m_gov = (q1+q2+q3+q4+q5+q6)/6; m_blind = (q7+q8+q9+q10+q11)/5; m_estrat = (q12+q13+q14+q15+q16)/5; m_reforma = (q17+q18+q19+q20+q21)/5
            df_radar = pd.DataFrame({'Pilar': ['Governança', 'Blindagem', 'Estratégia', 'Reforma 2026'], 'Nível': [m_gov, m_blind, m_estrat, m_reforma]})
            fig = px.line_polar(df_radar, r='Nível', theta='Pilar', line_close=True, range_r=[0,5])
            st.plotly_chart(fig)
            resumo_wa = f"MATURIDADE ORIGINAL%0A👤 Nome: {nome}%0A🏢 Empresa: {empresa}%0A📊 Médias: Gov:{m_gov:.1f}, Blind:{m_blind:.1f}, Est:{m_estrat:.1f}, Ref:{m_reforma:.1f}"
            oferecer_proximos_passos(nome, empresa, resumo_wa)

# --- OPÇÃO 2: GOVERNANÇA, ESTRATÉGIA E VALUATION (NOVO!) ---
def diagnostico_valuation_ma():
    st.header("📈 Diagnóstico: Governança, Estratégia e Valuation")
    st.subheader("Prepare sua empresa para Crescimento, M&A ou Sucessão")
    
    with st.form("valuation_form"):
        col1, col2 = st.columns(2)
        with col1: nome = st.text_input("Seu Nome:")
        with col2: empresa = st.text_input("Sua Empresa:")
        
        tab1, tab2, tab3 = st.tabs(["🏛️ Governança", "🎯 Estratégia", "💰 Valuation & M&A"])
        
        with tab1:
            g1 = st.slider("Nível de profissionalização da gestão (Dono vs Processos)?", 1, 5, 1)
            g2 = st.slider("Transparência e qualidade das demonstrações financeiras?", 1, 5, 1)
            g3 = st.slider("Eficiência do Conselho e alinhamento entre sócios?", 1, 5, 1)
        with tab2:
            e1 = st.slider("Diferencial competitivo e barreiras de entrada no mercado?", 1, 5, 1)
            e2 = st.slider("Dependência da empresa em relação aos fundadores?", 1, 5, 1)
            e3 = st.slider("Escalabilidade e previsibilidade da receita?", 1, 5, 1)
        with tab3:
            v1 = st.slider("Conhecimento do valor real de mercado (Valuation)?", 1, 5, 1)
            v2 = st.slider("Prontidão para uma Due Diligence (Auditoria)?", 1, 5, 1)
            v3 = st.slider("Atratividade do EBITDA e controle de passivos ocultos?", 1, 5, 1)
            
        submitted = st.form_submit_button("📊 ANALISAR POTENCIAL DE VALUATION")

    if submitted:
        if nome and empresa:
            m_gov = (g1+g2+g3)/3; m_est = (e1+e2+e3)/3; m_val = (v1+v2+v3)/3
            df_radar = pd.DataFrame({'Pilar': ['Governança', 'Estratégia', 'Valuation'], 'Nível': [m_gov, m_est, m_val]})
            fig = px.line_polar(df_radar, r='Nível', theta='Pilar', line_close=True, range_r=[0,5])
            st.plotly_chart(fig)
            resumo_wa = f"GOV E VALUATION%0A👤 Nome: {nome}%0A🏢 Empresa: {empresa}%0A📊 Médias: Gov:{m_gov:.1f}, Estrat:{m_est:.1f}, Val:{m_val:.1f}"
            oferecer_proximos_passos(nome, empresa, resumo_wa)

# --- OPÇÃO 3: CORPORATIVO COMPLETO (BASEADO NA SUA TABELA) ---
def diagnostico_corporativo_completo():
    st.header("🏢 Diagnóstico Corporativo Profundo")
    nome = st.text_input("Executivo Responsável:"); empresa = st.text_input("Empresa Analisada:")
    tabs = st.tabs(["Org & Estratégia", "Financeiro & Tributário", "Cadeia & Comercial", "Governança & Sucessão", "Pessoas & Tecnologia"])
    with tabs[0]:
        c1 = st.slider("Agilidade para operar dois regimes tributários?", 1, 5, 1); c2 = st.slider("Perenidade do modelo (sem benefícios fiscais)?", 1, 5, 1); c3 = st.slider("Estrutura de decisão robusta?", 1, 5, 1); c4 = st.slider("Cultura de reação rápida?", 1, 5, 1); c5 = st.slider("Visão de painel de controle (Cenários)?", 1, 5, 1); c6 = st.slider("Orquestração da cadeia de valor?", 1, 5, 1)
    with tabs[1]:
        f1 = st.slider("Previsão de impacto no fluxo de caixa?", 1, 5, 1); f2 = st.slider("Mapeamento de prejuízo em produtos?", 1, 5, 1); f3 = st.slider("Gestão preditiva (EBITDA)?", 1, 5, 1); f4 = st.slider("Controle da Margem Líquida?", 1, 5, 1); f5 = st.slider("Orçamento para conformidade?", 1, 5, 1); f6 = st.slider("Integridade de dados (tempo real)?", 1, 5, 1)
    with tabs[2]:
        v1 = st.slider("Defesa de preço por Proposta de Valor?", 1, 5, 1); v2 = st.slider("Conhecimento da elasticidade de preço?", 1, 5, 1); v3 = st.slider("Prontidão físico vs digital?", 1, 5, 1); v4 = st.slider("Plano B para fornecedores tóxicos?", 1, 5, 1); v5 = st.slider("Eficiência logística real?", 1, 5, 1); v6 = st.slider("Proteção de margem em contratos?", 1, 5, 1)
    with tabs[3]:
        g1 = st.slider("Segregação patrimônio vs risco?", 1, 5, 1); g2 = st.slider("Acordo de sócios robusto?", 1, 5, 1); g3 = st.slider("Conselho técnico?", 1, 5, 1); g4 = st.slider("Conforto em assinar demonstrações?", 1, 5, 1); g5 = st.slider("Plano de sucessão técnica?", 1, 5, 1); g6 = st.slider("Transparência e Compliance?", 1, 5, 1)
    with tabs[4]:
        t1 = st.slider("Musculatura técnica (evitar burnout)?", 1, 5, 1); t2 = st.slider("Plano de retenção de talentos?", 1, 5, 1); t3 = st.slider("Plano de treinamento?", 1, 5, 1); t4 = st.slider("ERP como ativo estratégico?", 1, 5, 1); t5 = st.slider("Confiança nos dados cadastrais?", 1, 5, 1); t6 = st.slider("Automação vs Inchaço de folha?", 1, 5, 1)
    if st.button("🚀 GERAR DIAGNÓSTICO CORPORATIVO"):
        if nome and empresa:
            m_est = (c1+c2+c3+c4+c5+c6)/6; m_fin = (f1+f2+f3+f4+f5+f6)/6; m_com = (v1+v2+v3+v4+v5+v6)/6; m_gov = (g1+g2+g3+g4+g5+g6)/6; m_tec = (t1+t2+t3+t4+t5+t6)/6
            df_radar = pd.DataFrame({'Pilar': ['Estratégia', 'Financeiro', 'Comercial', 'Governança', 'Tecnologia'], 'Nível': [m_est, m_fin, m_com, m_gov, m_tec]})
            st.plotly_chart(px.line_polar(df_radar, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
            resumo_wa = f"CORPORATIVO%0A👤 De: {nome}%0A🏢 Cliente: {empresa}%0A📊 Médias: Est:{m_est:.1f}, Fin:{m_fin:.1f}, Com:{m_com:.1f}, Gov:{m_gov:.1f}, Tec:{m_tec:.1f}"
            oferecer_proximos_passos(nome, empresa, resumo_wa)

# --- NAVEGAÇÃO ---
st.sidebar.title("Menu DANGELLI")
opcao = st.sidebar.radio("Selecione o Diagnóstico:", ["1. Maturidade DANGELLI (Original)", "2. Governança, Estratégia e Valuation", "3. Corporativo Completo (Tabela Master)"])
st.sidebar.divider(); st.sidebar.write("v 2.5 - Business Excellence")

if opcao == "1. Maturidade DANGELLI (Original)": diagnostico_original_dangelli()
elif opcao == "2. Governança, Estratégia e Valuation": diagnostico_valuation_ma()
else: diagnostico_corporativo_completo()
