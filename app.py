import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse
from perguntas import DIAGNOSTICO_1, DIAGNOSTICO_2, DIAGNOSTICO_MASTER

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="DANGELLI Hub - Maturidade 2026", layout="wide")

# --- FUNÇÃO DE APOIO: WHATSAPP E PRÓXIMOS PASSOS ---
def oferecer_proximos_passos(nome, empresa, tipo_diag, resumo_medias, detalhamento_notas):
    st.divider()
    st.subheader("🎓 Próximos Passos: DANGELLI Advisory")
    st.write(f"Parabéns, **{nome}**! Você deu o passo fundamental para a perenidade da **{empresa}**.")
    
    # Texto estruturado limpo para envio no WhatsApp
    texto_bruto = (
        f"DIAGNÓSTICO DANGELLI - {tipo_diag}\n"
        f"👤 Responsável: {nome}\n"
        f"🏢 Empresa: {empresa}\n\n"
        f"📊 MÉDIAS POR PILAR:\n{resumo_medias}\n"
        f"📌 DETALHAMENTO INICIAL:\n{detalhamento_notas}\n"
        f"🚀 Aguardo análise técnica da equipe DANGELLI."
    )
    
    # URL Encoding correto para não quebrar links no navegador
    texto_encoded = urllib.parse.quote(texto_bruto)
    
    # Número de telefone configurado
    numero_wa = "5531983984001"
    link_wa = f"https://wa.me/{numero_wa}?text={texto_encoded}"
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 **Análise de Governança:** Envie o relatório detalhado diretamente para nossa equipe de conselheiros.")
        st.link_button("🟢 Enviar Relatório via WhatsApp", link_wa, type="primary")

# --- MENU LATERAL (SIDEBAR) ---
st.sidebar.title("DANGELLI Hub")
st.sidebar.caption("Avaliação de Maturidade Corporativa")

opcao_diagnostico = st.sidebar.radio(
    "Selecione o Diagnóstico:",
    [
        "1. Estruturação da Maturidade",
        "2. Maturidade Plena 2026",
        "3. Diagnóstico Estratégico Master (82 Questões)"
    ]
)

st.sidebar.divider()
st.sidebar.caption("v 6.0 - DANGELLI Governance & Strategy")

# --- CABEÇALHO PRINCIPAL ---
st.title("🛡️ DANGELLI - Diagnóstico Estratégico Corporativo - inclui Reforma Tributária")

# Formulário de Identificação
col_a, col_b = st.columns(2)
with col_a:
    nome_usuario = st.text_input("Responsável Técnico / Avaliador:", key="resp_tec")
with col_b:
    empresa_usuario = st.text_input("Empresa / Organização:", key="emp_nome")

st.divider()

# --- CARREGAMENTO DAS PERGUNTAS CORRESPONDENTES ---
if "1. Estruturação" in opcao_diagnostico:
    config_atual = DIAGNOSTICO_1
elif "2. Maturidade Plena" in opcao_diagnostico:
    config_atual = DIAGNOSTICO_2
else:
    config_atual = DIAGNOSTICO_MASTER

# --- FORMULÁRIO DE AVALIAÇÃO ---
respostas = {}
pontuacoes_por_bloco = {}

with st.form("form_diagnostico"):
    st.subheader(f"📋 {opcao_diagnostico}")
    
    for bloco, lista_perguntas in config_atual.items():
        st.markdown(f"### {bloco}")
        notas_bloco = []
        
        for item in lista_perguntas:
            p_id = item["id"]
            p_texto = item["pergunta"]
            p_opcoes = item["opcoes"]
            
            escolha = st.selectbox(
                p_texto,
                options=list(p_opcoes.keys()),
                key=p_id
            )
            nota = p_opcoes[escolha]
            notas_bloco.append(nota)
            respostas[p_texto] = nota
            
        media_bloco = sum(notas_bloco) / len(notas_bloco) if notas_bloco else 0
        pontuacoes_por_bloco[bloco] = media_bloco
        st.divider()
        
    btn_calcular = st.form_submit_button("📊 Gerar Relatório de Maturidade")

# --- PROCESSAMENTO E EXIBIÇÃO DE RESULTADOS ---
if btn_calcular:
    if not nome_usuario or not empresa_usuario:
        st.warning("⚠️ Por favor, preencha o Nome e a Empresa no topo da página antes de gerar o relatório.")
    else:
        st.success("Diagnóstico concluído com sucesso!")
        
        st.header("📈 Desempenho por Bloco Estratégico")
        
        df_resultados = pd.DataFrame({
            "Bloco": list(pontuacoes_por_bloco.keys()),
            "Maturidade (0 a 3)": list(pontuacoes_por_bloco.values())
        })
        
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            fig_bar = px.bar(
                df_resultados, 
                x="Maturidade (0 a 3)", 
                y="Bloco", 
                orientation='h',
                range_x=[0, 3],
                title="Nota Média por Pilar",
                color="Maturidade (0 a 3)",
                color_continuous_scale="Reds"
            )
            st.plotly_chart(fig_bar, use_container_width=True)
            
        with col_chart2:
            fig_radar = px.line_polar(
                df_resultados, 
                r="Maturidade (0 a 3)", 
                theta="Bloco", 
                line_close=True,
                range_r=[0, 3],
                title="Matriz Radar de Maturidade"
            )
            st.plotly_chart(fig_radar, use_container_width=True)
            
        # Resumo formatado para envio
        resumo_texto = ""
        for bloco, media in pontuacoes_por_bloco.items():
            resumo_texto += f"• {bloco}: {media:.2f} / 3.0\n"
            
        detalhes_texto = ""
        for perg, nota in list(respostas.items())[:8]:
            detalhes_texto += f"• {perg[:35]}... = Nota {nota}\n"

        oferecer_proximos_passos(
            nome=nome_usuario,
            empresa=empresa_usuario,
            tipo_diag=opcao_diagnostico,
            resumo_medias=resumo_texto,
            detalhamento_notas=detalhes_texto
        )
