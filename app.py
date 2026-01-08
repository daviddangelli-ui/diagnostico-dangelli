import streamlit as st
import urllib.parse
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="DANGELLI - Diagnóstico de Maturidade", layout="centered")

# ESTILIZAÇÃO CSS
st.markdown("""
    <style>
    .blur-container { filter: blur(8px); -webkit-filter: blur(8px); pointer-events: none; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #25D366; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Diagnóstico de Maturidade: Reforma Tributária vs. Governança")

# 1. IDENTIFICAÇÃO
with st.container():
    nome = st.text_input("Seu Nome Completo:")
    empresa = st.text_input("Nome da sua Empresa:")

st.divider()

st.subheader("Avaliação Técnica de Maturidade (Escala 1 a 5)")
st.info("1: Inexistente | 2: Inicial | 3: Intermediário | 4: Avançado | 5: Pleno")

# --- BLOCO 1: GOVERNANÇA CORPORATIVA (6 Perguntas) ---
st.markdown("### 🏛️ Governança Corporativa")
g1 = st.slider("1. Acordo de Sócios/Quotas formalizado e atualizado?", 1, 5, 2)
g2 = st.slider("2. Separação entre gestão (executiva) e propriedade (sócios)?", 1, 5, 2)
g3 = st.slider("3. Periodicidade e formalização de reuniões de diretoria?", 1, 5, 2)
g4 = st.slider("4. Estrutura de Conselho (Consultivo ou Fiscal)?", 1, 5, 2)
g5 = st.slider("5. Transparência e Auditoria dos números da empresa?", 1, 5, 2)
g6 = st.slider("6. Implementação de Código de Conduta e Compliance?", 1, 5, 2)

# --- BLOCO 2: BLINDAGEM PATRIMONIAL (5 Perguntas) ---
st.markdown("### 🛡️ Blindagem Patrimonial")
b1 = st.slider("7. Segregação entre patrimônio pessoal e da PJ operacional?", 1, 5, 2)
b2 = st.slider("8. Utilização de Holding para proteção de ativos ativos?", 1, 5, 2)
b3 = st.slider("9. Existência de Plano de Sucessão e Governança Familiar?", 1, 5, 2)
b4 = st.slider("10. Proteção contra riscos de gestão (Seguro D&O)?", 1, 5, 2)
b5 = st.slider("11. Planejamento sucessório antecipado (Doação/Usufruto)?", 1, 5, 2)

# --- BLOCO 3: ESTRATÉGIA TRIBUTÁRIA (5 Perguntas) ---
st.markdown("### 📈 Estratégia Tributária")
e1 = st.slider("12. Revisão periódica de créditos tributários (últimos 5 anos)?", 1, 5, 2)
e2 = st.slider("13. Planejamento Tributário preventivo anual?", 1, 5, 2)
e3 = st.slider("14. Análise técnica de regime (Lucro Real vs. Presumido)?", 1, 5, 2)
e4 = st.slider("15. Monitoramento e gestão de passivos fiscais?", 1, 5, 2)
e5 = st.slider("16. Aproveitamento de incentivos fiscais do setor?", 1, 5, 2)

# --- BLOCO 4: REFORMA TRIBUTÁRIA (5 Perguntas) ---
st.markdown("### ⚡ Reforma Tributária 2026")
r1 = st.slider("17. Cálculo do impacto de preços (CBS/IBS) no faturamento?", 1, 5, 2)
r2 = st.slider("18. Comitê interno para transição da Reforma Tributária?", 1, 5, 2)
r3 = st.slider("19. Prontidão para o modelo de 'Split Payment'?", 1, 5, 2)
r4 = st.slider("20. Mapeamento da cadeia de fornecedores e créditos de IVA?", 1, 5, 2)
r5 = st.slider("21. Plano de adequação de sistemas (ERP) e Tecnologia?", 1, 5, 2)

# CÁLCULO DAS MÉDIAS (Convertendo escala 1-5 para 0-10)
# Fórmula: ((Média - 1) / 4) * 10
def calc_score(lista):
    media = sum(lista) / len(lista)
    return round(((media - 1) / 4) * 10, 1)

m_gov = calc_score([g1, g2, g3, g4, g5, g6])
m_bli = calc_score([b1, b2, b3, b4, b5])
m_est = calc_score([e1, e2, e3, e4, e5])
m_ref = calc_score([r1, r2, r3, r4, r5])

if st.button("ANALISAR MATURIDADE COMPLETA"):
    if not nome or not empresa:
        st.error("Por favor, preencha seu nome e a empresa.")
    else:
        # SALVAR NO GOOGLE SHEETS
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            novo_lead = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "NOME": nome,
                "EMPRESA": empresa,
                "GOVERNANÇA": m_gov,
                "BLINDAGEM": m_bli,
                "ESTRATÉGIA": m_est,
                "REFORMA": m_ref
            }])
            conn.create(worksheet="RESPOSTAS", data=novo_lead)
        except Exception as e:
            st.error("Erro ao gravar. Verifique se a aba da planilha chama-se RESPOSTAS.")

        # GRÁFICO DE RADAR
        categories = ['Governança', 'Blindagem', 'Estratégia', 'Reforma']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[m_gov, m_bli, m_est, m_ref], theta=categories, fill='toself', line_color='#1f77b4'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=False)

        st.subheader(f"Resultado Preliminar: {empresa}")
        st.markdown('<div class="blur-container">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.warning("⚠️ Diagnóstico concluído! Clique abaixo para liberar o relatório detalhado e remover o desfoque.")
        
        # WHATSAPP COM RESULTADOS
        meu_whats = "55119XXXXXXXX" # <-- COLOQUE SEU NÚMERO AQUI
        msg = (f"Olá! Concluí o Diagnóstico de Maturidade (21 Pontos).\n"
               f"*Empresa:* {empresa}\n"
               f"*Médias Apuradas:*\n"
               f"- Governança: {m_gov}/10\n"
               f"- Blindagem: {m_bli}/10\n"
               f"- Estratégia: {m_est}/10\n"
               f"- Reforma: {m_ref}/10\n\n"
               f"Quero liberar o gráfico completo e agendar análise técnica.")
        
        link_wa = f"https://wa.me/{meu_whats}?text={urllib.parse.quote(msg)}"
        st.markdown(f'<a href="{link_wa}" target="_blank"><button>🔓 LIBERAR ANÁLISE COMPLETA AGORA</button></a>', unsafe_allow_html=True)
