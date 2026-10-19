import pandas as pd
import numpy as np

# 1. Carrega a planilha original
caminho_arquivo = "Cassio.xlsx"
df = pd.read_excel(caminho_arquivo, sheet_name="Tela de dados")

# Guardar a lista exata e a ordem das colunas originais
colunas_originais = df.columns.tolist()

# 2. Filtra apenas as linhas preenchidas na coluna "Dia Serviço"
df = df.dropna(subset=["Dia Serviço"]).copy()

# ----------------------------------------------------
# 3. Tratamento e Padronização de Datas
# ----------------------------------------------------
meses_pt = {
    1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6: 'jun',
    7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'
}

def formatar_dia_servico(val):
    if pd.isna(val):
        return np.nan
    dt = pd.to_datetime(val, errors='coerce')
    if pd.isna(dt):
        return str(val).strip()
    return f"{dt.strftime('%d')}/{meses_pt[dt.month]}"

def formatar_aniversario(val):
    if pd.isna(val):
        return np.nan
    dt = pd.to_datetime(val, errors='coerce')
    if pd.isna(dt):
        return np.nan
    return dt.strftime('%d/%m/%Y')

# Formata a coluna "Dia Serviço" (dd/mmm) e a coluna "Aniversário" (dd/mm/aaaa)
df["Dia Serviço"] = df["Dia Serviço"].apply(formatar_dia_servico)
df["Aniversário"] = df["Aniversário"].apply(formatar_aniversario)

# ----------------------------------------------------
# 4. Limpeza de Espaços em Branco nas Colunas de Texto
# ----------------------------------------------------
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].apply(lambda x: str(x).strip() if pd.notna(x) and not isinstance(x, (int, float)) else x)
    df[col] = df[col].replace(["nan", "None", ""], np.nan)

# ----------------------------------------------------
# 5. Mantem a ordem das colunas do arquivo original
# ----------------------------------------------------
df_tratado = df[colunas_originais].copy()

# 6. Salva em um novo arquivo Excel
nome_saida = "Tela_de_dados_Tratada.xlsx"
df_tratado.to_excel(nome_saida, index=False)

print(f"Sucesso! Arquivo '{nome_saida}' gerado com todas as {len(colunas_originais)} colunas originais preservadas.")