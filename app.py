import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse

# Configuração da Página
st.set_page_config(page_title="DANGELLI - Diagnóstico Estratégico", layout="centered")

# Estilo Customizado
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #00c853; color: white; border-radius: 10px; font-weight: bold; width: 100%; }
    h1, h2, h3 { color: #d4af37; }
    .parecer-box { background-color: #1e2130; padding: 20px; border-radius: 10px; border-left: 5px solid #d4af37; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho Profissional
st.title("🛡️ Diagnóstico de Prontidão 2026")
st.subheader("DANGELLI Serviços - Conselho e Estratégia")
st.write("Especialista com **8 anos de parceria com a Fundação Dom Cabral (FDC)**.")
st.info("Preencha os campos abaixo para receber seu parecer estratégico imediato.")
st.write("---")

# Formulário (CAMPOS ZERADOS PARA O CLIENTE)
with st.form("diagnostico"):
    st.write("### 1. Identificação do Líder")
    nome = st.text_input("Seu Nome Completo", value="")
    empresa = st.text_input("Sua Empresa", value="")
    desafio = st.text_area("Qual seu maior desafio estratégico hoje?", value="")
    
    st.write("### 2. Avaliação (Notas 1 a 5)")
    n1 = st.slider("Processos e Governança", 1, 5, 1) # Começa no 1 (zerado)
    n2 = st.slider("Presença Digital", 1, 5, 1)
    n3 = st.slider("Uso de IA", 1, 5, 1)
    n4 = st.slider("Cultura de Dados", 1, 5, 1)
    n5 = st.slider("Gestão de Pessoas", 1, 5, 1)
    n6 = st.slider("Estratégia e Inovação", 1, 5, 1) # O NOVO 6º ITEM
    
    enviado = st.form_submit_button("GERAR MEU DIAGNÓSTICO E PARECER")

if enviado:
    if not nome or not empresa:
        st.error("Por favor, preencha seu nome e empresa antes de enviar.")
    else:
        media = (n1 + n2 + n3 + n4 + n5 + n6) / 6
        
        # Gráfico Radar com 6 Pilares
        df = pd.DataFrame({
            'Área': ["Processos", "Digital", "IA", "Dados", "Gestão", "Estratégia"],
            'Nota': [n1, n2, n3, n4, n5, n6]
        })
        fig = px.line_polar(df, r='Nota', theta='Área', line_close=True, range_r=[0,5])
        st.plotly_chart(fig)

        # Lógica de Parecer (1-2, 3-4, 5)
        if media <= 2.9:
            nivel = "PRIMEIRO NÍVEL (Sobrevivência)"
            parecer = "Atenção: Sua estrutura atual apresenta riscos para 2026. Foco em processos básicos e governança."
        elif media <= 4.9:
            nivel = "NÍVEL MÉDIO (Escalabilidade)"
            parecer = "Bom desempenho: Sua empresa tem maturidade, mas precisa de IA e dados para escala plena."
        else:
            nivel = "NÍVEL EXCELÊNCIA (Vanguarda)"
            parecer = "Parabéns: Você está no topo. O desafio agora é inovação disruptiva e novos oceanos azuis."

        st.markdown(f"""<div class="parecer-box"><h3>📋 Parecer Preliminar</h3>
            <p><b>Nível:</b> {nivel}</p><p>{parecer}</p></div>""", unsafe_allow_html=True)

        # WhatsApp Automático (Número com o 9)
        numero_faro = "5531983984001"
        resumo = f"Notas: P:{n1}, Dig:{n2}, IA:{n3}, Dad:{n4}, Ges:{n5}, Est:{n6} (Média: {media:.1f})"
        
        mensagem = (
            f"Olá David, sou {nome} da {empresa}.\n"
            f"Fiz o diagnóstico DANGELLI.\n"
            f"📊 {resumo}\n"
            f"🎯 Desafio: {desafio}\n"
            f"Quero garantir minha vaga na aula geral."
        )
        
        texto_url = urllib.parse.quote(mensagem)
        link_final = f"https://api.whatsapp.com/send?phone={numero_faro}&text={texto_url}"

        st.link_button("✅ ENVIAR RESULTADOS PARA O DAVID", link_final)
