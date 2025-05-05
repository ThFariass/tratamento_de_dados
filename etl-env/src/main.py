import pandas as pd
from transformations import tratar_cliente

# 1. Ler arquivo original
df = pd.read_csv('../data/Dataset_Pratico_ETL_Anomalias_Corrigido.csv', sep=';', encoding='utf-8')

# 2. Aplicar funções de tratamento em cada coluna
df['Cliente'] = df['Cliente'].apply(tratar_cliente)

# Observacao: manter como está

# 3. Remover linhas inválidas conforme regras (exemplo: produto vazio, status vazio)
df = df[df['Produto'].notnull() & (df['Produto'].str.lower() != 'n/a')]
df = df[df['Status'].notnull() & (df['Status'] != '')]

# 4. Salvar arquivo limpo
df.to_csv('../data/dados_tratados.csv', sep=';', index=False, encoding='utf-8')
