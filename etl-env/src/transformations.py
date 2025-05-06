import pandas as pd
import phonenumbers
from dateutil.parser import parse
import re

def tratar_cliente(nome: str) -> str:
    """Remove prefixos como 'Sr.', 'Sra.', 'Dr.', 'Dra.', 'srta.', 'sr', 'dr.' (independente de
maiusculas/minusculas e presença de ponto) e padroniza o nome da capitalização correta"""
    if pd.isnull(nome) or not isinstance(nome, str):
        return ''
    nome = nome.strip()
    #Remove prefixos do inicio, ignorando maiusculas/minusculas e ponto
    nome = re.sub(r'^(sr\.?|sra\.?|srta\.?|dr\.?|dra\.?)\s+', '', nome, flags=re.IGNORECASE)
    #Padroniza para a primeira letra ser maiuscula em cada nome
    return nome.title()

def tratar_data_cadastro(data_str: str) -> pd.Timestamp:
    """Converte string para data, aceitando formatos variados. 
    Retorna pd.NaT se não conseguir converter"""
    if pd.isnull(data_str) or not isinstance(data_str, str):
        return ''
    try:
        #dayfisrt=True considera dia antes do mês
        return parse(data_str, dayfirst=True)
    except Exception:
        return dt.strftime('%d/%m/%Y')

def tratar_telefone(numero: str) -> str:
    """Formata numeros para o padrão brasileiro (xx) XXXX-XXXX.
    se não for reconhecido, retorna 'telefone invalido' """
    if pd.isnull(numero) or not isinstance(numero, str):
        return 'telefone inválido'
    try:
        phone = phonenumbers.parse(numero, "BR")
        if phonenumbers.is_valid_number(phone):
            return phonenumbers.format_number(
                phone,
                phonenumbers.PhoneNumberFormat.NATIONAL
            )
        return "Telefone inválido"
    except:
        return "Telefone Inválido"

def tratar_email(email: str) -> str:
    """Valida o formato do email. se invalido, retorna 'Email Invalido"""
    if pd.isnull(email) or not isinstance (email, str):
        return "Email Invalido"
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(regex, email.strip()):
        return email.strip().lower()
    else:
        return "Email Inválido"

def tratar_valor_compra(valor: str) -> float:
    """Padrozina o separador decimal e converte para float. 
    Se não conseguir, retorna 0.0"""
    if pd.isnull(valor):
        return 0.0
    valor = str(valor).replace(',','.')
    try:
        return float(valor)
    except: 0.0

def tratar_status(status: str) -> str:
    """Padroniza os status para: Ativo, Inativo, em analise.
    Retorna string vazia se não for reconhecido"""

    if pd.isnull(status) or status.strip() == '':
        return ''
    status = status.strip().lower()
    if status == 'ativo':
        return 'Ativo'
    elif status == 'inativo':
        return 'inativo'
    elif status == ['em análise', 'em analise']:
        return 'Em análise'
    else:
        return ''
    
def tratar_categoria(cat: str)-> str:
    """corrige inconsistentes e preenche vazios com 'Outros' """
    if pd.isnull(cat) or cat.strip() == '':
        return 'Outros'
    cat = cat.strip().lower()
    if cat in ['alimento', 'alimentos']:
        return 'Alimento'
    elif cat in ['roupa', 'roupas']:
        return 'Roupas'
    elif cat in ['móveis', 'moveis']:
        return 'Móveis'
    elif cat in ['eletrônicos', 'eletronicos']:
        return 'Eletrônicos'
    else:
        return 'Outros'

def tratar_id_produto(idp: str) -> str:
    """Valida se o ID segue o padrão ??##-##??. Se não, retorna 'ID Inválido'."""
    if pd.isnull(idp) or not isinstance(idp, str):
        return 'ID Inválido'
    if re.match(r'^[A-Za-z]{2}\d{2}-\d{2}[A-Za-z]{2}$', idp.strip()):
        return idp.strip()
    else:
        return 'ID Inválido'

def tratar_endereco(endereco: str) -> str:
    """Completa com 'endereço incompleto' onde so houver o nome da cidade."""
    if pd.isnull(endereco) or endereco.strip() == '':
        return 'Endereço Incompleto'
    #Se só tem uma palavra(provavelmente so cidade)
    if len(endereco.split(',')) < 2:
        return 'Endereço Incompleto'
    return endereco.strip()

def tratar_estado(estado: str) -> str:
    """Corrige siglas erradas ('XX') para 'UF DESCONHECIDA"""
    if pd.isnull(estado) or estado.strip() == '':
        return 'UF Desconhecida'
    return estado.strip().upper()

def tratar_cep(cep: str) -> str:
    """valida que o cep tenha 8 digitos e formata como 00000-000"""
    if pd.isnull(cep) or not isinstance(cep, str):
        return 'CEP Inválido'
    cep_digits = re.sub(r'\D', '', cep)
    if len(cep_digits) == 8:
        return f'{cep_digits[:5]}-{cep_digits[5:]}'
    else:
        return 'CEP invalido'

def tratar_produto(produto: str) -> str:
    """Remove registros com produtos 'n\a' ou vazios."""
    if pd.isnull(produto) or produto.strip().lower() in ['n/a', '']:
        return ''
    return produto.strip().title()

def tratar_quantidade(qtd) -> int:
    """Preenche valores ausentes com 1"""
    if pd.isnull(qtd) or qtd == '':
        return 1
    try:
        return int(qtd)
    except:
        return 1
    
def tratar_forma_pagamento(forma: str) -> str:
    """Corrige caixa de texto e preenche vazios com 'não informado'. """
    if pd.isnull(forma) or forma.strip() == '':
        return 'Não informado'
    return forma.strip().capitalize()