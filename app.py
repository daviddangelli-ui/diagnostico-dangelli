import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Diagnóstico DANGELLI", layout="wide")

# --- FUNÇÃO DE APOIO: WHATSAPP ---
def oferecer_proximos_passos(nome, empresa, resumo_msg):
    st.warning("⚠️ **ÚLTIMO PASSO OBRIGATÓRIO:**")
    link_final = f"https://wa.me/5531983984001?text={resumo_msg}"
    st.link_button("🚀 CLIQUE PARA ENVIAR DIAGNÓSTICO", link_final, use_container_width=True)
    st.divider()
    st.success(f"Processado para {nome}!")

# --- OPÇÃO 1: MATURIDADE ORIGINAL ---
def diagnostico_original_dangelli():
    st.header("🏛️ Maturidade: Reforma vs. Governança")
    with st.form("form1"):
        nome = st.text_input("Nome:"); emp = st.text_input("Empresa:")
        st.subheader("Responda de 1 a 5:")
        q1 = st.slider("Acordo de Sócios?", 1, 5, 1); q2 = st.slider("Atas de Diretoria?", 1, 5, 1)
        q3 = st.slider("Plano de Sucessão?", 1, 5, 1); q4 = st.slider("Separação Patrimonial?", 1, 5, 1)
        q5 = st.slider("Conselho Independente?", 1, 5, 1); q6 = st.slider("Código de Ética?", 1, 5, 1)
        q7 = st.slider("Holding constituída?", 1, 5, 1); q8 = st.slider("Proteção Cível?", 1, 5, 1)
        q9 = st.slider("Seguro D&O?", 1, 5, 1); q10 = st.slider("Estrutura de Capital?", 1, 5, 1)
        q11 = st.slider("Impenhorabilidade?", 1, 5, 1); q12 = st.slider("Planejamento 5 anos?", 1, 5, 1)
        q13 = st.slider("EBITDA mensal?", 1, 5, 1); q14 = st.slider("Valuation recente?", 1, 5, 1)
        q15 = st.slider("Auditoria?", 1, 5, 1); q16 = st.slider("Processos mapeados?", 1, 5, 1)
        q17 = st.slider("Impacto no Caixa?", 1, 5, 1); q18 = st.slider("Time treinado IVA?", 1, 5, 1)
        q19 = st.slider("Split Payment?", 1, 5, 1); q20 = st.slider("Revisão Contratos?", 1, 5, 1)
        q21 = st.slider("Comitês Transição?", 1, 5, 1)
        if st.form_submit_button("📊 GERAR GRÁFICO"):
            m_gov = (q1+q2+q3+q4+q5+q6)/6; m_blind = (q7+q8+q9+q10+q11)/5
            m_est = (q12+q13+q14+q15+q16)/5; m_ref = (q17+q18+q19+q20+q21)/5
            df = pd.DataFrame({'Pilar':['Gov','Blind','Est','Ref'],'Nível':[m_gov,m_blind,m_est,m_ref]})
            st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
            oferecer_proximos_passos(nome, emp, f"MATURIDADE%0ANome: {nome}")

# --- OPÇÃO 2: GOVERNANÇA E VALUATION ---
def diagnostico_valuation_ma():
    st.header("📈 Governança, Estratégia e Valuation")
    nome = st.text_input("Nome:"); emp = st.text_input("Empresa:")
    t1, t2, t3, t4 = st.tabs(["🏛️ Gov", "🛡️ Prot", "🎯 Est", "💰 Val"])
    with t1:
        g1 = st.slider("Acordo de Sócios?", 1, 5, 1); g2 = st.slider("Atas formalizadas?", 1, 5, 1)
        g3 = st.slider("Sucessão e Formação?", 1, 5, 1); g4 = st.slider("Conselhos (Família/Consult)?", 1, 5, 1)
        g5 = st.slider("Código de Ética?", 1, 5, 1); g6 = st.slider("Regras Sucessão/Morte?", 1, 5, 1)
        g7 = st.slider("Política de Lucros?", 1, 5, 1)
    with t2:
        p1 = st.slider("Holding Acionistas?", 1, 5, 1); p2 = st.slider("Acordo de Acionistas?", 1, 5, 1)
        p3 = st.slider("Proteção Ativos?", 1, 5, 1); p4 = st.slider("Seguros (D&O/Sucess)?", 1, 5, 1)
    with t3:
        e1 = st.slider("Plano 5 Anos?", 1, 5, 1); e2 = st.slider("KPIs Mensais?", 1, 5, 1)
        e3 = st.slider("DRE/EBITDA Mensal?", 1, 5, 1); e4 = st.slider("Alinhamento Reforma?", 1, 5, 1)
    with t4:
        v1 = st.slider("Valuation 2 anos?", 1, 5, 1); v2 = st.slider("Modelagem BP?", 1, 5, 1)
        v3 = st.slider("Estratégia Funding?", 1, 5, 1); v4 = st.slider("Pronto p/ Venda?", 1, 5, 1)
        v5 = st.slider("Value Drivers?", 1, 5, 1)
    if st.button("📊 ANALISAR VALUATION"):
        m_gov=(g1+g2+g3+g4+g5+g6+g7)/7; m_prot=(p1+p2+p3+p4)/4; m_est=(e1+e2+e3+e4)/4; m_val=(v1+v2+v3+v4+v5)/5
        df = pd.DataFrame({'Pilar':['Gov','Prot','Est','Val'],'Nível':[m_gov,m_prot,m_est,m_val]})
        st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
        oferecer_proximos_passos(nome, emp, f"VALUATION%0ANome: {nome}")

