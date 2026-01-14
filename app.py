import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Diagnóstico de Maturidade DANGELLI", layout="wide")

# --- FUNÇÃO DE APOIO: FINALIZAÇÃO (WHATSAPP E MASTERCLASS) ---
def oferecer_proximos_passos(nome, empresa, resumo_msg):
    st.warning("⚠️ **ÚLTIMO PASSO OBRIGATÓRIO:**")
    link_final = f"https://wa.me/5531983984001?text={resumo_msg}"
    st.link_button("🚀 CLIQUE AQUI PARA CONCLUIR E ENVIAR DIAGNÓSTICO", link_final, use_container_width=True)
    st.divider()
    st.success(f"Análise processada para {nome}!")
    st.info(f"Obrigado, {nome}! Seus dados foram enviados para a central técnica da DANGELLI.")

# --- ALTERNATIVA 1: MATURIDADE ORIGINAL (21 QUESTÕES) ---
def diagnostico_original_dangelli():
    st.header("🏛️ Diagnóstico de Maturidade: Reforma Tributária vs. Governança")
    with st.form("diagnostico_form"):
        st.subheader("📋 Identificação")
        nome = st.text_input("Seu Nome Completo:")
        empresa = st.text_input("Nome da sua Empresa:")
        st.divider()
        st.subheader("📊 Responda às 21 questões fundamentais (Nível 1 a 5):")
        
        st.info("Pilar 1: Governança e Longevidade")
        q1 = st.slider("1. Existe um Acordo de Sócios formalizado?", 1, 5, 1); q2 = st.slider("2. As reuniões de diretoria são formalizadas em atas?", 1, 5, 1); q3 = st.slider("3. Há um plano de sucessão definido?", 1, 5, 1); q4 = st.slider("4. Patrimônio pessoal separado do da empresa?", 1, 5, 1); q5 = st.slider("5. Existe conselho consultivo independente?", 1, 5, 1); q6 = st.slider("6. O Código de Ética é conhecido por todos?", 1, 5, 1)
        
        st.info("Pilar 2: Blindagem e Proteção Patrimonial")
        q7 = st.slider("7. Possui holding patrimonial constituída?", 1, 5, 1); q8 = st.slider("8. Ativos protegidos contra riscos cíveis?", 1, 5, 1); q9 = st.slider("9. Há seguro D&O para diretores?", 1, 5, 1); q10 = st.slider("10. Estrutura de capital otimizada?", 1, 5, 1); q11 = st.slider("11. Cláusulas de impenhorabilidade nos bens?", 1, 5, 1)
        
        st.info("Pilar 3: Estratégia e Valuation")
        q12 = st.slider("12. Possui planejamento estratégico (5 anos)?", 1, 5, 1); q13 = st.slider("13. EBITDA monitorado mensalmente?", 1, 5, 1); q14 = st.slider("14. Fez Valuation nos últimos 2 anos?", 1, 5, 1); q15 = st.slider("15. Possui auditoria independente?", 1, 5, 1); q16 = st.slider("16. Processos internos mapeados?", 1, 5, 1)
        
        st.info("Pilar 4: Prontidão para a Reforma Tributária 2026")
        q17 = st.slider("17. Mapeou impacto do IBS/CBS no caixa?", 1, 5, 1); q18 = st.slider("18. Setor contábil treinado para IVA?", 1, 5, 1); q19 = st.slider("19. Estratégia para o Split Payment?", 1, 5, 1); q20 = st.slider("20. Cláusulas de revisão tributária em contratos?", 1, 5, 1); q21 = st.slider("21. Participa de comitês sobre a transição?", 1, 5, 1)
        
        submitted = st.form_submit_button("📊 GERAR MEU GRÁFICO")

    if submitted:
        if nome and empresa:
            m_gov = (q1+q2+q3+q4+q5+q6)/6; m_blind = (q7+q8+q9+q10+q11)/5; m_estrat = (q12+q13+q14+q15+q16)/5; m_reforma = (q17+q18+q19+q20+q21)/5
            df_radar = pd.DataFrame({'Pilar': ['Governança', 'Blindagem', 'Estratégia', 'Reforma 2026'], 'Nível': [m_gov, m_blind, m_estrat, m_reforma]})
            fig = px.line_polar(df_radar, r='Nível', theta='Pilar', line_close=True, range_r=[0,5])
            st.plotly_chart(fig)
            resumo_wa = f"MATURIDADE ORIGINAL%0A👤 Nome: {nome}%0A🏢 Empresa: {empresa}%0A%0A📊 Médias:%0AGov: {m_gov:.1f}%0ABlind: {m_blind:.1f}%0AEstrat: {m_estrat:.1f}%0ARef: {m_reforma:.1f}"
            oferecer_proximos_passos(nome, empresa, resumo_wa)

# --- ALTERNATIVA 2: PME (SIMPLIFICADO) ---
def diagnostico_pme():
    st.header("💡 Perfil PME: Diagnóstico Rápido")
    nome_pme = st.text_input("Seu Nome:")
    emp_pme = st.text_input("Empresa:")
    p1 = st.select_slider("Estratégia para dois sistemas tributários:", options=[1, 2, 3, 4, 5])
    p2 = st.select_slider("Controle de margem líquida (vs bruto):", options=[1, 2, 3, 4, 5])
    p3 = st.select_slider("Resiliência do modelo de negócio:", options=[1, 2, 3, 4, 5])
    if st.button("Analisar PME"):
        resumo_pme = f"PERFIL PME%0A👤 Nome: {nome_pme}%0A🏢 Empresa: {emp_pme}%0AMédia: {(p1+p2+p3)/3:.1f}"
        oferecer_proximos_passos(nome_pme, emp_pme, resumo_pme)

