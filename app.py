import streamlit as st
import urllib.parse

st.set_page_config(page_title="DANGELLI - Diagnóstico Profissional", layout="wide")

# CABEÇALHO DE IMPACTO (Baseado no seu Print 1)
st.markdown("""# O que garante a **perenidade** de uma média empresa em tempos de transformações profundas?""")
st.info("""Governança e Estratégia precisam estar completamente integradas sempre na moderna visão da perenidade dos negócios. Isso torna-se mais crítico agora com a chegada da Reforma Tributária.""")

with st.form("diagnostico_dangelli"):
    nome = st.text_input("Seu Nome Completo")
    empresa = st.text_input("Sua Empresa")

    # NÍVEL 1: GOVERNANÇA (Conforme image_b6efff.png)
    st.markdown("### 🏛️ Nível 1: Fundamentos da Governança")
    options = ["Inexistente", "2", "3", "4", "Pleno"]
    g1 = st.select_slider("1. Sua empresa possui um Acordo de Sócios formalizado e atualizado?", options=options)
    g2 = st.select_slider("2. Existe um plano de sucessão estruturado para posições-chave?", options=options)
    g3 = st.select_slider("3. Há uma separação rigorosa entre contas pessoais (PF) e empresariais (PJ)?", options=options)
    g4 = st.select_slider("4. A empresa conta com um Conselho Consultivo ou Administrativo ativo?", options=options)
    g5 = st.select_slider("5. Os processos de tomada de decisão estratégica são documentados e colegiados?", options=options)

    # NÍVEL 2: BLINDAGEM & MATURIDADE TÉCNICA (Conforme image_b6f05a.jpg)
    st.markdown("### 🛡️ Nível 2: Blindagem & Maturidade Técnica")
    b1 = st.select_slider("1. Há distinção formal entre Sócio e Executivo, com processos de meritocracia prevalecendo sobre a consanguinidade?", options=options)
    b2 = st.select_slider("2. O Conselho possui calendário estratégico fixo e maturidade na avaliação trimestral de desempenho?", options=options)
    b3 = st.select_slider("3. A empresa utiliza Matriz de Alçada técnica e contrata Auditoria Externa Independente anualmente?", options=options)
    b4 = st.select_slider("4. O Acordo inclui cláusulas complexas como Tag Along, Drag Along e Shotgun devidamente pactuadas?", options=options)
    b5 = st.select_slider("5. Existe um Protocolo Familiar instituído que define regras de entrada e saída de familiares na gestão?", options=options)

    # NÍVEL 3: REFORMA TRIBUTÁRIA (Conforme image_b6f324.jpg)
    st.markdown("### ⚖️ Nível 3: Reforma Tributária")
    t1 = st.select_slider("1. Sua equipe financeira já mapeou a transição para o novo modelo IVA (CBS/IBS)?", options=options)
    t2 = st.select_slider("2. O impacto da reforma na margem líquida operacional foi simulado para 2026-2033?", options=options)
    t3 = st.select_slider("3. Seus sistemas possuem rastreabilidade integral para aproveitamento imediato de créditos?", options=options)
    t4 = st.select_slider("4. Já existe uma estratégia de revisão de preços baseada na neutralidade do IVA?", options=options)
    t5 = st.select_slider("5. A empresa possui plano para monetização de créditos acumulados antes da transição?", options=options)

    enviado = st.form_submit_button("GERAR DIAGNÓSTICO E RECEBER CONVITE MASTERCLASS")

if enviado:
    if not nome or not empresa:
        st.error("Por favor, preencha seu nome e empresa para continuar.")
    else:
        st.success("Diagnóstico concluído com sucesso!")
        
        # Consolidação das Notas para o David
        resumo = (f"\n\nNOTAS DO DIAGNÓSTICO:\n"
                  f"- Governança: {g1}, {g2}, {g3}, {g4}, {g5}\n"
                  f"- Blindagem: {b1}, {b2}, {b3}, {b4}, {b5}\n"
                  f"- Reforma: {t1}, {t2}, {t3}, {t4}, {t5}")
        
        msg = f"Olá David! Sou {nome} da {empresa}. Concluí meu diagnóstico de perenidade e gostaria de receber o convite para a MasterClass.{resumo}"
        url_wa = f"https://api.whatsapp.com/send?phone=5531983984001&text={urllib.parse.quote(msg)}"
        
        st.markdown(f"### Parabéns, {nome}! Seu perfil foi mapeado.")
        st.write("Clique no botão abaixo para enviar seus resultados e garantir sua vaga na nossa próxima MasterClass sobre Perenidade e Reforma Tributária.")
        
        st.link_button("🚀 ENVIAR RESULTADOS E ACESSAR MASTERCLASS", url_wa)
        st.link_button("🔗 VER PERFIL NO LINKEDIN", "https://www.linkedin.com/in/daviddangelli/")
