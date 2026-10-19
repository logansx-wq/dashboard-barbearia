import pandas as pd

# 1. Carregar a planilha (ajuste o nome do arquivo se necessário)
caminho_arquivo = "Tela_de_dados_Tratada.xlsx"
df = pd.read_excel(caminho_arquivo, sheet_name="Tela de dados")

# 2. Localizar onde consta 'mensal' em Status ou Forma de Pagamento
mascara_mensal = (
    df["Status do Pagamento"].astype(str).str.strip().str.lower() == "mensal"
) | (
    df["Forma de Pagamento"].astype(str).str.strip().str.lower() == "mensal"
)

indices_mensais = df[mascara_mensal].index
total = len(indices_mensais)

# 3. Lista de opções para distribuir igualmente
opcoes = ["Pix", "Cartão de Débito", "Cartão de Crédito"]

# Distribuição cíclica em rodízio (1/3 para cada opção)
novas_formas = [opcoes[i % len(opcoes)] for i in range(total)]

# 4. Atualizar as colunas
df.loc[indices_mensais, "Forma de Pagamento"] = novas_formas
df.loc[indices_mensais, "Status do Pagamento"] = "Pago"

# 5. Salvar o resultado
df.to_excel("Tela_de_dados_Sem_Mensal.xlsx", index=False)

# Relatório no terminal
print(f"Total de registros alterados: {total}")
print(f"- Pix: {novas_formas.count('Pix')}")
print(f"- Cartão de Débito: {novas_formas.count('Cartão de Débito')}")
print(f"- Cartão de Crédito: {novas_formas.count('Cartão de Crédito')}")
print("\nArquivo 'Tela_de_dados_Sem_Mensal.xlsx' salvo com sucesso!")