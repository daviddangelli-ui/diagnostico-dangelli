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
        st.subheader("📊 Avaliação de Maturidade (1 a 5):")
        
        # Perguntas restauradas conforme histórico
        q1 = st.slider("1. Existe um Acordo de Sócios formalizado?", 1, 5, 1)
        q2 = st.slider("2. As reuniões de diretoria são formalizadas em atas?", 1, 5, 1)
        q3 = st.slider("3. Há um plano de sucessão definido?", 1, 5, 1)
        q4 = st.slider("4. Patrimônio pessoal separado do da empresa?", 1, 5, 1)
        q5 = st.slider("5. Existe conselho consultivo independente?", 1, 5, 1)
        q6 = st.slider("6. O Código de Ética é conhecido por todos?", 1, 5, 1)
        q7 = st.slider("7. Possui holding patrimonial constituída?", 1, 5, 1)
        q8 = st.slider("8. Ativos protegidos contra riscos cíveis?", 1, 5, 1)
        q9 = st.slider("9. Há seguro D&O para diretores?", 1, 5, 1)
        q10 = st.slider("10. Estrutura de capital otimizada?", 1, 5, 1)
        q11 = st.slider("11. Cláusulas de impenhorabilidade nos bens?", 1, 5, 1)
        q12 = st.slider("12. Planejamento estratégico (5 anos)?", 1, 5, 1)
        q13 = st.slider("13. EBITDA monitorado mensalmente?", 1, 5, 1)
        q14 = st.slider("14. Valuation nos últimos 2 anos?", 1, 5, 1)
        q15 = st.slider("15. Auditoria independente?", 1, 5, 1)
        q16 = st.slider("16. Processos mapeados?", 1, 5, 1)
        q17 = st.slider("17. Impacto do IBS/CBS no caixa?", 1, 5, 1)
        q18 = st.slider("18. Setor contábil treinado para IVA?", 1, 5, 1)
        q19 = st.slider("19. Estratégia para Split Payment?", 1, 5, 1)
        q20 = st.slider("20. Revisão tributária em contratos?", 1, 5, 1)
        q21 = st.slider("21. Comitês de transição?", 1, 5, 1)
        
        if st.form_submit_button("🚀 GERAR DIAGNÓSTICO CORPORATIVO"):
            m_gov = (q1+q2+q3+q4+q5+q6)/6
            m_blind = (q7+q8+q9+q10+q11)/5
            m_est = (q12+q13+q14+q15+q16)/5
            m_ref = (q17+q18+q19+q20+q21)/5
            df = pd.DataFrame({'Pilar':['Gov','Prot','Est','Ref'],'Nível':[m_gov,m_blind,m_est,m_ref]})
            st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
            resumo = f"DIAG_MATURIDADE%0ANome: {nome}%0ANotas: {q1},{q2},{q3},{q4},{q5},{q6},{q7},{q8},{q9},{q10},{q11},{q12},{q13},{q14},{q15},{q16},{q17},{q18},{q19},{q20},{q21}"
            oferecer_proximos_passos(nome, empresa, resumo)

