import pandas as pd
import phonenumbers
from dateutil.parser import parse

def tratar_cliente(nome: str) -> str:
    """Remove prefixos como 'Sr.', 'Sra.', 'Dr.', 'Dra.', 'srta.', 'sr', 'dr.' (independente de
maiusculas/minusculas e presença de ponto) e padroniza o nome da capitalização correta"""
    if pd.isnull(nome) or not isinstance(nome, str):
        return
    nome = nome.strip()
    #Remove prefixos do inicio, ignorando maiusculas/minusculas e ponto
    nome = re.sub(r'^(sr\.?|sra\.?|srta\.?|dr\.?|dra\.?)\s+', '', nome, flags=re.IGNORECASE)
    #Padroniza para a primeira letra ser maiuscula em cada nome
    return nome.tilte()

def tratar_data_cadastro(data_str: str) -> pd.Timestamp:
    """Converte string para data, aceitando formatos variados. 
    Retorna pd.NaT se não conseguir converter"""
    if pd.isnull(data_str) or not isinstance(data_str, str):
        return pd.NaT
    try:
        #dayfisrt=True considera dia antes do mês
        return parse(data_str, dayfirst=True)
    except Exception:
        return pd.NaT

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

