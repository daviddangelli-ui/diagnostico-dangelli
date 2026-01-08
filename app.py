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

# FUNÇÃO AUXILIAR PARA PONTUAÇÃO
def get_val(text):
    return int(text.split('(')[-1].split(')')[0])

# 2. AS 21 PERGUNTAS DETALHADAS
st.subheader("Avaliação Técnica de Maturidade")

# --- GOVERNANÇA CORPORATIVA (6 Perguntas) ---
st.markdown("### 🏛️ Governança Corporativa")
g1 = st.radio("1. Possui Acordo de Sócios/Quotas formalizado?", ["Não (0)", "Em rascunho (5)", "Sim, registrado (10)"])
g2 = st.radio("2. Separação clara entre gestão e propriedade?", ["Não (0)", "Parcial (5)", "Total (10)"])
g3 = st.radio("3. Reuniões de diretoria com atas?", ["Não (0)", "Eventuais (5)", "Mensais (10)"])
g4 = st.radio("4. Possui Conselho Consultivo ou Fiscal?", ["Não (0)", "Em implantação (5)", "Sim (10)"])
g5 = st.radio("5. Auditoria externa independente?", ["Não (0)", "Apenas interna (5)", "Sim (10)"])
g6 = st.radio("6. Código de Conduta e Compliance?", ["Não (0)", "Em rascunho (5)", "Sim (10)"])

# --- BLINDAGEM PATRIMONIAL (5 Perguntas) ---
st.markdown("### 🛡️ Blindagem Patrimonial")
b1 = st.radio("7. Patrimônio pessoal separado da PJ operacional?", ["Não (0)", "Parcial (5)", "Total (10)"])
b2 = st.radio("8. Utiliza Holding Patrimonial?", ["Não (0)", "Em estudo (5)", "Sim (10)"])
b3 = st.radio("9. Plano de Sucessão definido?", ["Não (0)", "Informal (5)", "Documentado (10)"])
b4 = st.radio("10. Seguro de responsabilidade (D&O)?", ["Não (0)", "Em cotação (5)", "Sim (10)"])
b5 = st.radio("11. Doação com reserva de usufruto realizada?", ["Não (0)", "Em análise (5)", "Sim (10)"])

# --- ESTRATÉGIA TRIBUTÁRIA (5 Perguntas) ---
st.markdown("### 📈 Estratégia Tributária")
e1 = st.radio("12. Planejamento Tributário anual?", ["Não (0)", "Pontual (5)", "Sim (10)"])
e2 = st.radio("13. Revisão de créditos tributários (5 anos)?", ["Nunca (0)", "Há mais de 2 anos (5)", "Sim, constante (10)"])
e3 = st.radio("14. Estudo de viabilidade de regime (Real x Presumido)?", ["Não (0)", "Superficial (5)", "Sim, técnico (10)"])
e4 = st.radio("15. Gestão de passivo tributário ativa?", ["Não (0)", "Parcial (5)", "Sim (10)"])
e5 = st.radio("16. Incentivos fiscais mapeados?", ["Não (0)", "Alguns (5)", "Sim (10)"])

# --- REFORMA TRIBUTÁRIA (5 Perguntas) ---
st.markdown("### ⚡ Reforma Tributária")
r1 = st.radio("17. Cálculo de impacto CBS/IBS realizado?", ["Não (0)", "Superficial (5)", "Sim (10)"])
r2 = st.radio("18. Comitê de transição da Reforma?", ["Não (0)", "Contabilidade olha (5)", "Sim, estratégico (10)"])
r3 = st.radio("19. Plano para o 'Split Payment'?", ["Não sei o que é (0)", "Em estudo (5)", "Sim (10)"])
r4 = st.radio("20. Mapeamento da cadeia de fornecedores (IVA)?", ["Não (0)", "Iniciado (5)", "Sim (10)"])
r5 = st.radio("21. Treinamento da equipa sobre o novo modelo?", ["Não (0)", "Previsto (5)", "Sim (10)"])

# CÁLCULOS DAS MÉDIAS
m_gov = (get_val(g1) + get_val(g2) + get_val(g3) + get_val(g4) + get_val(g5) + get_val(g6)) / 6
m_bli = (get_val(b1) + get_val(b2) + get_val(b3) + get_val(b4) + get_val(b5)) / 5
m_est = (get_val(e1) + get_val(e2) + get_val(e3) + get_val(e4) + get_val(e5)) / 5
m_ref = (get_val(r1) + get_val(r2) + get_val(r3) + get_val(r4) + get_val(r5)) / 5

if st.button("ANALISAR MATURIDADE COMPLETA"):
    if not nome or not empresa:
        st.error("Por favor, preencha nome e empresa.")
    else:
        # SALVAR NO GOOGLE SHEETS
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            novo_lead = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "NOME": nome,
                "EMPRESA": empresa,
                "GOVERNANÇA": round(m_gov, 1),
                "BLINDAGEM": round(m_bli, 1),
                "ESTRATÉGIA": round(m_est, 1),
                "REFORMA": round(m_ref, 1)
            }])
            conn.create(worksheet="RESPOSTAS", data=novo_lead)
        except Exception as e:
            st.error("Erro ao salvar. Verifique se a aba chama-se RESPOSTAS.")

        # GRÁFICO DE RADAR
        categories = ['Governança', 'Blindagem', 'Estratégia', 'Reforma']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[m_gov, m_bli, m_est, m_ref], theta=categories, fill='toself', line_color='#1f77b4'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=False)

        st.subheader(f"Diagnóstico DANGELLI: {empresa}")
        st.markdown('<div class="blur-container">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.warning("⚠️ Diagnóstico de 21 pontos concluído! Clique abaixo para remover o desfoque e receber o relatório.")
        
        # WHATSAPP COM RESULTADOS
        meu_whats = "5531983984001"
        msg = (f"Olá! Fiz o Diagnóstico Completo (21 pontos).\n"
               f"*Empresa:* {empresa}\n"
               f"*Médias:*\n"
               f"- Governança: {m_gov:.1f}\n"
               f"- Blindagem: {m_bli:.1f}\n"
               f"- Estratégia: {m_est:.1f}\n"
               f"- Reforma: {m_ref:.1f}\n\n"
               f"Quero agendar a minha reunião de análise.")
        
        link_wa = f"https://wa.me/{meu_whats}?text={urllib.parse.quote(msg)}"
        st.markdown(f'<a href="{link_wa}" target="_blank"><button>🔓 LIBERAR ANÁLISE COMPLETA</button></a>', unsafe_allow_html=True)
