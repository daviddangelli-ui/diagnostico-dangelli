import streamlit as st
import urllib.parse
import plotly.graph_objects as go
import pandas as pd
class DANGELLI_APP:
    pass # Estrutura de organização interna
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
nome = st.text_input("Seu Nome Completo:")
empresa = st.text_input("Nome da sua Empresa:")

st.divider()

st.subheader("Avaliação Técnica (1: Inexistente | 5: Pleno)")

# FUNÇÃO DE CÁLCULO (Escala 1-5 para 0-10)
def score(lista):
    return round(((sum(lista)/len(lista)) - 1) / 4 * 10, 1)

# 3. AS 21 PERGUNTAS (INICIANDO EM 1)
with st.expander("🏛️ GOVERNANÇA E LONGEVIDADE", expanded=True):
    g1 = st.slider("1. Acordo de Sócios/Quotas formalizado?", 1, 5, 1)
    g2 = st.slider("2. Separação clara entre gestão e propriedade?", 1, 5, 1)
    g3 = st.slider("3. Reuniões de diretoria com atas documentadas?", 1, 5, 1)
    g4 = st.slider("4. Estrutura de Conselho Consultivo ou Fiscal?", 1, 5, 1)
    g5 = st.slider("5. Planejamento de continuidade e sucessão?", 1, 5, 1)
    g6 = st.slider("6. Governança focada em perpetuidade do negócio?", 1, 5, 1)

with st.expander("🛡️ PATRIMÔNIO E BLINDAGEM", expanded=True):
    b1 = st.slider("7. Segregação patrimonial (Sócio x Empresa)?", 1, 5, 1)
    b2 = st.slider("8. Utilização de Holding para proteção de ativos?", 1, 5, 1)
    b3 = st.slider("9. Seguro de responsabilidade para diretores (D&O)?", 1, 5, 1)
    b4 = st.slider("10. Planejamento sucessório (Doação/Usufruto)?", 1, 5, 1)
    b5 = st.slider("11. Proteção de ativos intangíveis e marcas?", 1, 5, 1)

with st.expander("📈 ESTRATÉGIA TRIBUTÁRIA E VALUATION", expanded=True):
    e1 = st.slider("12. Planejamento Tributário preventivo anual?", 1, 5, 1)
    e2 = st.slider("13. Revisão sistemática de créditos acumulados?", 1, 5, 1)
    e3 = st.slider("14. Estudo técnico de Valuation da empresa?", 1, 5, 1)
    e4 = st.slider("15. Impacto do passivo tributário no valor do negócio?", 1, 5, 1)
    e5 = st.slider("16. Gestão de EBITDA focada em valor de mercado?", 1, 5, 1)

with st.expander("⚡ REFORMA TRIBUTÁRIA 2026", expanded=True):
    r1 = st.slider("17. Cálculo de impacto CBS/IBS no faturamento?", 1, 5, 1)
    r2 = st.slider("18. Comitê de transição da Reforma Tributária?", 1, 5, 1)
    r3 = st.slider("19. Prontidão tecnológica para Split Payment?", 1, 5, 1)
    r4 = st.slider("20. Mapeamento de créditos na cadeia de suprimentos?", 1, 5, 1)
    r5 = st.slider("21. Plano de adequação financeira ao novo modelo?", 1, 5, 1)

# CÁLCULOS DAS MÉDIAS
m_gov = score([g1,g2,g3,g4,g5,g6])
m_bli = score([b1,b2,b3,b4,b5])
m_est = score([e1,e2,e3,e4,e5])
m_ref = score([r1,r2,r3,r4,r5])

# 4. BOTÃO DE ANÁLISE E GRAVAÇÃO
if st.button("ANALISAR MATURIDADE COMPLETA"):
    if not nome or not empresa:
        st.error("Preencha nome e empresa.")
    else:
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            df = pd.DataFrame([{"DATA": datetime.now().strftime("%d/%m/%Y %H:%M"), "NOME": nome, "EMPRESA": empresa, 
                                "GOVERNANÇA": m_gov, "BLINDAGEM": m_bli, "ESTRATÉGIA": m_est, "REFORMA": m_ref}])
            conn.create(worksheet="RESPOSTAS", data=df)
            st.success("✅ Diagnóstico sincronizado!")
        except:
            st.warning("Diagnóstico processado com sucesso!")

        # GRÁFICO
        categories = ['Governança', 'Blindagem', 'Estratégia', 'Reforma']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[m_gov, m_bli, m_est, m_ref], theta=categories, fill='toself'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=False)
        st.markdown('<div class="blur-container">', unsafe_allow_html=True)
        st.plotly_chart(fig)
        st.markdown('</div>', unsafe_allow_html=True)

        # MONTAGEM DA MENSAGEM DETALHADA PARA WHATSAPP
        detalhes = (
            f"*🏛️ GOVERNANÇA:* Q1:{g1}, Q2:{g2}, Q3:{g3}, Q4:{g4}, Q5:{g5}, Q6:{g6} (Média: {m_gov})\n"
            f"*🛡️ PATRIMÔNIO:* Q7:{b1}, Q8:{b2}, Q9:{b3}, Q10:{b4}, Q11:{b5} (Média: {m_bli})\n"
            f"*📈 ESTRATÉGIA:* Q12:{e1}, Q13:{e2}, Q14:{e3}, Q15:{e4}, Q16:{e5} (Média: {m_est})\n"
            f"*⚡ REFORMA:* Q17:{r1}, Q18:{r2}, Q19:{r3}, Q20:{r4}, Q21:{r5} (Média: {m_ref})"
        )
        
        texto_wa = (f"Olá David! Fiz o Diagnóstico DANGELLI.\n\n"
                    f"*Empresa:* {empresa}\n"
                    f"*Lead:* {nome}\n\n"
                    f"*NOTAS DETALHADAS (1 a 5):*\n{detalhes}\n\n"
                    f"Quero liberar minha análise completa.")
        
        link = f"https://wa.me/5531983984001?text=" + urllib.parse.quote(texto_wa)
        st.markdown(f'<a href="{link}" target="_blank"><button>🔓 LIBERAR ANÁLISE COMPLETA</button></a>', unsafe_allow_html=True)
