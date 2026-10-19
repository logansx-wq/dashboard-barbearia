# Pipeline de Tratamento de Dados Operacionais - Barbearia

## Visao Geral

Este projeto consiste no desenvolvimento de uma pipeline de engenharia e tratamento de dados operacionais de uma barbearia, utilizando a biblioteca Pandas em Python. O objetivo principal e realizar a limpeza, padronizacao estrutural e preparacao analitica dos registros transacionais de adimentos, permitindo que a base de dados tratada alimente dashboards no Power BI e relatorios executivos com consistencia e contenfiabilidade.

## Estrutura do Repositorio

A organizacao do projeto adota a divisao padrão entre dados brutos e dados processados para assegurar a imutabilidade da fonte original:

```text
barbearia-dados-pandas/
│
├── data/
│   ├── raw/
│   │   └── Cassio.xlsx              # Base de dados operacional bruta
│   └── processed/
│       └── Cassio_Tratado.xlsx      # Base final tratada e padronizada
│
├── BG Dashboard/                    # Identidade visual e fundos para telas analiticas
│
├── analise-e-tratamento.py          # Script principal de ingestao, limpeza e processamento
├── README.md                        # Documentacao tecnica do projeto
└── .gitignore                       # Filtro de arquivos transientes e ambientes virtuais

```
Regras de Negocio e Etapas de Tratamento
O script analise-e-tratamento.py executa o tratamento dos dados brutos estruturado nas seguintes etapas:

1. Ingestao e Filtragem de Consistencia
Leitura da planilha operacional localizada em data/raw/Cassio.xlsx.

Remocao de registros nulos e linhas vazias na coluna Dia Servico, assegurando que apenas atendimentos efetivamente ocorridos permaneçam na base ativa.

2. Padronizacao Cronologica
Dia Servico: Conversao dos carimbos de data para o padrao formal abreviado dd/mes (ex.: 01/set, 15/out), simplificando a categorizacao temporal por dia de atendimento.

Aniversario: Tratamento com remocao de erros de digitacao e formatacao no padrao padronizado dd/mm/aaaa, facilitando segmentacoes de campanhas de relacionamento com clientes.

3. Sanitizacao Textual e Nomes de Campos
Remocao de espacos em branco nas extremidades de todos os campos textuais (Quem foi ?, Nome do Cliente, Novo Cliente, Lista de Servicos, Lista de Servico Extra, Status do Pagamento e Forma de Pagamento).

Normalizacao de espacamentos e eliminacao de caracteres residuais de preenchimento manual.

Padronizacao do nome do campo de  Novo Cliente para Novo Cliente.

4. Tratamento Financeiro
Conversao dos campos financeiros (Valor Avulso, ValorExtra e Valor Servicos) para formato numerico continuo (ponto flutuante).

Tratamento de valores vazios com preenchimento zerado (0.0), impedindo falhas em calculos agregados.

Consolidacao da receita individual por comanda somando os servicos principais e extras realizados.

5. Formatacao de Contato Telefonico
Conversao das entradas numericas e notacoes decimais para strings alfanumericas consistentes de identificador de chamada.

6. Preservacao Estrutural
Manutencao rigorosa das colunas originais da base de dados, garantindo compatibilidade reversa com ferramentas de relatorio e preservando a integridade estrutural das metricas de negocio.

Como Executar o Projeto
Pre-requisitos
Python 3.10 ou superior instalado.

Git configurado.

Instalacao
Clone o repositorio:

Bash
git clone [https://github.com/logansx-wq/projeto-barbearia-pandas.git](https://github.com/logansx-wq/projeto-barbearia-pandas.git)
cd projeto-barbearia-pandas
Crie e ative um ambiente virtual (recomendado):

Bash
# Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
Instale as dependencias necessarias:

Bash
pip install pandas openpyxl
Execucao do Script
Para processar os dados brutos e gerar a base pronta para analise:

Bash
python analise-e-tratamento.py
O arquivo final estara disponivel em data/processed/Cassio_Tratado.xlsx, pronto para importacao e modelagem dimensional em ferramentas de BI.
