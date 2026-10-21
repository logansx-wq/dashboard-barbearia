# Dashboard de Inteligência Operacional e Gerencial para Barbearia

## Objetivo

Solução integrada de Business Intelligence e Engenharia de Dados voltada para a gestão de uma barbearia em expansão. O objetivo central é unificar registros operacionais fragmentados em uma base analítica consistente, viabilizando o monitoramento contínuo da saúde financeira, produtividade da equipe, comportamento da base de clientes e controle de inventário por meio de dashboards interativos no Power BI.

---

## A Necessidade do Negócio

O proprietário da barbearia enfrentava dificuldades na tomada de decisão devido à ausência de relatórios consolidados em tempo real:

* **Incerteza Financeira:** Dificuldade em apurar com exatidão o faturamento bruto, custos operacionais, margem líquida real e a dependência de cada método de pagamento (Pix, cartões e dinheiro).
* **Gestão e Comissionamento de Parceiros:** Falta de automatização no cálculo das comissões devidas aos profissionais e na mensuração da margem retida pela empresa.
* **Acompanhamento de Metas e Produtividade:** Inexistência de métricas objetivas para acompanhar o alcance de metas individuais e a cadência média diária de atendimentos.
* **Controle Crítico de Estoque:** Descontrole na reposição de insumos essenciais de bancada (lâminas, golas) e itens de revenda, gerando rupturas operacionais ou imobilização excessiva de capital de giro.
* **Eficácia Promocional e Retenção:** Ausência de dados para medir a taxa de atração de novos clientes versus retenção de clientes recorrentes, além do impacto dos descontos concedidos.

---

## Solução Desenvolvida

A solução foi concebida de ponta a ponta: desde a sanitização e tratamento estrutural dos dados transacionais via Python (Pandas) até a modelagem dimensional e construção das interfaces analíticas no Power BI.

O dashboard gerencial organiza-se em cinco módulos principais:

### 1. Navegação 
Interface central para alternância ágil entre os pilares estratégicos de gestão: Financeiro, Metas de Equipe, Clientes e Estoque.
<img width="1024" height="568" alt="image" src="https://github.com/user-attachments/assets/30ee2bb4-9437-4e8a-a2bb-d93ecea6711a" />

### 2. Raio-X Financeiro e Executivo
Painel voltado para a saúde de caixa e lucratividade:
* Apuração do Faturamento Bruto, Total de Gastos, Lucro Líquido, Ticket Médio e Margem Líquida.
* Gráfico tipo velocímetro para acompanhamento de faturamento acumulado versus meta global.
* Distribuição de receita por método de liquidação (Pix, Cartão de Débito, Cartão de Crédito, Mensal e Dinheiro).
* Tendência de faturamento entre períodos contábeis.
<img width="1024" height="579" alt="image" src="https://github.com/user-attachments/assets/77b1e214-900d-4fbb-9731-6ec039a6d654" />


### 3. Performance e Gestão de Equipe
Painel para avaliação de produtividade e transparência no comissionamento:
* Total de atendimentos e média de atendimentos diários por profissional.
* Cálculo automático das comissões devidas e do volume retido pela barbearia.
* Comparativo individual entre faturamento alcançado e meta estabelecida.
* Matriz de representatividade do mix de serviços prestados por cada barbeiro.
<img width="1024" height="568" alt="image" src="https://github.com/user-attachments/assets/233e1b40-e1c2-4216-b82f-8b88dfccc224" />


### 4. Clientes, Campanhas e Descontos
Módulo dedicado ao comportamento da carteira de clientes:
* Relação entre clientes únicos atendidos e aquisição de novos clientes (taxa de novos clientes).
* Volume total de descontos concedidos e taxa de desconto efetivo sobre a receita.
* Retorno e adesão por modalidade de campanha promocional (Aniversariante, Combos, Primeira Visita e Planos Mensalistas).
<img width="1024" height="558" alt="image" src="https://github.com/user-attachments/assets/fa34e2d6-3e8c-4d2c-8c41-c4e8867eba23" />


### 5. Gestão de Estoque e Reposição
Painel voltado para mitigação de rupturas e controle de giro:
* Identificação visual com alertas de reposição urgente para itens em nível crítico ou no limite do estoque mínimo.
* Segmentação do capital imobilizado a custo por categoria (Revenda, Insumos de Bancada e Químicos).
* Projeção do potencial de faturamento do inventário disponível.
<img width="1024" height="572" alt="image" src="https://github.com/user-attachments/assets/6e2fac15-7386-48cb-9c9c-bea3be757cc6" />

---
