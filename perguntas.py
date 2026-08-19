# perguntas.py
# DANGELLI - Base de Dados dos Diagnósticos Corporativos

OPCOES_PADRAO = {
    "0 - Não Iniciado / Desconhecido (Risco Crítico)": 0,
    "1 - Em Discussão / Informal (Risco Alto)": 1,
    "2 - Em Mapeamento / Implementação Parcial (Risco Médio)": 2,
    "3 - Implementado, Formalizado e Monitorado (Maturidade)": 3
}

DIAGNOSTICO_MASTER = {
    "BLOCO 1: Governança Corporativa, Proteção Patrimonial e Sucessão": [
        {"id": "b1_01", "pergunta": "1. Existe um Acordo de Sócios formalizado?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_02", "pergunta": "2. Há um plano de sucessão definido (natural ou por morte)?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_03", "pergunta": "3. Patrimônio pessoal é separado do da empresa?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_04", "pergunta": "4. Existe conselho consultivo independente?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_05", "pergunta": "5. Existe um programa de Formação de Sucessores?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_06", "pergunta": "6. Existem regras definidas para exclusão da sociedade?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_07", "pergunta": "7. Existe uma política de distribuição de lucros?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_08", "pergunta": "8. Possui holding patrimonial para o negócio e também para cada acionista?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_09", "pergunta": "9. Possui Acordo de Acionistas para o negócio e para cada acionista?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_10", "pergunta": "10. Possui seguro para proteção dos ativos contra riscos cíveis?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_11", "pergunta": "11. Possui seguro contratado para questões de sucessão?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_12", "pergunta": "12. Possui seguro D&O para proteção dos Diretores e Administradores?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_13", "pergunta": "13. Possui regras para impenhorabilidade nos bens?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_14", "pergunta": "14. A empresa fez seu Valuation recente para conhecer o valor das cotas dos sócios em caso de necessidade?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_15", "pergunta": "15. Já cogitaram venda e/ou a empresa já recebeu assédio do mercado interessado em comprar o ativo ou sociedade?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_16", "pergunta": "16. A empresa já instituiu um Comitê de transição interno para acompanhar as ações e a sustentabilidade do negócio?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_17", "pergunta": "17. Foram feitas simulações sobre reestruturação societária (cisão, PJ operacional/patrimonial) diante das alterações do IRPJ/CSLL?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_18", "pergunta": "18. O Comitê de Transição possui regimento interno formal, matriz de alçadas para aprovar investimentos e reporte direto ao Conselho?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_19", "pergunta": "19. A transição da Reforma foi incorporada às metas (OKRs/KPIs) e à remuneração variável das diretorias executivas?", "opcoes": OPCOES_PADRAO},
        {"id": "b1_20", "pergunta": "20. O Conselho atual mapeou os riscos de responsabilidade civil, fiscal e sanitização de passivos legados durante a transição?", "opcoes": OPCOES_PADRAO}
    ],
    "BLOCO 2: Estratégia de Negócios, Contratos e Cadeia de Valor": [
        {"id": "b2_01", "pergunta": "1. Possui planejamento estratégico com mapa estratégico, iniciativas, objetivos e metas para os próximos 5 anos?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_02", "pergunta": "2. A empresa já está se preparando para a transição multidisciplinar exigida pela Reforma Tributária?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_03", "pergunta": "3. Sabe de onde buscará recursos para a estratégia de crescimento (recursos próprios, do mercado ou acionista externo)?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_04", "pergunta": "4. Os atuais contratos de longo prazo protegem sua margem contra aumentos de alíquota da reforma tributária?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_05", "pergunta": "5. Mapeou quais fornecedores da sua cadeia se tornarão 'tóxicos' por não gerarem os créditos tributários necessários?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_06", "pergunta": "6. Sua logística é desenhada para eficiência real ou depende de incentivos fiscais estaduais que deixarão de existir?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_07", "pergunta": "7. Existe um plano de renegociação ativo com seus parceiros estratégicos antes da entrada em vigor da reforma?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_08", "pergunta": "8. A integração com fornecedores permite visibilidade em tempo real para garantir que o crédito tributário flua no capital de giro?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_09", "pergunta": "9. Existem ações estratégicas alinhadas com as necessidades da Reforma Tributária?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_10", "pergunta": "10. Foram mapeados, priorizados e revistos os contratos em execução que persistirão durante o período de transição (2027 a 2033)?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_11", "pergunta": "11. Nos novos contratos, foram revistas cláusulas de pagamento, responsabilidades fiscais e resolução de disputas?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_12", "pergunta": "12. Foram feitos estudos sobre enquadramento em regimes específicos e/ou diferenciados de tributação instituídos pela reforma?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_13", "pergunta": "13. Foram realizados estudos sobre a viabilidade econômica com o deslocamento da arrecadação da origem para o destino?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_14", "pergunta": "14. Analisou logística operacional, CDs, lojas físicas/virtuais e marketplaces diante da extinção dos benefícios fiscais estaduais?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_15", "pergunta": "15. Mapeou o regime de apuração dos fornecedores visando o aproveitamento de créditos de IBS/CBS e limitações do Simples Nacional?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_16", "pergunta": "16. Mapeou quantos contratos com fornecedores terão que ser renegociados para assegurar a opção pelo regime regular do IBS/CBS?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_17", "pergunta": "17. Realizou simulações do impacto econômico em bens e serviços submetidos à isenção, alíquota zero ou imunidade quanto aos créditos?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_18", "pergunta": "18. Avaliou o timing ideal para a compra de grandes máquinas e expansões industriais (CAPEX) frente ao aproveitamento do IVA a partir de 2027?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_19", "pergunta": "19. Como planeja adaptar a aquisição de insumos críticos e o uso de regimes suspensivos (Drawback, RECOF) às regras do IVA Dual?", "opcoes": OPCOES_PADRAO},
        {"id": "b2_20", "pergunta": "20. Qual é o plano de mitigação para a perda gradual de benefícios fiscais estaduais sobre os quais se assenta a margem operacional?", "opcoes": OPCOES_PADRAO}
    ],
    "BLOCO 3: Gestão Financeira, Capacidade de Caixa e Tecnologia (ERP)": [
        {"id": "b3_01", "pergunta": "1. Realiza reuniões mensais para acompanhamento de indicadores, DRE, Balanço e monitoramento do EBITDA?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_02", "pergunta": "2. Entende e acompanha as variáveis-chave responsáveis pela geração de valor do negócio?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_03", "pergunta": "3. Seu fluxo de caixa suporta o impacto de demora na recuperação de créditos tributários durante a fase de transição?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_04", "pergunta": "4. Existe projeção do aumento da Necessidade de Capital de Giro (NCG) com a Reforma Tributária?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_05", "pergunta": "5. Tem clareza absoluta sobre quais margens de contribuição de produtos do portfólio passarão a dar prejuízo sob novas alíquotas?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_06", "pergunta": "6. Sua gestão financeira é preditiva, antecipando cenários de impacto no EBITDA, ou apenas reativa?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_07", "pergunta": "7. Existe um orçamento reservado especificamente para o custo de conformidade (sistemas, consultorias, treinamentos) da transição?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_08", "pergunta": "8. Está gerindo a empresa olhando para o faturamento bruto ou tem controle sobre a margem de contribuição líquida pós-impostos?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_09", "pergunta": "9. Seu ERP é um ativo estratégico com inteligência fiscal ou uma âncora para calcular impostos na nova regra?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_10", "pergunta": "10. Confia 100% na qualidade dos dados cadastrais atuais para evitar perda imediata de margem ou multas no novo sistema?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_11", "pergunta": "11. Sua empresa está investindo em automação para lidar com a burocracia da transição ou inchará a folha de pagamento?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_12", "pergunta": "12. A tecnologia utilizada permite simular cenários tributários em tempo real para apoiar decisões de preço e compra?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_13", "pergunta": "13. Está modernizando seus processos digitais ou apenas digitalizando burocracia antiga sem ganho de eficiência?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_14", "pergunta": "14. Setores de orçamento, compras, comercial, contábil e fiscal atuam integrados? O ERP já foi parametrizado ao Padrão NFS-e?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_15", "pergunta": "15. Foram mapeados os reflexos de caixa, margem e risco em virtude das alterações da tributação sobre o consumo?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_16", "pergunta": "16. Realizou análises sobre a possibilidade de cisão ou segregação de atividades complementares para otimizar o ciclo de crédito?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_17", "pergunta": "17. Foram mapeados os reflexos no preço considerando a convivência simultânea dos regimes durante a transição?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_18", "pergunta": "18. Analisou impactos no fluxo de caixa pelo recolhimento antecipado de IBS/CBS em adiantamentos e faturamento sem recebimento?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_19", "pergunta": "19. Analisou a viabilidade de alteração do regime de apuração do IRPJ/CSLL diante do maior creditamento do IVA?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_20", "pergunta": "20. Realizou simulações quanto ao impacto em bens e serviços submetidos a saída imune, isenta ou alíquota zero e glosa de créditos?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_21", "pergunta": "21. Realizou simulações quanto ao aproveitamento imediato de créditos de CBS sobre compras de ativos imobilizados a partir de 2027?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_22", "pergunta": "22. Realizou análises sobre o aproveitamento de crédito presumido sobre o estoque de bens materiais existente em 1º de janeiro de 2027?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_23", "pergunta": "23. Foi realizado planejamento estratégico para assegurar a melhor destinação aos créditos acumulados de ICMS, PIS e COFINS?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_24", "pergunta": "24. Qual é a estratégia de tesouraria para suportar o impacto no caixa pela retenção via Split Payment diante dos prazos da indústria?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_25", "pergunta": "25. Possui ferramentas automáticas para checar adimplência e regularidade fiscal de fornecedores evitando glosa de créditos?", "opcoes": OPCOES_PADRAO},
        {"id": "b3_26", "pergunta": "26. Existe um plano de saneamento de litígios e passivos fiscais legados para impedir travas nas compensações automáticas?", "opcoes": OPCOES_PADRAO}
    ],
    "BLOCO 4: Mercado (Comercial/Marketing) e Governança de Capital Humano": [
        {"id": "b4_01", "pergunta": "1. A Proposta de Valor é forte o suficiente para justificar seu preço quando as alíquotas mudarem no mercado?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_02", "pergunta": "2. Sua equipe comercial sabe explicar ao cliente por que o preço mudou sem usar desculpas genéricas que enfraquecem a marca?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_03", "pergunta": "3. Conhece a elasticidade de preço do seu cliente para saber até onde pode repassar novos custos sem destruir a demanda?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_04", "pergunta": "4. A estratégia de canais está preparada para a equalização das cargas tributárias ou depende de brechas regionais?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_05", "pergunta": "5. Monitora seus concorrentes para saber se usarão a reforma tributária para ganhar market share agressivamente sobre sua base?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_06", "pergunta": "6. A equipe atual tem capacidade técnica para operar dois sistemas tributários simultâneos sem colapso ou burnout?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_07", "pergunta": "7. Está preparado para reter talentos fiscais e financeiros durante a escassez de profissionais qualificados no mercado?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_08", "pergunta": "8. A cultura da sua empresa incentiva a adaptação rápida e o aprendizado contínuo?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_09", "pergunta": "9. Existe um plano de treinamento robusto para capacitar a empresa sobre como os impostos impactam o negócio a partir de agora?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_10", "pergunta": "10. Suas lideranças estão prontas para conduzir a equipe através da incerteza do período de transição?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_11", "pergunta": "11. Já treinou sua equipe de gestão e operacional sobre as novas regras pós-reforma tributária?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_12", "pergunta": "12. Mapeou os impactos da impossibilidade de crédito de IBS/CBS sobre folha de pagamento vs. creditamento em serviços contratados de PJ?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_13", "pergunta": "13. Mapeou os clientes que promoverão retenção e recolhimento de IBS/CBS via Split Payment e o impacto disso no fluxo de caixa?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_14", "pergunta": "14. A equipe comercial foi treinada para negociar preços na base líquida (Net Price), demonstrando o ganho de crédito ao comprador?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_15", "pergunta": "15. Os contratos de fornecimento de longo prazo possuem cláusulas de revisão por imprevisto tributário (hardship)?", "opcoes": OPCOES_PADRAO},
        {"id": "b4_16", "pergunta": "16. Simulou a posição competitiva dos concorrentes (nacionais vs. importadores) quanto a ganhos de margem no IVA?", "opcoes": OPCOES_PADRAO}
    ]
}

# Diagnóstico 1: Filtra as primeiras 5 perguntas essenciais de cada bloco (20 perguntas)
DIAGNOSTICO_1 = {bloco: lista[:5] for bloco, lista in DIAGNOSTICO_MASTER.items()}

# Diagnóstico 2: Filtra as primeiras 10 perguntas de transição de cada bloco (40 perguntas)
DIAGNOSTICO_2 = {bloco: lista[:10] for bloco, lista in DIAGNOSTICO_MASTER.items()}
