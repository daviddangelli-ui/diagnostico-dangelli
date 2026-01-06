import streamlit as st
import urllib.parse
import plotly.graph_objects as go

st.set_page_config(page_title="DANGELLI - Diagnóstico Profissional", layout="wide")

# Mapeamento de Notas para Cálculo
mapa_notas = {"Inexistente": 1.0, "2": 2.0, "3": 3.0, "4": 4.0, "Pleno": 5.0}

st.markdown("""# O que garante a **perenidade** de uma média empresa em tempos de transformações profundas?""")
st.info("""Governança e Estratégia integradas para a Reforma Tributária 2026.""")

with st.form("diagnostico_dangelli"):
    nome = st.text_input("Seu Nome Completo")
    empresa = st.text_input("Sua Empresa")
    options = ["Inexistente", "2", "3", "4", "Pleno"]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🏛️ Nível 1: Governança")
        g1 = st.select_slider("1. Acordo de Sócios?", options=options)
        g2 = st.select_slider("2. Plano de Sucessão?", options=options)
        g3 = st.select_slider("3. Separação PF/PJ?", options=options)
        g4 = st.select_slider("4. Conselho Ativo?", options=options)
        g5 = st.select_slider("5. Decisões Colegiadas?", options=options)

        st.markdown("### 🛡️ Nível 2: Blindagem")
        b1 = st.select_slider("1. Meritocracia vs Consanguinidade?", options=options)
        b2 = st.select_slider("2. Calendário Estratégico?", options=options)
        b3 = st.select_slider("3. Auditoria/Alçada?", options=options)
        b4 = st.select_slider("4. Cláusulas Tag/Drag Along?", options=options)
        b5 = st.select_slider("5. Protocolo Familiar?", options=options)
        b6 = st.select_slider("6. Visão clara sobre Sucessão?", options=options)

    with col2:
        st.markdown("### 🚀 Nível 3: Estratégia")
        e1 = st.select_slider("1. Visão de Expansão/Captação?", options=options)
        e2 = st.select_slider("2. Assédio/M&A?", options=options)
        e3 = st.select_slider("3. Conhece Variáveis de Valor?", options=options)
        e4 = st.select_slider("4. Acompanhamento de KPIs?", options=options)

        st.markdown("### ⚖️ Nível 4: Reforma Tributária")
        t1 = st.select_slider("1. Transição IVA?", options=options)
        t2 = st.select_slider("2. Simulação Margem 2026?", options=options)
        t3 = st.select_slider("3. Rastreado de Créditos?", options=options)
        t4 = st.select_slider("4. Estratégia de Preços?", options=options)
        t5 = st.select_slider("5. Monetização de Créditos?", options=options)
        t6 = st.select_slider("6. VALUATION e Reforma?", options=options)

    enviado = st.form_submit_button("GERAR DIAGNÓSTICO E SCORE")

if enviado:
    if not nome or not empresa:
        st.error("Preencha Nome e Empresa.")
    else:
        # Cálculo das Médias (Score 1.0 a 5.0)
        s_g = sum([mapa_notas[x] for x in [g1,g2,g3,g4,g5]]) / 5
        s_b = sum([mapa_notas[x] for x in [b1,b2,b3,b4,b5,b6]]) / 6
        s_e = sum([mapa_notas[x] for x in [e1,e2,e3,e4]]) / 4
        s_t = sum([mapa_notas[x] for x in [t1,t2,t3,t4,t5,t6]]) / 6

        st.success("Diagnóstico Concluído com Sucesso!")
        
        c1, c2 = st.columns([1, 1])
        with c1:
            # Gráfico de Radar (Estilo image_6e119f.png)
            fig = go.Figure(data=go.Scatterpolar(
                r=[s_g, s_b, s_e, s_t, s_g],
                theta=['Governança','Blindagem','Estratégia','Reforma','Governança'],
                fill='toself', line_color='#f39c12'
            ))
            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=False)
            st.plotly_chart(fig)

        with c2:
            st.metric("Score Governança", f"{s_g:.1f}/5.0")
            st.metric("Score Blindagem", f"{s_b:.1f}/5.0")
            st.metric("Score Estratégia", f"{s_e:.1f}/5.0")
            st.metric("Score Reforma", f"{s_t:.1f}/5.0")

        msg = f"Olá David! Sou {nome} da {empresa}. Score: G:{s_g:.1f} B:{s_b:.1f} E:{s_e:.1f} T:{s_t:.1f}."
        url_wa = f"https://api.whatsapp.com/send?phone=5531983984001&text={urllib.parse.quote(msg)}"
        st.link_button("🚀 CONFIRMAR PARTICIPAÇÃO E RECEBER RELATÓRIO", url_wa)
