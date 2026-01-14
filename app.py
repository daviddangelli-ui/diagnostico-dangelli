import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO BÁSICA
st.set_page_config(page_title="DANGELLI Hub", layout="wide")

# --- FUNÇÃO DE APOIO: FINALIZAÇÃO E WHATSAPP ---
def oferecer_proximos_passos(nome, empresa, resumo_msg):
    st.divider()
    st.subheader("🎓 Próximos Passos: Masterclass DANGELLI")
    st.write(f"Parabéns, **{nome}**! Você deu o primeiro passo para a perenidade da **{empresa}**.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("📺 ASSISTIR MASTERCLASS", "https://youtube.com/@dangelliconsultoria", use_container_width=True)
    with col2:
        # Link do WhatsApp formatado de forma ultra-simples para evitar erro de servidor
        wa_url = f"https://wa.me/5531983984001?text={resumo_msg}"
        st.link_button("🚀 ENVIAR PARA ANÁLISE TÉCNICA", wa_url, use_container_width=True)

# --- OPÇÃO 1: MATURIDADE DANGELLI ORIGINAL ---
def diagnostico_original_dangelli():
    st.header("🏛️ Diagnóstico de Maturidade: Reforma Tributária vs. Governança")
    with st.form("form_original"):
        nome = st.text_input("Seu Nome Completo:")
        empresa = st.text_input("Nome da sua Empresa:")
        st.divider()
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Governança e Longevidade**")
            q1 = st.slider("Existe um Acordo de Sócios formalizado e atualizado?", 1, 5, 1)
            q2 = st.slider("As reuniões de diretoria são formalizadas em atas?", 1, 5, 1)
            q3 = st.slider("Há um plano de sucessão definido e comunicado?", 1, 5, 1)
            q4 = st.slider("O patrimônio pessoal está separado da empresa?", 1, 5, 1)
            q5 = st.slider("Existe um conselho ou diretoria independente?", 1, 5, 1)
            q6 = st.slider("O Código de Ética é conhecido por todos?", 1, 5, 1)
            st.markdown("**Blindagem Patrimonial**")
            q7 = st.slider("A empresa possui holding patrimonial?", 1, 5, 1)
            q8 = st.slider("Os ativos estão protegidos contra riscos cíveis?", 1, 5, 1)
            q9 = st.slider("Há seguro D&O para os diretores?", 1, 5, 1)
            q10 = st.slider("A estrutura de capital está otimizada?", 1, 5, 1)
            q11 = st.slider("Existem cláusulas de impenhorabilidade?", 1, 5, 1)
        with c2:
            st.markdown("**Estratégia e Valuation**")
            q12 = st.slider("Planejamento estratégico para os próximos 5 anos?", 1, 5, 1)
            q13 = st.slider("O EBITDA é monitorado mensalmente?", 1, 5, 1)
            q14 = st.slider("Valuation profissional nos últimos 2 anos?", 1, 5, 1)
            q15 = st.slider("Existe auditoria periódica?", 1, 5, 1)
            q16 = st.slider("Processos internos mapeados e padronizados?", 1, 5, 1)
            st.markdown("**Prontidão Reforma 2026**")
            q17 = st.slider("Mapeou impacto do IBS/CBS no fluxo de caixa?", 1, 5, 1)
            q18 = st.slider("Setor contábil recebeu treinamento para IVA?", 1, 5, 1)
            q19 = st.slider("Há estratégia para o Split Payment?", 1, 5, 1)
            q20 = st.slider("Contratos possuem revisão tributária?", 1, 5, 1)
            q21 = st.slider("Participa de comitês sobre a transição?", 1, 5, 1)
        
        submitted = st.form_submit_button("🚀 GERAR DIAGNÓSTICO CORPORATIVO")
        
    if submitted:
        if nome and empresa:
            m_gov = (q1+q2+q3+q4+q5+q6)/6
            m_blind = (q7+q8+q9+q10+q11)/5
            m_est = (q12+q13+q14+q15+q16)/5
            m_ref = (q17+q18+q19+q20+q21)/5
            
            df = pd.DataFrame({
                'Pilar': ['Governança', 'Blindagem', 'Estratégia', 'Reforma'],
                'Nível': [m_gov, m_blind, m_est, m_ref]
            })
            st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
            
            resumo = f"Nome: {nome} - Empresa: {empresa} - Medias: G:{m_gov:.1f} B:{m_blind:.1f} E:{m_est:.1f} R:{m_ref:.1f}"
            oferecer_proximos_passos(nome, empresa, resumo)

# --- OPÇÃO 2: GOVERNANÇA, ESTRATÉGIA E VALUATION ---
def diagnostico_valuation_ma():
    st.header("📈 Diagnóstico: Governança, Estratégia e Valuation")
    nome = st.text_input("Seu Nome:")
    empresa = st.text_input("Empresa:")
    
    t1, t2, t3, t4 = st.tabs(["🏛️ Governança", "🛡️ Proteção", "🎯 Estratégia", "💰 Valuation"])
    with t1:
        g1 = st.slider("Acordo de Sócios formalizado?", 1, 5, 1)
        g2 = st.slider("Atas de diretoria em dia?", 1, 5, 1)
        g3 = st.slider("Plano de sucessão definido?", 1, 5, 1)
        g4 = st.slider("Conselho Consultivo ativo?", 1, 5, 1)
    with t2:
        p1 = st.slider("Holding constituída?", 1, 5, 1)
        p2 = st.slider("Proteção contra riscos cíveis?", 1, 5, 1)
    with t3:
        e1 = st.slider("Planejamento 5 anos?", 1, 5, 1)
        e2 = st.slider("EBITDA mensal monitorado?", 1, 5, 1)
    with t4:
        v1 = st.slider("Valuation recente?", 1, 5, 1)
        v2 = st.slider("Visão de Value Drivers?", 1, 5, 1)

    if st.button("🚀 GERAR DIAGNÓSTICO CORPORATIVO", key="btn_val"):
        if nome and empresa:
            df = pd.DataFrame({
                'Pilar': ['Gov', 'Prot', 'Est', 'Val'],
                'Nível': [g1, p1, e1, v1]
            })
            st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
            resumo = f"Valuation - Nome: {nome} - Notas: {g1},{p1},{e1},{v1}"
            oferecer_proximos_passos(nome, empresa, resumo)

# --- OPÇÃO 3: CORPORATIVO COMPLETO ---
def diagnostico_corporativo_completo():
    st.header("🏢 Diagnóstico Corporativo Profundo")
    nome = st.text_input("Responsável:")
    empresa = st.text_input("Empresa Cliente:")
    
    tabs = st.tabs(["Estratégia", "Financeiro", "Cadeia", "Governança", "Tecnologia"])
    with tabs[0]:
        c1 = st.slider("Operação em dois regimes tributários?", 1, 5, 1)
        c2 = st.slider("Perenidade sem benefícios fiscais?", 1, 5, 1)
    with tabs[1]:
        f1 = st.slider("Impacto real no fluxo de caixa?", 1, 5, 1)
        f2 = st.slider("Margem líquida por canal?", 1, 5, 1)
    with tabs[2]:
        v1 = st.slider("Defesa de preço por valor?", 1, 5, 1)
        v2 = st.slider("Revisão de contratos longos?", 1, 5, 1)
    with tabs[3]:
        g1 = st.slider("Segregação patrimônio vs risco?", 1, 5, 1)
        g2 = st.slider("Sucessão técnica preparada?", 1, 5, 1)
    with tabs[4]:
        x1 = st.slider("Time contábil treinado?", 1, 5, 1)
        x2 = st.slider("ERP como ativo estratégico?", 1, 5, 1)

    if st.button("🚀 GERAR DIAGNÓSTICO CORPORATIVO", key="btn_corp"):
        if nome and empresa:
            df = pd.DataFrame({
                'Pilar': ['Est', 'Fin', 'Cad', 'Gov', 'Tec'],
                'Nível': [c1, f1, v1, g1, x1]
            })
            st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
            resumo = f"Corporativo - Nome: {nome} - Empresa: {empresa}"
            oferecer_proximos_passos(nome, empresa, resumo)

# --- MENU ---
st.sidebar.title("DANGELLI Hub")
op = st.sidebar.radio("Selecione:", ["Maturidade", "Valuation", "Corporativo"])
st.sidebar.divider()
st.sidebar.write("v 4.0 - Estabilidade Total")

if op == "Maturidade":
    diagnostico_original_dangelli()
elif op == "Valuation":
    diagnostico_valuation_ma()
else:
    diagnostico_corporativo_completo()
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="DANGELLI Hub de Maturidade", layout="wide")

