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
    st.info(f"Obrigado, {nome}! Seus dados foram enviados para análise técnica da DANGELLI.")

# --- ALTERNATIVA 1: O SEU CÓDIGO ORIGINAL (21 PERGUNTAS) ---
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
            resumo_wa = f"DIAGNÓSTICO DANGELLI%0A👤 Nome: {nome}%0A🏢 Empresa: {empresa}%0A%0A📊 Médias:%0AGov: {m_gov:.1f}%0ABlind: {m_blind:.1f}%0AEstrat: {m_estrat:.1f}%0ARef: {m_reforma:.1f}"
            oferecer_proximos_passos(nome, empresa, resumo_wa)

# --- ALTERNATIVA 2: PME (FOCO EM SOBREVIVÊNCIA) ---
def diagnostico_pme():
    st.header("💡 Diagnóstico Rápido: Foco em PMEs")
    nome_pme = st.text_input("Seu Nome (PME):")
    emp_pme = st.text_input("Empresa (PME):")
    p1 = st.toggle("A estratégia em vigência considera a turbulência de gerir dois sistemas tributários simultâneos?")
    p2 = st.toggle("Você tem controle real sobre a margem líquida ou olha apenas para o faturamento bruto?")
    p3 = st.toggle("Seu modelo de negócio suportará o aumento de carga tributária sem perda de clientes?")
    if st.button("Analisar Perfil PME"):
        resumo_pme = f"PERFIL PME%0A👤 Nome: {nome_pme}%0A🏢 Empresa: {emp_pme}%0AMargem Real: {p2}"
        oferecer_proximos_passos(nome_pme, emp_pme, resumo_pme)

# --- ALTERNATIVA 3: CORPORATIVO (EXATAMENTE COMO O PRINT) ---
def diagnostico_corporativo_interno():
    st.header("🏢 Diagnóstico Corporativo Profundo (Equipe Interna)")
    nome_corp = st.text_input("Consultor/Executivo Responsável:")
    emp_corp = st.text_input("Empresa Analisada:")
    aba1, aba2, aba3, aba4 = st.tabs(["Gestão Estratégica & Gov", "Gestão Financeira", "Cadeia & Comercial", "Pessoas & Inovação"])
    with aba1:
        st.subheader("Gestão Estratégica e Governança")
        c1 = st.checkbox("O atual modelo de negócios conseguirá operar pelos próximos 2 anos?")
        c2 = st.checkbox("A estratégia em vigência considera a turbulência de gerir dois sistemas tributários simultâneos?")
        c3 = st.checkbox("Sua empresa está sendo observada por alguma agência de risco (rating)?")
        c4 = st.checkbox("Existe clara segregação entre o patrimônio familiar e os riscos da operação?")
    with aba2:
        st.subheader("Gestão Financeira")
        c5 = st.checkbox("Você tem controle real sobre a margem líquida ou olha apenas para o faturamento bruto?")
        c6 = st.checkbox("Existe projeção do aumento da Necessidade de Capital de Giro (NCG) com a Reforma?")
        c7 = st.checkbox("Sua gestão financeira é preditiva (antecipa impacto no EBITDA)?")
        c8 = st.checkbox("Existe orçamento para o custo de conformidade (sistemas e treinamento)?")
    with aba3:
        st.subheader("Cadeia de Valor e Comercial")
        c9 = st.checkbox("Você mapeou quais fornecedores podem se tornar 'tóxicos' (não geram créditos)?")
        c10 = st.checkbox("Sua proposta de valor justifica repasse de custos ou perderá mercado por centavos?")
        c11 = st.checkbox("Existe um plano de revisão de contratos com cláusulas de impacto tributário?")
    with aba4:
        st.subheader("Pessoas, Inovação e Tecnologia")
        c12 = st.checkbox("Sua equipe tem 'musculatura técnica' para operar o novo sistema sem entrar em burnout?")
        c13 = st.checkbox("Seu ERP é um ativo estratégico ou uma âncora que impedirá o cálculo correto?")
        c14 = st.checkbox("A liderança está engajada em treinar o time para a transição digital/fiscal?")
    if st.button("Gerar Score Corporativo Completo"):
        pontos = sum([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14])
        total = 14
        percentual = (pontos/total)*100
        st.metric("Índice de Prontidão Corporativa", f"{percentual:.0f}%")
        st.progress(percentual/100)
        resumo_corp = f"CORPORATIVO%0A👤 De: {nome_corp}%0A🏢 Cliente: {emp_corp}%0AScore: {pontos}/{total}%0AProntidão: {percentual:.0f}%"
        oferecer_proximos_passos(nome_corp, emp_corp, resumo_corp)

# --- NAVEGAÇÃO LATERAL ---
st.sidebar.title("Menu DANGELLI")
opcao = st.sidebar.radio("Selecione o Diagnóstico:", ["1. Maturidade DANGELLI (Original)", "2. Perfil PME (Simplificado)", "3. Corporativo (Completo)"])
st.sidebar.divider()
st.sidebar.write("v 2.0 - Reforma Tributária & Governança")

if opcao == "1. Maturidade DANGELLI (Original)":
    diagnostico_original_dangelli()
elif opcao == "2. Perfil PME (Simplificado)":
    diagnostico_pme()
else:
    diagnostico_corporativo_interno()
