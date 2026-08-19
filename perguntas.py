# perguntas.py
# DANGELLI - Base de Dados de Perguntas do Diagnóstico Estratégico de Maturidade

OPCOES_PADRAO = {
    "0 - Não Iniciado / Desconhecido (Risco Crítico)": 0,
    "1 - Em Discussão / Informal (Risco Alto)": 1,
    "2 - Em Mapeamento / Implementação Parcial (Risco Médio)": 2,
    "3 - Implementado, Formalizado e Monitorado (Maturidade)": 3
}

DIAGNOSTICO_CONFIG = {
    "Bloco 1: Governança, Estratégia e Acordo de Acionistas": [
        {
            "id": "gov_01",
            "pergunta": "1. O Acordo de Acionistas/Quotas possui regramento claro para quóruns de decisão sobre investimentos de capital (CAPEX) e reestruturação fiscal?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "gov_02",
            "pergunta": "2. Existe um Conselho de Administração ou Consultivo estruturado com reuniões periódicas e pautas estratégicas de transição corporativa?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "gov_03",
            "pergunta": "3. O Planejamento Estratégico de médio/longo prazo contempla cenários de transição tributária e impactos no valuation da empresa?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "gov_04",
            "pergunta": "4. A empresa possui uma Matriz de Riscos Corporativos (ERM) e diretrizes de Compliance formalizadas e auditadas?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "gov_05",
            "pergunta": "5. A estrutura de liderança executiva (C-Level) possui autonomia e metas (OKRs/KPIs) atreladas à eficiência operacional e fiscal?",
            "opcoes": OPCOES_PADRAO
        }
    ],
    "Bloco 2: CAPEX, Operações, Contratos & Cláusula de Hardship": [
        {
            "id": "ope_01",
            "pergunta": "6. Os contratos plurianuais B2B (com clientes e fornecedores) possuem cláusulas específicas de Hardship / Reequilíbrio Econômico-Financeiro?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "ope_02",
            "pergunta": "7. A gestão de CAPEX possui metodologia de aprovação de projetos com avaliação de retorno considerando o aproveitamento de créditos fiscais?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "ope_03",
            "pergunta": "8. Existe mapeamento do impacto da reforma tributária sobre a aquisição de máquinas, equipamentos e estoque de insumos industriais?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "ope_04",
            "pergunta": "9. A empresa aplica metodologias de eficiência operacional (Lean, Six Sigma ou TOC) para redução de gargalos e estoques intermediários?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "ope_05",
            "pergunta": "10. Os processos fabris e contratuais atendem aos requisitos de certificações ISO e exigências ESG de grandes contratantes?",
            "opcoes": OPCOES_PADRAO
        }
    ],
    "Bloco 3: Finanças, ERP & Split Payment (Impacto de Caixa)": [
        {
            "id": "fin_01",
            "pergunta": "11. O sistema ERP atual está mapeado e em fase de adequação/homologação técnica para o recolhimento automático do Split Payment (IBS/CBS)?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "fin_02",
            "pergunta": "12. Foi realizado estudo de impacto do retenção do Split Payment sobre o Capital de Giro e a liquidez imediata da tesouraria?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "fin_03",
            "pergunta": "13. A empresa possui estratégia definida para acompanhamento e ressarcimento de saldos credores acumulados dos novos tributos?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "fin_04",
            "pergunta": "14. A apuração de custos e margens de contribuição utiliza modelagem que separa o efeito do IVA não-cumulativo dos custos operacionais?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "fin_05",
            "pergunta": "15. O planejamento orçamentário anual (Orçado x Realizado) possui simulações para a fase de transição e alíquotas do IBS/CBS?",
            "opcoes": OPCOES_PADRAO
        }
    ],
    "Bloco 4: Comercial, Precificação, Margem & Pessoas/RH": [
        {
            "id": "com_01",
            "pergunta": "16. A política de precificação (Pricing) foi revisada para neutralizar o impacto das alíquotas do IBS/CBS nas propostas comerciais B2B?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "com_02",
            "pergunta": "17. A equipe comercial e de vendas está treinada para negociar o repasse fiscal e apresentar a Proposta de Valor sem perda de margem?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "com_03",
            "pergunta": "18. Há monitoramento contínuo sobre os reflexos das alterações tributárias na folha de pagamento e nos custos diretos de mão de obra?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "com_04",
            "pergunta": "19. O Plano de Cargos, Salários e Competências da empresa está alinhado com a retórica de retenção de talentos estratégicos?",
            "opcoes": OPCOES_PADRAO
        },
        {
            "id": "com_05",
            "pergunta": "20. O modelo de vendas contempla avaliação do grau de dependência da carteira em relação aos maiores clientes e fornecedores do setor?",
            "opcoes": OPCOES_PADRAO
        }
    ]
}
