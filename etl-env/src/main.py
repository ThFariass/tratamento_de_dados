import pandas as pd
from transformations import *
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'Dataset_Pratico_ETL_Anomalias.csv')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'Dataset_Pratico_ETL_Anomalias_Corrigido.csv')

df = pd.read_csv(DATASET_PATH, sep=';', encoding='utf-8')
# 1. Ler arquivo original
#df = pd.read_csv('../data/Dataset_Pratico_ETL_Anomalias.csv', sep=';', encoding='utf-8')
# 2. Aplicar funções de tratamento em cada coluna
df['Cliente'] = df['Cliente'].apply(tratar_cliente)
df['Data_Cadastro'] = df['Data_Cadastro'].apply(tratar_data_cadastro)
df['Telefone'] = df['Telefone'].apply(tratar_telefone)
df['Email'] = df['Email'].apply(tratar_email)
df['Valor_Compra'] = df['Valor_Compra'].apply(tratar_valor_compra)
df['Status'] = df['Status'].apply(tratar_status)
df['Categoria'] = df['Categoria'].apply(tratar_categoria)
df['ID_Produto'] = df['ID_Produto'].apply(tratar_id_produto)
df['Endereco'] = df['Endereco'].apply(tratar_endereco)
df['Estado'] = df['Estado'].apply(tratar_estado)
df['CEP'] = df['CEP'].apply(tratar_cep)
df['Produto'] = df['Produto'].apply(tratar_produto)
df['Quantidade'] = df['Quantidade'].apply(tratar_quantidade)
df['Forma_Pagamento'] = df['Forma_Pagamento'].apply(tratar_forma_pagamento)
# Observacao: manter como está

# 3. Remover linhas inválidas conforme regras
df = df[df['Produto'].notnull() & (df['Produto'] != '')]
df = df[df['Status'].notnull() & (df['Status'] != '')]

# 4. Salvar arquivo limpo
#df.to_csv('../data/Dataset_Pratico_ETL_Anomalias_Corrigido.csv', sep=';', index=False, encoding='utf-8')
df.to_csv(OUTPUT_PATH, sep=';', index=False, encoding='utf-8')

print("Arquivo CSV tratado salvo em: data/dados_tratados.csv")
