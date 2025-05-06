import unittest
from transformations import *

class TestTransformations(unittest.TestCase):
# 
    def test_tratar_cliente(self):
        self.assertEqual(tratar_cliente('Sr. maria fernanda'), 'Maria Fernanda')
        self.assertEqual(tratar_cliente('dra. ana'), 'Ana')
        self.assertEqual(tratar_cliente('Dr. João Silva'), 'João Silva')
        self.assertEqual(tratar_cliente('ana'), 'Ana')
        self.assertEqual(tratar_cliente('Sra. MARIA'), 'Maria')
        self.assertEqual(tratar_cliente(None), '')

    def test_tratar_data_cadastro(self):
        self.assertEqual(tratar_data_cadastro('2023-12-01'), '01/12/2023')
        self.assertEqual(tratar_data_cadastro('01/12/2023'), '01/12/2023')
        self.assertEqual(tratar_data_cadastro('31/01/2024'), '31/01/2024')
        self.assertEqual(tratar_data_cadastro('errado'), '')
        self.assertEqual(tratar_data_cadastro(None), '')

    def test_tratar_telefone(self):
        self.assertEqual(tratar_telefone('5531970050393'), '(31) 97005-0393')
        self.assertEqual(tratar_telefone('+55 61 0216-1697'), '(61) 0216-1697')
        self.assertEqual(tratar_telefone('abc'), 'Telefone Inválido')
        self.assertEqual(tratar_telefone(None), 'Telefone Inválido')

    def test_tratar_email(self):
        self.assertEqual(tratar_email('teste@teste.com'), 'teste@teste.com')
        self.assertEqual(tratar_email('TESTE@TESTE.COM'), 'teste@teste.com')
        self.assertEqual(tratar_email('errado.com'), 'Email Inválido')
        self.assertEqual(tratar_email(''), 'Email Inválido')
        self.assertEqual(tratar_email(None), 'Email Inválido')

    def test_tratar_valor_compra(self):
        self.assertEqual(tratar_valor_compra('123,45'), 123.45)
        self.assertEqual(tratar_valor_compra('123.45'), 123.45)
        self.assertEqual(tratar_valor_compra('0'), 0.0)
        self.assertEqual(tratar_valor_compra(None), 0.0)

    def test_tratar_status(self):
        self.assertEqual(tratar_status('ativo'), 'Ativo')
        self.assertEqual(tratar_status('inativo'), 'Inativo')
        self.assertEqual(tratar_status('Em análise'), 'Em análise')
        self.assertEqual(tratar_status('em analise'), 'Em análise')
        self.assertEqual(tratar_status(''), '')

    def test_tratar_categoria(self):
        self.assertEqual(tratar_categoria('alimento'), 'Alimentos')
        self.assertEqual(tratar_categoria('Alimentos'), 'Alimentos')
        self.assertEqual(tratar_categoria('roupa'), 'Roupas')
        self.assertEqual(tratar_categoria('Roupas'), 'Roupas')
        self.assertEqual(tratar_categoria('móveis'), 'Móveis')
        self.assertEqual(tratar_categoria('eletronicos'), 'Eletrônicos')
        self.assertEqual(tratar_categoria(''), 'Outros')
        self.assertEqual(tratar_categoria(None), 'Outros')

    def test_tratar_id_produto(self):
        self.assertEqual(tratar_id_produto('AB12-34CD'), 'AB12-34CD')
        self.assertEqual(tratar_id_produto('ab12-34cd'), 'ab12-34cd')
        self.assertEqual(tratar_id_produto('errado'), 'ID Inválido')
        self.assertEqual(tratar_id_produto(None), 'ID Inválido')

    def test_tratar_endereco(self):
        self.assertEqual(tratar_endereco('Lima'), 'Endereço Incompleto')
        self.assertEqual(tratar_endereco('Rua A, 123'), 'Rua A, 123')
        self.assertEqual(tratar_endereco(''), 'Endereço Incompleto')
        self.assertEqual(tratar_endereco(None), 'Endereço Incompleto')

    def test_tratar_estado(self):
        self.assertEqual(tratar_estado('XX'), 'UF Desconhecida')
        self.assertEqual(tratar_estado('sp'), 'SP')
        self.assertEqual(tratar_estado('AM'), 'AM')
        self.assertEqual(tratar_estado(''), 'UF Desconhecida')
        self.assertEqual(tratar_estado(None), 'UF Desconhecida')

    def test_tratar_cep(self):
        self.assertEqual(tratar_cep('12345678'), '12345-678')
        self.assertEqual(tratar_cep('1234'), 'CEP Inválido')
        self.assertEqual(tratar_cep('12345-678'), '12345-678')
        self.assertEqual(tratar_cep(''), 'CEP Inválido')
        self.assertEqual(tratar_cep(None), 'CEP Inválido')

    def test_tratar_produto(self):
        self.assertEqual(tratar_produto('n/a'), '')
        self.assertEqual(tratar_produto('Cadeira'), 'Cadeira')
        self.assertEqual(tratar_produto(''), '')
        self.assertEqual(tratar_produto(None), '')

    def test_tratar_quantidade(self):
        self.assertEqual(tratar_quantidade(''), 1)
        self.assertEqual(tratar_quantidade(None), 1)
        self.assertEqual(tratar_quantidade('2'), 2)
        self.assertEqual(tratar_quantidade(5), 5)

    def test_tratar_forma_pagamento(self):
        self.assertEqual(tratar_forma_pagamento('dinheiro'), 'Dinheiro')
        self.assertEqual(tratar_forma_pagamento(''), 'Não Informado')
        self.assertEqual(tratar_forma_pagamento(None), 'Não Informado')
        self.assertEqual(tratar_forma_pagamento('PIX'), 'Pix')

if __name__ == '__main__':
    unittest.main()
 