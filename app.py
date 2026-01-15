import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="DANGELLI Hub - Maturidade 2026", layout="wide")

# --- FUNÇÃO DE APOIO: WHATSAPP E PRÓXIMOS PASSOS ---
def oferecer_proximos_passos(nome, empresa, tipo_diag, resumo_medias, detalhamento_notas):
    st.divider()
    st.subheader("🎓 Próximos Passos: Masterclass DANGELLI")
    st.write(f"Parabéns, **{nome}**! Você deu o passo fundamental para a perenidade da **{empresa}**.")
    st.info("💡 **DICA ESTRATÉGICA:** Assista à nossa Masterclass exclusiva sobre Governança e a Nova Reforma Tributária.")
    
    # Formatação da mensagem para o WhatsApp
    texto_wa = (
        f"DIAGNÓSTICO_DANGELLI_{tipo_diag}%0A"
        f"👤 Nome: {nome}%0A"
        f"🏢 Empresa: {empresa}%0A%0A"
        f"📊 MÉDIAS:%0A{resumo_medias}%0A%0A"
        f"📝 RESPOSTAS DETALHADAS:%0A{detalhamento_notas}%0A%0A"
        f"🚀 Aguardo análise técnica e link da Masterclass."
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("📺 ASSISTIR MASTERCLASS GRATUITA", "https://youtube.com/@dangelliconsultoria", use_container_width=True)
    with col2:
        link_final = f"https://wa.me/5531983984001?text={texto_wa}"
        st.link_button("🚀 ENVIAR RESULTADOS PARA O CONSULTOR", link_final, use_container_width=True)

# --- DIAGNÓSTICO 1: ESTRUTURAÇÃO DA MATURIDADE 2026 ---
def diagnostico_estruturacao():
    st.header("🏛️ DIAGNÓSTICO 1 – ESTRUTURAÇÃO DA MATURIDADE 2026")
    with st.form("form_diag1"):
        nome = st.text_input("Seu Nome Completo:")
        empresa = st.text_input("Nome da sua Empresa:")
        st.divider()
        
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("GOVERNANÇA E LONGEVIDADE")
            q1 = st.slider("Existe um Acordo de Sócios formalizado?", 1, 5, 1)
            q2 = st.slider("Há um plano de sucessão definido (natural ou por morte)?", 1, 5, 1)
            q3 = st.slider("Patrimônio pessoal é separado do da empresa?", 1, 5, 1)
            q4 = st.slider("Existe conselho consultivo independente?", 1, 5, 1)
            q5 = st.slider("Existe um programa de Formação de Sucessores?", 1, 5, 1)
            q6 = st.slider("Existem regras definidas para exclusão da sociedade?", 1, 5, 1)
            q7 = st.slider("Existe uma política de distribuição de lucros?", 1, 5, 1)
            
            st.subheader("PROTEÇÃO DA EMPRESA E DO PATRIMÔNIO")
            q8 = st.slider("Possui holding patrimonial para o negócio e também para cada acionista?", 1, 5, 1)
            q9 = st.slider("Possui Acordo de Acionistas para o negócio e também para cada acionista?", 1, 5, 1)
            q10 = st.slider("Possui seguro para proteção dos ativos contra riscos cíveis?", 1, 5, 1)
            q11 = st.slider("Possui seguro contratado para questões de sucessão?", 1, 5, 1)
            q12 = st.slider("Possui seguro D&O para proteção dos Diretores e Administradores?", 1, 5, 1)
            q13 = st.slider("Possui regras para impenhorabilidade nos bens?", 1, 5, 1)
            q14 = st.slider("A empresa fez seu Valuation recente para conhecer o valor das cotas?", 1, 5, 1)
            q15 = st.slider("Já cogitaram venda ou foram assediados pelo mercado?", 1, 5, 1)

        with c2:
            st.subheader("ESTRATÉGIA E REFORMA TRIBUTÁRIA")
            q16 = st.slider("Possui planejamento estratégico (mapa, iniciativas, metas) para 5 anos?", 1, 5, 1)
            q17 = st.slider("Sabe de onde buscará recursos para a estratégia de crescimento?", 1, 5, 1)
            q18 = st.slider("Realiza reuniões mensais de indicadores, DRE e monitoração do EBITDA?", 1, 5, 1)
            q19 = st.slider("Entende e acompanha as variáveis chave geradoras de valor?", 1, 5, 1)
            q20 = st.slider("Treinou a equipe e possui ações alinhadas com a Reforma Tributária?", 1, 5, 1)
            q21 = st.slider("Instituiu Comitê de transição interno para sustentabilidade?", 1, 5, 1)
            q22 = st.slider("O setor contábil está alinhado com as novas regras?", 1, 5, 1)
            q23 = st.slider("Avaliou e tomou providências sobre o impacto do Split Payment no Giro?", 1, 5, 1)
            q24 = st.slider("Avaliou providências sobre o impacto da Reforma nas margens?", 1, 5, 1)
            q25 = st.slider("Está avaliando a renegociação de contratos para garantia de margens?", 1, 5, 1)
            q26 = st.slider("Já tem estudo para novas propostas considerando as novas regras?", 1, 5, 1)

        submit = st.form_submit_button("🚀 GERAR RADAR DE ESTRUTURAÇÃO")

    if submit and nome and empresa:
        m_gov = (q1+q2+q3+q4+q5+q6+q7)/7
        m_prot = (q8+q9+q10+q11+q12+q13+q14+q15)/8
        m_est = (q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26)/11
        
        df = pd.DataFrame({'Pilar':['Governança','Proteção','Estratégia'],'Nível':[m_gov, m_prot, m_est]})
        st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
        
        medias = f"- Gov: {m_gov:.1f}%0A- Prot: {m_prot:.1f}%0A- Estrat: {m_est:.1f}"
        detalhe = f"G:{q1},{q2},{q3},{q4},{q5},{q6},{q7}|P:{q8},{q9},{q10},{q11},{q12},{q13},{q14},{q15}|E:{q16}-{q26}"
        oferecer_proximos_passos(nome, empresa, "ESTRUTURACAO", medias, detalhe)

# --- DIAGNÓSTICO 2: MATURIDADE PLENA 2026 ---
def diagnostico_plena():
    st.header("🏢 DIAGNÓSTICO 2 – MATURIDADE PLENA 2026")
    with st.form("form_diag2"):
        nome = st.text_input("Responsável Técnico:")
        empresa = st.text_input("Empresa:")
        st.divider()
        
        t1, t2 = st.columns(2)
        with t1:
            st.subheader("GESTÃO FINANCEIRA E TRIBUTÁRIA")
            f1 = st.slider("Fluxo de caixa suporta impacto de não recuperar créditos na transição?", 1, 5, 1)
            f2 = st.slider("Existe projeção do aumento da Necessidade de Capital de Giro?", 1, 5, 1)
            f3 = st.slider("Clareza absoluta se margens de produtos darão prejuízo no novo modelo?", 1, 5, 1)
            f4 = st.slider("Gestão financeira preditiva vs reativa (apagando incêndios)?", 1, 5, 1)
            f5 = st.slider("Existe orçamento para o custo de conformidade e sistemas/consultoria?", 1, 5, 1)
            f6 = st.slider("Controle real sobre margem líquida após impactos sobre consumo?", 1, 5, 1)
            
            st.subheader("CADEIA DE VALOR, FORNECEDORES E CONTRATOS")
            c1 = st.slider("Contratos de longo prazo protegem margem contra aumento de alíquota?", 1, 5, 1)
            c2 = st.slider("Mapeou fornecedores 'tóxicos' que não geram créditos tributários?", 1, 5, 1)
            c3 = st.slider("Logística desenhada para eficiência real vs 'colcha de retalhos' fiscal?", 1, 5, 1)
            c4 = st.slider("Plano de renegociação ativo com parceiros estratégicos?", 1, 5, 1)
            c5 = st.slider("Integração permite visibilidade de crédito tributário em tempo real?", 1, 5, 1)

            st.subheader("COMERCIAL & MARKETING")
            m1 = st.slider("Proposta de Valor justifica preço quando alíquotas mudarem?", 1, 5, 1)
            m2 = st.slider("Equipe sabe explicar mudança de preço vs 'desculpa do imposto'?", 1, 5, 1)
            m3 = st.slider("Conhece a elasticidade de preço para repasse sem destruir demanda?", 1, 5, 1)
            m4 = st.slider("Estratégia de canais preparada para equalização de cargas?", 1, 5, 1)
            m5 = st.slider("Monitora concorrentes para evitar perda de market share na reforma?", 1, 5, 1)

        with t2:
            st.subheader("PESSOAS E CAPITAL HUMANO")
            p1 = st.slider("Equipe tem 'musculatura técnica' para dois sistemas tributários?", 1, 5, 1)
            p2 = st.slider("Possui plano de retenção para evitar perda de talentos fiscais?", 1, 5, 1)
            p3 = st.slider("Cultura incentiva adaptação rápida vs resistência a mudanças?", 1, 5, 1)
            p4 = st.slider("Plano robusto para 're-alfabetizar' a empresa sobre novos impostos?", 1, 5, 1)
            p5 = st.slider("Lideranças prontas para conduzir a equipe na incerteza?", 1, 5, 1)
            
            st.subheader("INOVAÇÃO E TECNOLOGIA")
            i1 = st.slider("ERP é um ativo estratégico ou uma âncora que impede cálculos?", 1, 5, 1)
            i2 = st.slider("Confia 100% na qualidade dos dados cadastrais atuais?", 1, 5, 1)
            i3 = st.slider("Investindo em automação vs inchar folha com trabalho manual?", 1, 5, 1)
            i4 = st.slider("Tecnologia permite simular cenários tributários em tempo real?", 1, 5, 1)
            i5 = st.slider("Modernizando processos vs 'digitalizando a burocracia velha'?", 1, 5, 1)

        submit = st.form_submit_button("🚀 GERAR RADAR DE MATURIDADE PLENA")

    if submit and nome and empresa:
        m_fin = (f1+f2+f3+f4+f5+f6)/6
        m_cad = (c1+c2+c3+c4+c5)/5
        m_com = (m1+m2+m3+m4+m5)/5
        m_pes = (p1+p2+p3+p4+p5)/5
        m_tec = (i1+i2+i3+i4+i5)/5
        
        df = pd.DataFrame({
            'Pilar': ['Financeiro', 'Cadeia', 'Comercial', 'Pessoas', 'Tecnologia'],
            'Nível': [m_fin, m_cad, m_com, m_pes, m_tec]
        })
        st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
        
        medias = f"- Fin: {m_fin:.1f}%0A- Cad: {m_cad:.1f}%0A- Com: {m_com:.1f}%0A- Pes: {m_pes:.1f}%0A- Tec: {m_tec:.1f}"
        detalhe = f"F:{f1}-{f6}|C:{c1}-{c5}|M:{m1}-{m5}|P:{p1}-{p5}|T:{i1}-{i5}"
        oferecer_proximos_passos(nome, empresa, "PLENA_2026", medias, detalhe)

# --- MENU LATERAL ---
st.sidebar.title("DANGELLI Hub")
st.sidebar.markdown("Avaliação de Maturidade Corporativa")
escolha = st.sidebar.radio("Selecione o Diagnóstico:", [
    "1. Estruturação da Maturidade", 
    "2. Maturidade Plena 2026"
])
st.sidebar.divider()
st.sidebar.write("v 5.0 - Auditoria Técnica")

if escolha == "1. Estruturação da Maturidade":
    diagnostico_estruturacao()
else:
    diagnostico_plena()
