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
    st.info("💡 **DICA ESTRATÉGICA:** Assista à nossa Masterclass exclusiva sobre Governança e a Nova Reforma Tributária.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("📺 ASSISTIR MASTERCLASS GRATUITA", "https://youtube.com/@dangelliconsultoria", use_container_width=True)
    with col2:
        link_final = f"https://wa.me/5531983984001?text={resumo_msg}"
        st.link_button("🚀 ENVIAR RESULTADOS PARA ANÁLISE TÉCNICA", link_final, use_container_width=True)

# --- OPÇÃO 1: MATURIDADE DANGELLI ORIGINAL ---
def diagnostico_original_dangelli():
    st.header("🏛️ Diagnóstico de Maturidade: Reforma Tributária vs. Governança")
    with st.form("form_original"):
        nome = st.text_input("Seu Nome Completo:")
        empresa = st.text_input("Nome da sua Empresa:")
        st.divider()
        st.subheader("📊 Avaliação de Maturidade (Nível 1 a 5):")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Governança e Longevidade**")
            q1 = st.slider("Existe um Acordo de Sócios formalizado e atualizado?", 1, 5, 1)
            q2 = st.slider("As reuniões de diretoria são formalizadas em atas?", 1, 5, 1)
            q3 = st.slider("Há um plano de sucessão definido e comunicado?", 1, 5, 1)
            q4 = st.slider("O patrimônio pessoal está totalmente separado do patrimônio da empresa?", 1, 5, 1)
            q5 = st.slider("Existe um conselho consultivo ou diretoria independente?", 1, 5, 1)
            q6 = st.slider("O Código de Ética e Conduta é conhecido por todos?", 1, 5, 1)
            st.markdown("**Blindagem Patrimonial**")
            q7 = st.slider("A empresa possui holding patrimonial constituída?", 1, 5, 1)
            q8 = st.slider("Os ativos estão protegidos contra riscos cíveis e trabalhistas?", 1, 5, 1)
            q9 = st.slider("Há seguro D&O contratado para os diretores?", 1, 5, 1)
            q10 = st.slider("A estrutura de capital está otimizada (Dívida vs Patrimônio)?", 1, 5, 1)
            q11 = st.slider("Existem cláusulas de impenhorabilidade nos bens principais?", 1, 5, 1)
        with c2:
            st.markdown("**Estratégia e Valuation**")
            q12 = st.slider("A empresa possui planejamento estratégico formal para os próximos 5 anos?", 1, 5, 1)
            q13 = st.slider("O EBITDA é monitorado mensalmente com metas claras?", 1, 5, 1)
            q14 = st.slider("A empresa realizou Valuation profissional nos últimos 2 anos?", 1, 5, 1)
            q15 = st.slider("Existe auditoria independente ou interna periódica?", 1, 5, 1)
            q16 = st.slider("Os processos internos cruciais estão mapeados e padronizados?", 1, 5, 1)
            st.markdown("**Prontidão Reforma 2026**")
            q17 = st.slider("Foi feito o mapeamento do impacto do IBS/CBS no fluxo de caixa?", 1, 5, 1)
            q18 = st.slider("O setor contábil/fiscal já recebeu treinamento para o modelo de IVA?", 1, 5, 1)
            q19 = st.slider("Há estratégia definida para o funcionamento do Split Payment?", 1, 5, 1)
            q20 = st.slider("Os contratos atuais possuem cláusulas de revisão tributária?", 1, 5, 1)
            q21 = st.slider("A empresa participa de comitês ou fóruns sobre a transição tributária?", 1, 5, 1)
        
        if st.form_submit_button("🚀 GERAR DIAGNÓSTICO CORPORATIVO"):
            if nome and empresa:
                m_gov = (q1+q2+q3+q4+q5+q6)/6
                m_blind = (q7+q8+q9+q10+q11)/5
                m_est = (q12+q13+q14+q15+q16)/5
                m_ref = (q17+q18+q19+q20+q21)/5
                df = pd.DataFrame({'Pilar':['Gov','Prot','Est','Ref'],'Nível':[m_gov,m_blind,m_est,m_ref]})
                st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
                
                detalhe_notas = f"Gov: {q1},{q2},{q3},{q4},{q5},{q6} | Blind: {q7},{q8},{q9},{q10},{q11} | Est: {q12},{q13},{q14},{q15},{q16} | Ref: {q17},{q18},{q19},{q20},{q21}"
                msg = f"DIAG_MATURIDADE%0A👤 Nome: {nome}%0A🏢 Empresa: {empresa}%0A📊 Médias: Gov:{m_gov:.1f}, Blind:{m_blind:.1f}, Est:{m_est:.1f}, Ref:{m_ref:.1f}%0A📝 Notas: {detalhe_notas}"
                oferecer_proximos_passos(nome, empresa, msg)

# --- OPÇÃO 2: GOVERNANÇA, ESTRATÉGIA E VALUATION ---
def diagnostico_valuation_ma():
    st.header("📈 Diagnóstico: Governança, Estratégia e Valuation")
    nome = st.text_input("Executivo Responsável:"); empresa = st.text_input("Empresa:")
    t1, t2, t3, t4 = st.tabs(["🏛️ Governança", "🛡️ Proteção", "🎯 Estratégia", "💰 Valuation"])
    with t1:
        g1=st.slider("Existe um Acordo de Sócios formalizado e atualizado?",1,5,1); g2=st.slider("As reuniões de diretoria são formalizadas em atas?",1,5,1); g3=st.slider("Existe plano de sucessão e programa de formação de herdeiros?",1,5,1)
        g4=st.slider("A estrutura possui Conselho Consultivo e de Família?",1,5,1); g5=st.slider("Há Código de Ética assinado por todos os colaboradores?",1,5,1); g6=st.slider("Existem regras claras de sucessão por morte e exclusão?",1,5,1); g7=st.slider("A política de distribuição de lucros está claramente definida?",1,5,1)
    with t2:
        p1=st.slider("Existe Holding para proteção do negócio e dos acionistas?",1,5,1); p2=st.slider("O Acordo de Acionistas abrange a Holding e a família?",1,5,1); p3=st.slider("Os ativos estão protegidos contra riscos cíveis?",1,5,1); p4=st.slider("Há seguros contratados (D&O e Sucessão Patrimonial)?",1,5,1)
    with t3:
        e1=st.slider("Existe Planejamento Estratégico formal para os próximos 5 anos?",1,5,1); e2=st.slider("O acompanhamento de KPIs é realizado mensalmente?",1,5,1); e3=st.slider("Há monitoramento rigoroso de DRE e EBITDA?",1,5,1); e4=st.slider("As ações estratégicas estão alinhadas à Reforma Tributária?",1,5,1)
    with t4:
        v1=st.slider("A empresa realizou Valuation profissional nos últimos 2 anos?",1,5,1); v2=st.slider("Existe modelagem financeira para projeção de crescimento?",1,5,1); v3=st.slider("Há visão clara da estratégia de Funding para expansão?",1,5,1); v4=st.slider("Existe preparação para venda ou assédio do mercado (M&A)?",1,5,1); v5=st.slider("A diretoria domina as variáveis geradoras de valor (Value Drivers)?",1,5,1)
            
    if st.button("🚀 GERAR DIAGNÓSTICO CORPORATIVO"):
        if nome and empresa:
            m_gov=(g1+g2+g3+g4+g5+g6+g7)/7; m_prot=(p1+p2+p3+p4)/4; m_est=(e1+e2+e3+e4)/4; m_val=(v1+v2+v3+v4+v5)/5
            df = pd.DataFrame({'Pilar':['Gov','Prot','Est','Val'],'Nível':[m_gov, m_prot, m_est, m_val]})
            st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
            
            detalhe = f"Gov: {g1}-{g7} | Prot: {p1}-{p4} | Est: {e1}-{e4} | Val: {v1}-{v5}"
            msg = f"DIAG_VALUATION%0A👤 Nome: {nome}%0A🏢 Empresa: {empresa}%0A📊 Médias: G:{m_gov:.1f}, V:{m_val:.1f}%0A📝 Notas: {detalhe}"
            oferecer_proximos_passos(nome, empresa, msg)

# --- OPÇÃO 3: CORPORATIVO PROFUNDO ---
def diagnostico_corporativo_completo():
    st.header("🏢 Diagnóstico Corporativo Profundo")
    st.write("Auditoria de Competências Organizacionais, Áreas e Individuais (Nível 1 a 5)")
    nome = st.text_input("Consultor / Executivo:"); empresa = st.text_input("Empresa Cliente:")
    tabs = st.tabs(["Org & Estratégia", "Financeiro & Tributário", "Cadeia & Comercial", "Governança & Sucessão", "Pessoas & Tecnologia"])
    with tabs[0]:
        st.subheader("Competências Organizacionais e Estratégicas")
        c1=st.slider("Agilidade para operar dois regimes tributários simultâneos?",1,5,1); c2=st.slider("Perenidade do modelo de negócio (independência de benefícios fiscais)?",1,5,1); c3=st.slider("Estrutura de decisão robusta (evita paralisia por conflitos)?",1,5,1); c4=st.slider("Cultura de reação rápida e aprendizagem contínua?",1,5,1); c5=st.slider("Visão de painel de controle (cenários H1, H2, H3) vs Retrovisor?",1,5,1); c6=st.slider("Orquestração da cadeia de valor vs risco de obsolescência?",1,5,1)
    with tabs[1]:
        st.subheader("Eficiência Financeira e Fiscal")
        f1=st.slider("Previsão de impacto real no Fluxo de Caixa pós-reforma?",1,5,1); f2=st.slider("Mapeamento de margens e prejuízo oculto em produtos?",1,5,1); f3=st.slider("Gestão preditiva de EBITDA?",1,5,1); f4=st.slider("Controle rigoroso de Margem Líquida?",1,5,1); f5=st.slider("Orçamento para conformidade?",1,5,1); f6=st.slider("Integridade e confiabilidade de dados financeiros?",1,5,1)
    with tabs[2]:
        st.subheader("Cadeia de Valor e Comercial")
        v1=st.slider("Capacidade de defesa de preço por Proposta de Valor?",1,5,1); v2=st.slider("Conhe