# --- ALTERNATIVA 3: CORPORATIVO COMPLETO (TODAS AS QUESTÕES ENVIADAS) ---
def diagnostico_corporativo_completo():
    st.header("🏢 Diagnóstico Corporativo Profundo")
    st.markdown("Auditoria de Competências Organizacionais, Áreas e Individuais (Nível 1 a 5)")
    
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
        st.subheader("Gestão Financeira e Tributária")
        f1 = st.slider("Capacidade de prever impacto no fluxo de caixa (créditos)?", 1, 5, 1)
        f2 = st.slider("Mapeamento de prejuízo em produtos sob novas alíquotas?", 1, 5, 1)
        f3 = st.slider("Gestão preditiva (EBITDA) vs Reativa (incêndios)?", 1, 5, 1)
        f4 = st.slider("Controle da Margem de Contribuição Líquida?", 1, 5, 1)
        f5 = st.slider("Orçamento para custo de conformidade (transição)?", 1, 5, 1)
        f6 = st.slider("Integridade de dados para fiscalização em tempo real?", 1, 5, 1)

    with tabs[2]:
        st.subheader("Cadeia de Valor e Comercial")
        v1 = st.subheader("Comercial e Marketing")
        v1 = st.slider("Defesa de preço baseada em Proposta de Valor?", 1, 5, 1)
        v2 = st.slider("Conhecimento da elasticidade de preço do cliente?", 1, 5, 1)
        v3 = st.slider("Prontidão para equalização físico vs digital (canais)?", 1, 5, 1)
        v4 = st.subheader("Suprimentos e Logística")
        v4 = st.slider("Plano B para fornecedores 'tóxicos' tributariamente?", 1, 5, 1)
        v5 = st.slider("Eficiência real da logística (sem dependência de guerras fiscais)?", 1, 5, 1)
        v6 = st.slider("Proteção de margem em contratos de longo prazo?", 1, 5, 1)

    with tabs[3]:
        st.subheader("Governança, Acionistas e Sucessão")
        g1 = st.slider("Segregação clara entre patrimônio familiar e riscos operacionais?", 1, 5, 1)
        g2 = st.slider("Acordo de sócios robusto para reestruturações societárias?", 1, 5, 1)
        g3 = st.slider("Conselho com competência técnica para direcionar a estratégia?", 1, 5, 1)
        g4 = st.slider("Conforto dos acionistas em assinar demonstrações sob incerteza?", 1, 5, 1)
        g5 = st.slider("Plano de sucessão com foco na competência técnica para a 'tempestade'?", 1, 5, 1)
        g6 = st.slider("Transparência e Compliance (fim dos pontos cegos)?", 1, 5, 1)

    with tabs[4]:
        st.subheader("Pessoas, Inovação e Tecnologia")
        t1 = st.slider("Musculatura técnica da equipe (evitar burnout na transição)?", 1, 5, 1)
        t2 = st.slider("Plano de retenção de talentos chave (guerra por mão de obra)?", 1, 5, 1)
        t3 = st.slider("Plano de treinamento para 're-alfabetizar' a empresa?", 1, 5, 1)
        t4 = st.slider("ERP como ativo estratégico vs âncora de cálculo?", 1, 5, 1)
        t5 = st.slider("Qualidade e confiança 100% nos dados cadastrais?", 1, 5, 1)
        t6 = st.slider("Investimento em automação vs inchaço de folha manual?", 1, 5, 1)

    if st.button("🚀 GERAR DIAGNÓSTICO CORPORATIVO COMPLETO"):
        if nome and empresa:
            # Cálculos de médias por aba
            m_estrat = (c1+c2+c3+c4+c5+c6)/6
            m_fin = (f1+f2+f3+f4+f5+f6)/6
            m_com = (v1+v2+v3+v4+v5+v6)/6
            m_gov = (g1+g2+g3+g4+g5+g6)/6
            m_tec = (t1+t2+t3+t4+t5+t6)/6
            
            df_radar = pd.DataFrame({
                'Pilar': ['Estratégia', 'Financeiro', 'Comercial/Cadeia', 'Governança', 'Pessoas/Tec'],
                'Nível': [m_estrat, m_fin, m_com, m_gov, m_tec]
            })
            
            fig = px.line_polar(df_radar, r='Nível', theta='Pilar', line_close=True, range_r=[0,5])
            st.plotly_chart(fig)
            
            status = "CRÍTICO" if (m_estrat+m_fin+m_com+m_gov+m_tec)/5 < 3 else "ESTRATÉGICO"
            resumo_wa = f"DIAGNÓSTICO CORPORATIVO%0A👤 De: {nome}%0A🏢 Empresa: {empresa}%0A%0A📊 Médias:%0AEstrat: {m_estrat:.1f}%0AFin: {m_fin:.1f}%0ACom: {m_com:.1f}%0AGov: {m_gov:.1f}%0ATec: {m_tec:.1f}%0AStatus: {status}"
            oferecer_proximos_passos(nome, empresa, resumo_wa)
        else:
            st.error("Preencha o Nome e a Empresa Cliente.")

# --- NAVEGAÇÃO LATERAL ---
st.sidebar.title("Menu DANGELLI")
opcao = st.sidebar.radio("Selecione o Modelo:", 
    ["1. Maturidade DANGELLI (Original)", "2. Perfil PME (Simplificado)", "3. Corporativo (Completo)"])
st.sidebar.divider()
st.sidebar.write("v 2.1 - Auditoria de Competências")

if opcao == "1. Maturidade DANGELLI (Original)":
    diagnostico_original_dangelli()
elif opcao == "2. Perfil PME (Simplificado)":
    diagnostico_pme()
else:
    diagnostico_corporativo_completo()
