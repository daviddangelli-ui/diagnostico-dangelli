import streamlit as st
import urllib.parse

st.set_page_config(page_title="DANGELLI - Diagnóstico Profissional", layout="wide")

# CABEÇALHO DE IMPACTO
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

    # NÍVEL 2: BLINDAGEM & MATURIDADE TÉCNICA (Conforme image_b6f05a.jpg + Ajuste)
    st.markdown("### 🛡️ Nível 2: Blindagem & Maturidade Técnica")
    b1 = st.select_slider("1. Há distinção formal entre Sócio e Executivo, com processos de meritocracia prevalecendo sobre a consanguinidade?", options=options)
    b2 = st.select_slider("2. O Conselho possui calendário estratégico fixo e maturidade na avaliação trimestral de desempenho?", options=options)
    b3 = st.select_slider("3. A empresa utiliza Matriz de Alçada técnica e contrata Auditoria Externa Independente anualmente?", options=options)
    b4 = st.select_slider("4. O Acordo inclui cláusulas complexas como Tag Along, Drag Along e Shotgun devidamente pactuadas?", options=options)
    b5 = st.select_slider("5. Existe um Protocolo Familiar instituído que define regras de entrada e saída de familiares na gestão?", options=options)
    b6 = st.select_slider("6. A empresa tem uma visão clara sobre sucessão e isso já está sendo planejado?", options=options)

    # NOVO NÍVEL 3: ESTRATÉGIA DO NEGÓCIO
    st.markdown("### 🚀 Nível 3: Estratégia do Negócio")
    e1 = st.select_slider("1. A empresa tem uma visão estratégica de expansão do negócio, seus marcos estratégicos e como será a captação de recursos para este crescimento?", options=options)
    e2 = st.select_slider("2. A empresa já foi assediada pelo mercado por parceiros investidores e/ou para a venda do ativo?", options=options)
    e3 = st.select_slider("3. A empresa conhece seu valor de mercado, quais são as variáveis chaves do negócio e quais os principais responsáveis pela geração de valor?", options=options)
    e4 = st.select_slider("4. A empresa tem implantado um sistema de acompanhamento mensal de indicadores operacionais, financeiros e estratégicos?", options=options)

    # NÍVEL 4: REFORMA TRIBUTÁRIA (Antigo Nível 3)
    st.markdown("### ⚖️ Nível 4: Reforma Tributária")
    t1 = st.select_slider("1. Sua equipe financeira já mapeou a transição para o novo modelo IVA (CBS/IBS)?", options=options)
    t2 = st.select_slider("2. O impacto da reforma na margem líquida operacional foi simulado para 2026-2033?", options=options)
    t3 = st.select_slider("3. Seus sistemas possuem rastreabilidade integral para aproveitamento imediate de créditos?", options=options)
    t4 = st.select_slider("4. Já existe uma estratégia de revisão de preços baseada na neutralidade do IVA?", options=options)
    t5 = st.select_slider("5. A empresa possui plano para monetização de créditos acumulados antes da transição?", options=options)
    t6 = st.select_slider("6. A empresa já realizou o VALUATION para conhecer o valor do negócio e acompanha-lo durante as mudanças da Reforma Tributária?", options=options)

    enviado = st.form_submit_button("GERAR DIAGNÓSTICO E RECEBER CONVITE MASTERCLASS")

if enviado:
    if not nome or not empresa:
        st.error("Por favor, preencha seu nome e empresa para continuar.")
    else:
        st.success("Diagnóstico concluído com sucesso!")
        
        # Consolidação de todas as notas (21 perguntas)
        resumo = (f"\n\nNOTAS DO DIAGNÓSTICO:\n"
                  f"- N1 Governança: {g1}, {g2}, {g3}, {g4}, {g5}\n"
                  f"- N2 Blindagem: {b1}, {b2}, {b3}, {b4}, {b5}, {b6}\n"
                  f"- N3 Estratégia: {e1}, {e2}, {e3}, {e4}\n"
                  f"- N4 Reforma: {t1}, {t2}, {t3}, {t4}, {t5}, {t6}")
        
        msg = f"Olá David! Sou {nome} da {empresa}. Concluí meu diagnóstico de perenidade (4 Níveis) e gostaria de receber o convite para a MasterClass.{resumo}"
        url_wa = f"https://api.whatsapp.com/send?phone=5531983984001&text={urllib.parse.quote(msg)}"
        
        st.markdown(f"### Parabéns, {nome}! Seu perfil foi mapeado nos 4 eixos estratégicos.")
        st.write("Clique no botão abaixo para enviar seus resultados e garantir sua vaga na nossa próxima MasterClass.")
        
        st.link_button("🚀 ENVIAR RESULTADOS E ACESSAR MASTERCLASS", url_wa)
        st.link_button("🔗 VER PERFIL NO LINKEDIN", "https://www.linkedin.com/in/daviddangelli/")
