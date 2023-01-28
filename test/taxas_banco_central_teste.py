import unittest

from app.taxas_banco_central import TaxaJurosBancoCentral


class TaxaJurosBancoCentralTeste(unittest.TestCase):

    def test_read_aquisicao_veiculo_pessoa_fisica(self):
        taxas = TaxaJurosBancoCentral()
        # taxas.read_aquisicao_veiculo_pessoa_fisica()


if __name__ == '__main__':
    unittest.main()
