import streamlit as st
import urllib.parse
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# Configuração da página
st.set_page_config(page_title="DANGELLI - Diagnóstico Estratégico", layout="wide")

# CSS para o Efeito Nuvem (Blur) e Estilização
st.markdown("""
    <style>
    .nuvem-blur {
        filter: blur(8px);
        -webkit-filter: blur(8px);
        pointer-events: none;
        user-select: none;
    }
    .reveal-box {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #f39c12;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Mapeamento de Notas
mapa_notas = {"Inexistente": 1.0, "2": 2.0, "3": 3.0, "4": 4.0, "Pleno": 5.0}

st.markdown("# O que garante a **perenidade** de uma média empresa?")
st.info("Diagnóstico Integrado: Governança, Estratégia e Reforma Tributária 2026.")

# Inicialização do estado de revelação
if 'revelado' not in st.session_state:
    st.session_state.revelado = False

with st.form("diagnostico_dangelli"):
    nome = st.text_input("Seu Nome Completo")
    empresa = st.text_input("Sua Empresa")
    options = ["Inexistente", "2", "3", "4", "Pleno"]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🏛️ Nível 1: Governança")
        g = [st.select_slider(f"G{i+1}", options=options, label_visibility="collapsed") for i in range(5)]
        st.markdown("### 🛡️ Nível 2: Blindagem")
        b = [st.select_slider(f"B{i+1}", options=options, label_visibility="collapsed") for i in range(6)]

    with col2:
        st.markdown("### 🚀 Nível 3: Estratégia")
        e = [st.select_slider(f"E{i+1}", options=options, label_visibility="collapsed") for i in range(4)]
        st.markdown("### ⚖️ Nível 4: Reforma Tributária")
        t = [st.select_slider(f"T{i+1}", options=options, label_visibility="collapsed") for i in range(6)]

    gerar = st.form_submit_button("ANALISAR MATURIDADE DO NEGÓCIO")

if gerar:
    if not nome or not empresa:
        st.error("Por favor, preencha Nome e Empresa.")
    else:
        # Cálculos
        s_g = sum([mapa_notas[x] for x in g]) / 5
        s_b = sum([mapa_notas[x] for x in b]) / 6
        s_e = sum([mapa_notas[x] for x in e]) / 4
        s_t = sum([mapa_notas[x] for x in t]) / 6
        
# 1. SALVAR NO GOOGLE SHEETS (Implementação Real)
       try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            
            # Buscando os valores direto da memória do seu formulário
            novo_lead = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "NOME": nome,
                "EMPRESA": empresa,
                "GOVERNANÇA": st.session_state.get('score_governanca', 0),
                "BLINDAGEM": st.session_state.get('score_blindagem', 0),
                "ESTRATÉGIA": st.session_state.get('score_estrategia', 0),
                "REFORMA": st.session_state.get('score_reforma', 0)
            }])
            
            # Envia os dados para a planilha DANGELLI
            conn.create(data=novo_lead)
        except Exception as e:
            # Mantém o erro discreto para não interromper a experiência do usuário
            print(f"Erro no salvamento: {e}")

        st.success(f"Diagnóstico de {nome} processado com sucesso!")

        # 2. ÁREA DE RESULTADOS (COM OU SEM BLUR)
        blur_class = "" if st.session_state.revelado else "class='nuvem-blur'"
        
        st.markdown(f"<div {blur_class}>", unsafe_allow_html=True)
        c1, c2 = st.columns([1.5, 1])
        with c1:
            fig = go.Figure(data=go.Scatterpolar(
                r=[s_g, s_b, s_e, s_t, s_g],
                theta=['Governança','Blindagem','Estratégia','Reforma','Governança'],
                fill='toself', line_color='#f39c12'
            ))
            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=False)
            st.plotly_chart(fig)
        with c2:
            st.metric("Governança", f"{s_g:.1f}/5.0")
            st.metric("Blindagem", f"{s_b:.1f}/5.0")
            st.metric("Estratégia", f"{s_e:.1f}/5.0")
            st.metric("Reforma", f"{s_t:.1f}/5.0")
        st.markdown("</div>", unsafe_allow_html=True)

        # 3. BOX DE CONVERSÃO (O GATILHO)
        if not st.session_state.revelado:
            st.markdown("""
                <div class="reveal-box">
                    <h3>🔍 SEU RESULTADO ESTÁ PRONTO!</h3>
                    <p>Para remover a 'nuvem' e visualizar seu gráfico detalhado e scores, 
                    confirme sua vaga na MasterClass e receba seu relatório via WhatsApp.</p>
                </div>
            """, unsafe_allow_html=True)
        
        msg = f"Olá David! Sou {nome} da {empresa}. Concluí meu diagnóstico e quero meu relatório completo."
        url_wa = f"https://api.whatsapp.com/send?phone=5531983984001&text={urllib.parse.quote(msg)}"
        
        if st.link_button("🚀 CONFIRMAR E REVELAR RESULTADOS", url_wa):
             st.session_state.revelado = True
