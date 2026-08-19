import streamlit as st
import pandas as pd
import plotly.express as px
from perguntas import DIAGNOSTICO_CONFIG

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="DANGELLI Hub - Maturidade 2026", layout="wide")

# --- FUNÇÃO DE APOIO: WHATSAPP E PRÓXIMOS PASSOS ---
def oferecer_proximos_passos(nome, empresa, tipo_diag, resumo_medias, detalhamento_notas):
    st.divider()
    st.subheader("🎓 Próximos Passos: DANGELLI Advisory")
    st.write(f"Parabéns, **{nome}**! Você deu o passo fundamental para a perenidade da **{empresa}**.")
    
    # Formatação da mensagem para o WhatsApp
    texto_wa = (
        f"DIAGNÓSTICO_DANGELLI_{tipo_diag}%0A"
        f"👤 Nome: {nome}%0A"
        f"🏢 Empresa: {empresa}%0A%0A"
        f"📊 MÉRITAS COM CADA BLOCO:%0A{resumo_medias}%0A%0A"
        f"📌 DETALHAMENTO DE NOTAS:%0A{detalhamento_notas}%0A%0A"
        f"🚀 Aguardo análise técnica da equipe DANGELLI."
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 **Análise de Governança:** Envie o relatório detalhado diretamente para nossa equipe de conselheiros.")
        link_wa = f"https://wa.me/5531983984001?text={texto_wa}"  # Atualizar número se necessário
        st.markdown(f'[![Enviar no WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)]({link_wa})')

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
st.title("🛡️ DANGELLI - Diagnóstico Corporativo")

# Formulário de Identificação
col_a, col_b = st.columns(2)
with col_a:
    nome_usuario = st.text_input("Responsável Técnico / Avaliador:", key="resp_tec")
with col_b:
    empresa_usuario = st.text_input("Empresa / Organização:", key="emp_nome")

st.divider()

# --- CARREGAMENTO DAS PERGUNTAS ---
# Caso selecione a opção 3, carrega a matriz completa de 82 perguntas de perguntas.py
if opcao_diagnostico == "3. Diagnóstico Estratégico Master (82 Questões)":
    config_atual = DIAGNOSTICO_CONFIG
else:
    # Mantém estrutura simplificada para diagnósticos 1 e 2 caso selecione os anteriores
    config_atual = DIAGNOSTICO_CONFIG

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
            
        # Média do bloco
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
        
        # Dashboard de Indicadores
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
            resumo_texto += f"- {bloco}: {media:.2f} / 3.0%0A"
            
        detalhes_texto = ""
        for perg, nota in list(respostas.items())[:10]: # Envia resumo das primeiras notas
            detalhes_texto += f"• {perg[:40]}... = Nota {nota}%0A"

        oferecer_proximos_passos(
            nome=nome_usuario,
            empresa=empresa_usuario,
            tipo_diag=opcao_diagnostico.replace(" ", "_"),
            resumo_medias=resumo_texto,
            detalhamento_notas=detalhes_texto
        )
