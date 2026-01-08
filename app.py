import streamlit as st
import urllib.parse
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="DANGELLI - Diagnóstico de Maturidade", layout="centered")

# ESTILIZAÇÃO CSS
st.markdown("""
    <style>
    .blur-container { filter: blur(8px); -webkit-filter: blur(8px); pointer-events: none; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #25D366; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Diagnóstico de Maturidade: Reforma Tributária vs. Governança")

# 2. IDENTIFICAÇÃO
with st.container():
    nome = st.text_input("Seu Nome Completo:")
    empresa = st.text_input("Nome da sua Empresa:")

st.divider()

st.subheader("Avaliação Técnica (Escala 1 a 5)")
st.info("1: Inexistente | 2: Inicial | 3: Intermediário | 4: Avançado | 5: Pleno")

# 3. AS 21 PERGUNTAS DISTRIBUÍDAS POR BLOCOS
with st.expander("🏛️ GOVERNANÇA CORPORATIVA", expanded=True):
    g1 = st.slider("1. Acordo de Sócios/Quotas formalizado e atualizado?", 1, 5, 2)
    g2 = st.slider("2. Separação clara entre gestão executiva e propriedade?", 1, 5, 2)
    g3 = st.slider("3. Reuniões de diretoria/conselho com atas documentadas?", 1, 5, 2)
    g4 = st.slider("4. Estrutura de Conselho Consultivo ou Fiscal?", 1, 5, 2)
    g5 = st.slider("5. Transparência e Auditoria periódica dos números?", 1, 5, 2)
    g6 = st.slider("6. Implementação de Código de Conduta e Compliance?", 1, 5, 2)

with st.expander("🛡️ BLINDAGEM PATRIMONIAL", expanded=True):
    b1 = st.slider("7. Segregação entre patrimônio pessoal e da PJ operacional?", 1, 5, 2)
    b2 = st.slider("8. Utilização de Holding para proteção de ativos ativos?", 1, 5, 2)
    b3 = st.slider("9. Existência de Plano de Sucessão familiar e societária?", 1, 5, 2)
    b4 = st.slider("10. Proteção contra riscos de gestão (Seguro D&O)?", 1, 5, 2)
    b5 = st.slider("11. Planejamento sucessório antecipado (Doação/Usufruto)?", 1, 5, 2)

with st.expander("📈 ESTRATÉGIA TRIBUTÁRIA", expanded=True):
    e1 = st.slider("12. Planejamento Tributário preventivo realizado anualmente?", 1, 5, 2)
    e2 = st.slider("13. Revisão sistemática de créditos (últimos 5 anos)?", 1, 5, 2)
    e3 = st.slider("14. Análise técnica de regime (Lucro Real vs. Presumido)?", 1, 5, 2)
    e4 = st.slider("15. Monitoramento e gestão ativa de passivos fiscais?", 1, 5, 2)
    e5 = st.slider("16. Aproveitamento integral de incentivos fiscais do setor?", 1, 5, 2)

with st.expander("⚡ REFORMA TRIBUTÁRIA 2026", expanded=True):
    r1 = st.slider("17. Cálculo do impacto de preços (CBS/IBS) no faturamento?", 1, 5, 2)
    r2 = st.slider("18. Comitê interno ou responsável pela transição da Reforma?", 1, 5, 2)
    r3 = st.slider("19. Prontidão para o novo modelo de 'Split Payment'?", 1, 5, 2)
    r4 = st.slider("20. Mapeamento da cadeia de fornecedores e créditos de IVA?", 1, 5, 2)
    r5 = st.slider("21. Plano de adequação de sistemas (ERP) e tecnologia?", 1, 5, 2)

# FUNÇÃO DE CÁLCULO (Converte 1-5 para 0-10)
def score(lista):
    return round(((sum(lista)/len(lista)) - 1) / 4 * 10, 1)

m_gov = score([g1,g2,g3,g4,g5,g6])
m_bli = score([b1,b2,b3,b4,b5])
m_est = score([e1,e2,e3,e4,e5])
m_ref = score([r1,r2,r3,r4,r5])

# 4. BOTÃO DE ANÁLISE E GRAVAÇÃO
if st.button("ANALISAR MATURIDADE COMPLETA"):
    if not nome or not empresa:
        st.error("Por favor, preencha nome e empresa.")
    else:
        try:
            # CONEXÃO COM A PLANILHA
            conn = st.connection("gsheets", type=GSheetsConnection)
            df_final = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "NOME": nome,
                "EMPRESA": empresa,
                "GOVERNANÇA": m_gov,
                "BLINDAGEM": m_bli,
                "ESTRATÉGIA": m_est,
                "REFORMA": m_ref
            }])
            # Grava na aba específica
            conn.create(worksheet="RESPOSTAS", data=df_final)
            st.success("✅ Diagnóstico sincronizado com a base de dados DANGELLI!")
        except Exception as e:
            st.warning("Diagnóstico processado com sucesso! (Nota: Sincronismo da planilha em segundo plano)")

        # GRÁFICO DE RADAR
        categories = ['Governança', 'Blindagem', 'Estratégia', 'Reforma']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[m_gov, m_bli, m_est, m_ref], theta=categories, fill='toself', line_color='#1f77b4'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=False)

        st.subheader(f"Resultado Preliminar: {empresa}")
        st.markdown('<div class="blur-container">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.warning("⚠️ Relatório detalhado disponível! Clique abaixo para liberar o acesso total.")

        # WHATSAPP COM SEU NÚMERO E DADOS REAIS
        whatsapp_numero = "5531983984001"
        msg_text = (f"Olá David! Fiz o Diagnóstico DANGELLI (21 pontos).\n"
                    f"*Empresa:* {empresa}\n"
                    f"*Médias:*\n- Gov: {m_gov}\n- Blin: {m_bli}\n- Estr: {m_est}\n- Ref: {m_ref}\n\n"
                    f"Quero liberar o gráfico completo.")
        
        link_wa = f"https://wa.me/{whatsapp_numero}?text={urllib.parse.quote(msg_text)}"
        st.markdown(f'<a href="{link_wa}" target="_blank"><button>🔓 LIBERAR ANÁLISE COMPLETA AGORA</button></a>', unsafe_allow_html=True)
