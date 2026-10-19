## Estrutura do Repositório
A organização do projeto adota a divisão padrão entre dados brutos e dados processados para assegurar a imutabilidade da fonte original:

```text
barbearia-dados-pandas/
|
+-- data/
|   +-- raw/
|   |   \-- Cassio.xlsx              # Base de dados operacional bruta
|   \-- processed/
|       \-- Cassio_Tratado.xlsx      # Base final tratada e padronizada
|
+-- BG Dashboard/                    # Identidade visual e fundos para telas analíticas
|
+-- analise-e-tratamento.py          # Script principal de ingestão, limpeza e processamento
+-- README.md                        # Documentação técnica do projeto
\-- .gitignore                       # Filtro de arquivos transientes e ambientes virtuais
```
## Regras de Negócio e Etapas de Tratamento
O script analise-e-tratamento.py executa o tratamento dos dados brutos estruturado nas seguintes etapas:

## 1. Ingestão e Filtragem de Consistência
Leitura da planilha operacional localizada em data/raw/Cassio.xlsx.

Remoção de registros nulos e linhas vazias na coluna Dia Serviço, assegurando que apenas atendimentos efetivamente ocorridos permaneçam na base ativa.

## 2. Padronização Cronológica
Dia Serviço: Conversão dos carimbos de data para o padrão formal abreviado dd/mês (ex.: 01/set, 15/out), simplificando a categorização temporal por dia de atendimento.

Aniversário: Tratamento com remoção de erros de digitação e formatação no padrão formal dd/mm/aaaa, facilitando segmentações de campanhas de relacionamento com clientes.

## 3. Sanitização Textual e Nomes de Campos
Remoção de espaços em branco nas extremidades de todos os campos textuais (Quem foi ?, Nome do Cliente, Novo Cliente, Lista de Serviços, Lista de Serviço Extra, Status do Pagamento e Forma de Pagamento).

Normalização de espaçamentos e eliminação de caracteres residuais de preenchimento manual.

Padronização do nome do campo de  Novo Cliente para Novo Cliente.

## 4. Tratamento Financeiro
Conversão dos campos financeiros (Valor Avulso, ValorExtra e Valor Serviços) para formato numérico contínuo (ponto flutuante).

Tratamento de valores vazios com preenchimento zerado (0.0), impedindo falhas em cálculos agregados.

Consolidação da receita individual por comanda somando os serviços principais e extras realizados.

## 5. Formatação de Contato Telefônico
Conversão das entradas numéricas e notações decimais para strings alfanuméricas consistentes de identificador de chamada.

## 6. Preservação Estrutural
Manutenção rigorosa das colunas originais da base de dados, garantindo compatibilidade reversa com ferramentas de relatório e preservando a integridade estrutural das métricas de negócio.

## Como Executar o Projeto
Pré-requisitos
Python 3.10 ou superior instalado.

Git configurado.

## Instalação
Clone o repositório:

```Bash
git clone https://github.com/logansx-wq/projeto-barbearia-pandas.git
cd projeto-barbearia-pandas
```
Crie e ative um ambiente virtual:

```Bash
# Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate
```

Linux / macOS
```Bash
python3 -m venv venv
source venv/bin/activate
```
Instale as dependências necessárias:

```Bash
pip install pandas openpyxl
```
Execução do Script
Para processar os dados brutos e gerar a base pronta para análise:

```Bash
python analise-e-tratamento.py
```
O arquivo final estará disponível em data/processed/Cassio_Tratado.xlsx, pronto para importação e modelagem dimensional em ferramentas de BI.