# --- FUNÇÃO DE APOIO: WHATSAPP DETALHADO ---
def finalizar_com_wa(nome, empresa, tipo_diag, medias_txt, notas_txt):
    st.divider()
    st.subheader("🎓 Próximos Passos: Masterclass DANGELLI")
    st.write(f"Parabéns, **{nome}**! Você iniciou a jornada de perenidade da **{empresa}**.")
    
    # Montagem da mensagem rica para o WhatsApp
    texto_wa = (
        f"RESUMO_DIAGNOSTICO_{tipo_diag}%0A"
        f"👤 Nome: {nome}%0A"
        f"🏢 Empresa: {empresa}%0A"
        f"📊 {medias_txt}%0A"
        f"📝 Detalhamento: {notas_txt}"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("📺 ASSISTIR MASTERCLASS", "https://youtube.com/@dangelliconsultoria", use_container_width=True)
    with col2:
        link_final = f"https://wa.me/5531983984001?text={texto_wa}"
        st.link_button("🚀 ENVIAR RELATÓRIO COMPLETO", link_final, use_container_width=True)

# --- OPÇÃO 1: MATURIDADE DANGELLI ORIGINAL ---
def diag_original():
    st.header("🏛️ Maturidade: Reforma Tributária vs. Governança")
    with st.form("form_orig"):
        n = st.text_input("Nome Completo:"); e = st.text_input("Empresa:")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Governança & Longevidade**")
            q1=st.slider("1. Existe um Acordo de Sócios formalizado e atualizado?",1,5,1)
            q2=st.slider("2. As reuniões de diretoria são formalizadas em atas?",1,5,1)
            q3=st.slider("3. Há um plano de sucessão definido e comunicado?",1,5,1)
            q4=st.slider("4. O patrimônio pessoal está separado do da empresa?",1,5,1)
            q5=st.slider("5. Existe um conselho ou diretoria independente?",1,5,1)
            q6=st.slider("6. O Código de Ética é conhecido por todos?",1,5,1)
            st.markdown("**Blindagem Patrimonial**")
            q7=st.slider("7. A empresa possui holding patrimonial constituída?",1,5,1)
            q8=st.slider("8. Ativos protegidos contra riscos cíveis?",1,5,1)
            q9=st.slider("9. Há seguro D&O contratado para os diretores?",1,5,1)
            q10=st.slider("10. Estrutura de capital otimizada?",1,5,1)
            q11=st.slider("11. Cláusulas de impenhorabilidade nos bens?",1,5,1)
        with c2:
            st.markdown("**Estratégia & Valuation**")
            q12=st.slider("12. Planejamento estratégico formal (5 anos)?",1,5,1)
            q13=st.slider("13. EBITDA monitorado mensalmente com metas?",1,5,1)
            q14=st.slider("14. Valuation profissional nos últimos 2 anos?",1,5,1)
            q15=st.slider("15. Existe auditoria independente ou interna?",1,5,1)
            q16=st.slider("16. Processos cruciais mapeados e padronizados?",1,5,1)
            st.markdown("**Reforma 2026**")
            q17=st.slider("17. Mapeou impacto do IBS/CBS no caixa?",1,5,1)
            q18=st.slider("18. Setor contábil treinado para o modelo IVA?",1,5,1)
            q19=st.slider("19. Estratégia definida para o Split Payment?",1,5,1)
            q20=st.slider("20. Contratos possuem revisão tributária?",1,5,1)
            q21=st.slider("21. Participa de comitês sobre a transição?",1,5,1)
        
        if st.form_submit_button("🚀 GERAR RADAR DE MATURIDADE"):
            if n and e:
                m_gov=(q1+q2+q3+q4+q5+q6)/6; m_bli=(q7+q8+q9+q10+q11)/5; m_est=(q12+q13+q14+q15+q16)/5; m_ref=(q17+q18+q19+q20+q21)/5
                df=pd.DataFrame({'Pilar':['Gov','Blind','Est','Ref'],'Nível':[m_gov,m_bli,m_est,m_ref]})
                st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
                
                med_txt = f"Médias: G:{m_gov:.1f}, B:{m_bli:.1f}, E:{m_est:.1f}, R:{m_ref:.1f}"
                not_txt = f"G({q1},{q2},{q3},{q4},{q5},{q6}) B({q7},{q8},{q9},{q10},{q11}) E({q12},{q13},{q14},{q15},{q16}) R({q17},{q18},{q19},{q20},{q21})"
                finalizar_com_wa(n, e, "MATURIDADE", med_txt, not_txt)

# --- OPÇÃO 2: GOVERNANÇA, ESTRATÉGIA E VALUATION ---
def diag_valuation():
    st.header("📈 Governança, Estratégia e Valuation")
    with st.form("form_val"):
        n = st.text_input("Seu Nome:"); e = st.text_input("Empresa:")
        t1, t2 = st.columns(2)
        with t1:
            st.markdown("**Governança & Proteção**")
            g1=st.slider("Acordo de Sócios atualizado?",1,5,1); g2=st.slider("Conselho Consultivo ativo?",1,5,1); g3=st.slider("Holding e Proteção Cível?",1,5,1)
        with t2:
            st.markdown("**Estratégia & Valor**")
            v1=st.slider("Planejamento 5 anos e KPIs?",1,5,1); v2=st.slider("Valuation e Value Drivers?",1,5,1); v3=st.slider("Prontidão para M&A?",1,5,1)
        
        if st.form_submit_button("🚀 GERAR RADAR ESTRATÉGICO"):
            if n and e:
                df=pd.DataFrame({'Pilar':['Gov','Prot','Est','Val','M&A','KPI'],'Nível':[g1,g2,g3,v1,v2,v3]})
                st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
                finalizar_com_wa(n, e, "VALUATION", "Analise de Valor", f"Notas: {g1},{g2},{g3},{v1},{v2},{v3}")

# --- OPÇÃO 3: CORPORATIVO PROFUNDO ---
def diag_corp():
    st.header("🏢 Diagnóstico Corporativo Profundo")
    with st.form("form_corp"):
        n = st.text_input("Responsável:"); e = st.text_input("Empresa Cliente:")
        t1, t2, t3 = st.columns(3)
        with t1:
            st.markdown("**Estratégia**")
            c1=st.slider("Agilidade em dois regimes tributários?",1,5,1); c2=st.slider("Cultura de reação rápida?",1,5,1)
        with t2:
            st.markdown("**Financeiro**")
            f1=st.slider("Impacto real no Fluxo de Caixa?",1,5,1); f2=st.slider("Gestão preditiva de EBITDA?",1,5,1)
        with t3:
            st.markdown("**Tecnologia**")
            x1=st.slider("ERP como ativo estratégico?",1,5,1); x2=st.slider("Automação de processos?",1,5,1)
            
        if st.form_submit_button("🚀 GERAR DIAGNÓSTICO PROFUNDO"):
            if n and e:
                df=pd.DataFrame({'Pilar':['Estrat','Financ','Tecnol'],'Nível':[(c1+c2)/2, (f1+f2)/2, (x1+x2)/2]})
                st.plotly_chart(px.line_polar(df, r='Nível', theta='Pilar', line_close=True, range_r=[0,5]))
                finalizar_com_wa(n, e, "CORPORATIVO", "Analise Profunda", f"E:{c1},{c2} F:{f1},{f2} T:{x1},{x2}")

# --- MENU LATERAL ---
st.sidebar.title("DANGELLI Hub")
escolha = st.sidebar.radio("Selecione o Diagnóstico:", ["Maturidade Original", "Governança & Valuation", "Corporativo Profundo"])
st.sidebar.divider()
st.sidebar.write("v 4.1 - Estabilidade & Rico em Dados")

if escolha == "Maturidade Original": diag_original()
elif escolha == "Governança & Valuation": diag_valuation()
else: diag_corp()