# --- OPÇÃO 3: CORPORATIVO PROFUNDO (RESTAURADA CONFORME PRINT v2.1) ---
def diagnostico_corporativo_completo():
    st.header("🏢 Diagnóstico Corporativo Profundo")
    st.write("Auditoria de Competências Organizacionais, Áreas e Individuais (Nível 1 a 5)")
    
    nome = st.text_input("Consultor / Executivo Responsável:")
    empresa = st.text_input("Empresa Cliente:")
    
    tabs = st.tabs(["Org & Estratégia", "Financeiro & Tributário", "Cadeia & Comercial", "Governança & Sucessão", "Pessoas & Tecnologia"])
    
    with tabs[0]:
        st.subheader("Competências Organizacionais e Estratégicas")
        c1 = st.slider("Agilidade para operar dois regimes tributários simultâneos?", 1, 5, 1)
        c2 = st.slider("Perenidade do modelo de negócio (independência de benefícios fiscais)?", 1, 5, 1)
        c3 = st.slider("Estrutura de decisão robusta (evita paralisia por conflitos)?", 1, 5, 1)
        c4 = st.slider("Cultura de reação rápida e aprendizagem contínua?", 1, 5, 1)
        c5 = st.slider("Visão de painel de controle (cenários H1, H2, H3) vs Retrovisor?", 1, 5, 1)
        c6 = st.slider("Orquestração da cadeia de valor vs risco de obsolescência?", 1, 5, 1)
        
    with tabs[1]:
        st.subheader("Eficiência Financeira e Fiscal")
        f1 = st.slider("Previsão de impacto real no Fluxo de Caixa pós-reforma?", 1, 5, 1)
        f2 = st.slider("Mapeamento de margens e prejuízo oculto em produtos?", 1, 5, 1)
        f3 = st.slider("Gestão preditiva de EBITDA e geração de valor?", 1, 5, 1)
        f4 = st.slider("Controle rigoroso de Margem Líquida por canal?", 1, 5, 1)
        f5 = st.slider("Orçamento dedicado para custo de conformidade?", 1, 5, 1)
        f6 = st.slider("Integridade e confiabilidade de dados financeiros?", 1, 5, 1)
        
    with tabs[2]:
        st.subheader("Cadeia de Valor e Comercial")
        v1 = st.slider("Capacidade de defesa de preço por Proposta de Valor?", 1, 5, 1)
        v2 = st.slider("Conhecimento da elasticidade de preço do cliente final?", 1, 5, 1)
        v3 = st.slider("Equilíbrio competitivo entre canais físico vs digital?", 1, 5, 1)
        v4 = st.slider("Plano de contingência para fornecedores 'tóxicos'?", 1, 5, 1)
        v5 = st.slider("Eficiência logística e tributária na distribuição?", 1, 5, 1)
        v6 = st.slider("Revisão de contratos longos com cláusulas de reajuste?", 1, 5, 1)
        
    with tabs[3]:
        st.subheader("Governança e Continuidade")
        g1 = st.slider("Segregação clara entre patrimônio familiar e risco do negócio?", 1, 5, 1)
        g2 = st.slider("Acordo de sócios preparado para eventos de liquidez ou M&A?", 1, 5, 1)
        g3 = st.slider("Conselho com competência técnica para a nova economia?", 1, 5, 1)
        g4 = st.slider("Segurança jurídica na assinatura de balanços e impostos?", 1, 5, 1)
        g5 = st.slider("Sucessão técnica preparada para liderar em crises?", 1, 5, 1)
        g6 = st.slider("Compliance total e ausência de 'pontos cegos' operacionais?", 1, 5, 1)
        
    with tabs[4]:
        st.subheader("Capital Humano e Tecnologia")
        x1 = st.slider("Musculatura técnica do time contábil/fiscal interno?", 1, 5, 1)
        x2 = st.slider("Plano de retenção de talentos críticos durante a transição?", 1, 5, 1)
        x3 = st.slider("Treinamento de 're-alfabetização' tributária para vendas?", 1, 5, 1)
        x4 = st.slider("ERP atualizado e integrado como ativo estratégico?", 1, 5, 1)
        x5 = st.slider("Confiabilidade total nos dados cadastrais (clientes/itens)?", 1, 5, 1)
        x6 = st.slider("Automação de processos repetitivos vs trabalho manual?", 1, 5, 1)

    if st.button("🚀 GERAR DIAGNÓSTICO CORPORATIVO"):
        if nome and empresa:
            m_est=(c1+c2+c3+c4+c5+c6)/6
            m_fin=(f1+f2+f3+f4+f5+f6)/6
            m_cad=(v1+v2+v3+v4+v5+v6)/6
            m_gov=(g1+g2+g3+g4+g5+g6)/6
            m_tec=(x1+x2+x3+x4+x5+x6)/6
            
            df = pd.DataFrame({
                'Pilar': ['Estratégia', 'Financeiro', 'Cadeia', 'Governança', 'Tecnologia'],
                'Nível': [m_est, m_fin, m_cad, m_gov, m_tec]
            })
            st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
            
            detalhe = f"Est:{c1}-{c6}|Fin:{f1}-{f6}|Cad:{v1}-{v6}|Gov:{g1}-{g6}|Tec:{x1}-{x6}"
            resumo_wa = f"DIAG_CORPORATIVO_PROFUNDO%0A👤 Consultor: {nome}%0A🏢 Empresa: {empresa}%0A📝 Notas: {detalhe}"
            oferecer_proximos_passos(nome, empresa, resumo_wa)

# --- MENU ---
st.sidebar.title("Menu DANGELLI Hub")
op = st.sidebar.radio("Nível de Análise:", ["1. Maturidade Original", "3. Corporativo Completo"])
st.sidebar.divider()
st.sidebar.write("v 3.1 - Auditoria de Competências")

if op == "1. Maturidade Original":
    diagnostico_original_dangelli()
else:
    diagnostico_corporativo_completo()