# --- OPÇÃO 3: CORPORATIVO COMPLETO ---
def diagnostico_corporativo_completo():
    st.header("🏢 Corporativo Profundo")
    nome = st.text_input("Executivo:"); emp = st.text_input("Cliente:")
    t1, t2, t3, t4, t5 = st.tabs(["Estratégia", "Financeiro", "Cadeia", "Governança", "Tecnologia"])
    with t1:
        c1 = st.slider("Dois Regimes?", 1, 5, 1); c2 = st.slider("Perenidade?", 1, 5, 1); c3 = st.slider("Decisão Robusta?", 1, 5, 1)
        c4 = st.slider("Cultura Ágil?", 1, 5, 1); c5 = st.slider("Painel Cenários?", 1, 5, 1); c6 = st.slider("Orquestração?", 1, 5, 1)
    with t2:
        f1 = st.slider("Fluxo Caixa?", 1, 5, 1); f2 = st.slider("Prejuízo Produtos?", 1, 5, 1); f3 = st.slider("EBITDA Preditivo?", 1, 5, 1)
        f4 = st.slider("Margem Líquida?", 1, 5, 1); f5 = st.slider("Custo Conformidade?", 1, 5, 1); f6 = st.slider("Dados Real-time?", 1, 5, 1)
    with t3:
        v1 = st.slider("Proposta Valor?", 1, 5, 1); v2 = st.slider("Elasticidade Preço?", 1, 5, 1); v3 = st.slider("Físico vs Digital?", 1, 5, 1)
        v4 = st.slider("Fornecedor Tóxico?", 1, 5, 1); v5 = st.slider("Eficiência Logística?", 1, 5, 1); v6 = st.slider("Contratos?", 1, 5, 1)
    with t4:
        g1 = st.slider("Patrimônio vs Risco?", 1, 5, 1); g2 = st.slider("Acordo Sócios?", 1, 5, 1); g3 = st.slider("Conselho Técnico?", 1, 5, 1)
        g4 = st.slider("Assinatura Balanço?", 1, 5, 1); g5 = st.slider("Sucessão Técnica?", 1, 5, 1); g6 = st.slider("Compliance?", 1, 5, 1)
    with t5:
        x1 = st.slider("Musculatura Técnica?", 1, 5, 1); x2 = st.slider("Retenção Talentos?", 1, 5, 1); x3 = st.slider("Treinamento?", 1, 5, 1)
        x4 = st.slider("ERP Ativo?", 1, 5, 1); x5 = st.slider("Dados Cadastrais?", 1, 5, 1); x6 = st.slider("Automação?", 1, 5, 1)
    if st.button("🚀 ANALISAR CORPORATIVO"):
        m_est=(c1+c2+c3+c4+c5+c6)/6; m_fin=(f1+f2+f3+f4+f5+f6)/6; m_com=(v1+v2+v3+v4+v5+v6)/6; m_gov=(g1+g2+g3+g4+g5+g6)/6; m_tec=(x1+x2+x3+x4+x5+x6)/6
        df = pd.DataFrame({'Pilar':['Est','Fin','Com','Gov','Tec'],'Nível':[m_est,m_fin,m_com,m_gov,m_tec]})
        st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
        oferecer_proximos_passos(nome, emp, f"CORPORATIVO%0ANome: {nome}")

# --- MENU ---
st.sidebar.title("DANGELLI Hub")
op = st.sidebar.radio("Escolha:", ["1. Maturidade Original", "2. Gov & Valuation", "3. Corporativo Completo"])
if op == "1. Maturidade Original": diagnostico_original_dangelli()
elif op == "2. Gov & Valuation": diagnostico_valuation_ma()
else: diagnostico_corporativo_completo()
