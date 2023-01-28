import unittest

from app.financiamento_veiculo import FinanciamentoVeiculo


class FinanciamentoVeiculoTeste(unittest.TestCase):

    def test_valor_financiado(self):
        fi = FinanciamentoVeiculo(80000, 30000, 2.9, 48)
        self.assertEqual(fi.get_valor_financiado(), 50000)

    def test_taxa_juro_decimal(self):
        fi = FinanciamentoVeiculo(80000, 30000, 2.9, 48)
        self.assertEqual(fi.get_taxa_juro_decimal(), 0.028999999999999998)

    def test_numerador(self):
        fi = FinanciamentoVeiculo(80000, 30000, 2.9, 48)
        self.assertEqual(fi.get_numerador(), 5718.81425213324)

    def test_denominador(self):
        fi = FinanciamentoVeiculo(80000, 30000, 2.9, 48)
        self.assertEqual(fi.get_denominador(), 2.9440098290574075)

    def test_calcula_prestacao(self):
        fi = FinanciamentoVeiculo(80000, 30000, 2.9, 48)
        fi2 = FinanciamentoVeiculo(48000, 0, 1.77, 36)
        self.assertEqual(fi.calcula_prestacao(), 1942.5255295306708)
        self.assertEqual(fi2.calcula_prestacao(), 1814.323430767464)

    def test_calcula_valor_ipva(self):
        fi = FinanciamentoVeiculo(80000, 30000, 2.9, 48)
        fi2 = FinanciamentoVeiculo(48000, 0, 1.77, 36)
        self.assertEqual(fi.calcula_valor_ipva(), 3200.0)
        self.assertEqual(fi2.calcula_valor_ipva(), 1920.0)


if __name__ == '__main__':
    unittest.main()
