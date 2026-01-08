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
    .blur-container { filter: blur(8px); -webkit-filter: blur(8px); pointer-events: none; user-select: none; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #25D366; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Diagnóstico de Maturidade: Reforma Tributária vs. Governança")
st.write("Avalie os 21 pontos fundamentais para a perenidade do seu negócio.")

# 1. IDENTIFICAÇÃO DO LEAD
with st.container():
    nome = st.text_input("Seu Nome Completo:")
    empresa = st.text_input("Nome da sua Empresa:")

st.divider()

# FUNÇÃO PARA CALCULAR SCORE (Converte escala 1-5 para 0-10)
def calcular_pilar(lista_notas):
    media = sum(lista_notas) / len(lista_notas)
    return round(((media - 1) / 4) * 10, 1)

# 2. AS 21 PERGUNTAS (ESCALA 1-5)
st.subheader("Critérios de Avaliação (1: Inexistente | 5: Pleno)")

# GOVERNANÇA CORPORATIVA
with st.expander("🏛️ GOVERNANÇA CORPORATIVA", expanded=True):
    g1 = st.slider("1. Acordo de Sócios/Quotas formalizado e atualizado?", 1, 5, 2)
    g2 = st.slider("2. Separação clara entre gestão executiva e propriedade?", 1, 5, 2)
    g3 = st.slider("3. Reuniões de diretoria/conselho com atas documentadas?", 1, 5, 2)
    g4 = st.slider("4. Estrutura de Conselho Consultivo ou Fiscal?", 1, 5, 2)
    g5 = st.slider("5. Transparência e Auditoria periódica dos números?", 1, 5, 2)
    g6 = st.slider("6. Implementação de Código de Conduta e Compliance?", 1, 5, 2)

# BLINDAGEM PATRIMONIAL
with st.expander("🛡️ BLINDAGEM PATRIMONIAL", expanded=True):
    b1 = st.slider("7. Segregação entre patrimônio pessoal e da PJ operacional?", 1, 5, 2)
    b2 = st.slider("8. Utilização de Holding para proteção de ativos ativos?", 1, 5, 2)
    b3 = st.slider("9. Existência de Plano de Sucessão familiar e societária?", 1, 5, 2)
    b4 = st.slider("10. Proteção contra riscos de gestão (Seguro D&O)?", 1, 5, 2)
    b5 = st.slider("11. Planejamento sucessório antecipado (Doação/Usufruto)?", 1, 5, 2)

# ESTRATÉGIA TRIBUTÁRIA
with st.expander("📈 ESTRATÉGIA TRIBUTÁRIA", expanded=True):
    e1 = st.slider("12. Planejamento Tributário preventivo realizado anualmente?", 1, 5, 2)
    e2 = st.slider("13. Revisão sistemática de créditos (últimos 5 anos)?", 1, 5, 2)
    e3 = st.slider("14. Análise técnica de regime (Lucro Real vs. Presumido)?", 1, 5, 2)
    e4 = st.slider("15. Monitoramento e gestão ativa de passivos fiscais?", 1, 5, 2)
    e5 = st.slider("16. Aproveitamento integral de incentivos fiscais do setor?", 1, 5, 2)

# REFORMA TRIBUTÁRIA
with st.expander("⚡ REFORMA TRIBUTÁRIA 2026", expanded=True):
    r1 = st.slider("17. Cálculo do impacto de preços (CBS/IBS) no faturamento?", 1, 5, 2)
    r2 = st.slider("18. Comitê interno ou responsável pela transição da Reforma?", 1, 5, 2)
    r3 = st.slider("19. Prontidão para o novo modelo de 'Split Payment'?", 1, 5, 2)
    r4 = st.slider("20. Mapeamento da cadeia de fornecedores e créditos de IVA?", 1, 5, 2)
    r5 = st.slider("21. Plano de adequação de sistemas (ERP) e tecnologia?", 1, 5, 2)

# CÁLCULO DAS MÉDIAS FINAIS
score_gov = calcular_pilar([g1, g2, g3, g4, g5, g6])
score_bli = calcular_pilar([b1, b2, b3, b4, b5])
score_est = calcular_pilar([e1, e2, e3, e4, e5])
score_ref = calcular_pilar([r1, r2, r3, r4, r5])

if st.button("ANALISAR MATURIDADE COMPLETA"):
    if not nome or not empresa:
        st.error("Por favor, preencha seu Nome e o Nome da Empresa para gerar o gráfico.")
    else:
        # 1. SALVAMENTO NA PLANILHA (ABA RESPOSTAS)
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            df_lead = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "NOME": nome,
                "EMPRESA": empresa,
                "GOVERNANÇA": score_gov,
                "BLINDAGEM": score_bli,
                "ESTRATÉGIA": score_est,
                "REFORMA": score_ref
            }])
            conn.create(worksheet="RESPOSTAS", data=df_lead)
            st.success("✅ Diagnóstico registrado com sucesso!")
        except Exception as e:
            st.warning("Diagnóstico processado. (Nota: Erro de sincronismo com a planilha. Verifique os Secrets)")

        # 2. GRÁFICO DE RADAR
        categories = ['Governança', 'Blindagem', 'Estratégia', 'Reforma']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=[score_gov, score_bli, score_est, score_ref],
            theta=categories,
            fill='toself',
            name='Maturidade Atual',
            line_color='#1f77b4'
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            showlegend=False
        )

        st.subheader(f"Resultado Preliminar: {empresa}")
        
        # APLICA EFEITO BLUR NO GRÁFICO
        st.markdown('<div class="blur-container">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.warning("⚠️ Seu relatório detalhado está pronto! Clique no botão abaixo para liberar o acesso sem desfoque e agendar sua consultoria.")

        # 3. WHATSAPP CONFIGURADO
        whatsapp_numero = "5531983984001"
        texto_whats = (
            f"Olá David! Concluí o Diagnóstico DANGELLI de 21 Pontos.\n\n"
            f"*Nome:* {nome}\n"
            f"*Empresa:* {empresa}\n\n"
            f"*Médias Apuradas (0 a 10):*\n"
            f"🏛️ Governança: {score_gov}\n"
            f"🛡️ Blindagem: {score_bli}\n"
            f"📈 Estratégia: {score_est}\n"
            f"⚡ Reforma: {score_ref}\n\n"
            f"Gostaria de liberar meu gráfico completo e agendar a análise técnica."
        )
        
        link_final = f"https://wa.me/{whatsapp_numero}?text={urllib.parse.quote(texto_whats)}"
        
        st.markdown(f'<a href="{link_final}" target="_blank"><button>🔓 LIBERAR ANÁLISE COMPLETA AGORA</button></a>', unsafe_allow_html=True)
