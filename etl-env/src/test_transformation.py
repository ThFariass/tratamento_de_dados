import unittest
from transformations import (tratar_cliente, tratar_data_cadastro)

class testTransformations(unittest.TestCase):
    def test_cliente(self):
        self.assertEqual(tratar_cliente('Sr. maria fernanda'), 'Maria Fernanda')
        self.assertEqual(tratar_cliente('dra. ana'), 'Ana')
        
if __name__ == '__main__':
    unittest.main()