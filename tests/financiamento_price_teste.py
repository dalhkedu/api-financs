import unittest
import pytest

from app.financiamento_sac_price import FinanciamentoSacPrice


class FinanciamentoPriceTeste(unittest.TestCase):

    def test_amortizacao_price(self):
        fi = FinanciamentoSacPrice(100000, 8.4, 200)
        amortizacao = fi.get_amortizacao_price()
        self.assertEqual(amortizacao[1], 232.22104868698864)

    def test_valor_parcela_price(self):
        fi = FinanciamentoSacPrice(100000, 8.4, 200)
        self.assertEqual(fi.get_valor_parcela_price(), 930.6068010794328)

    def test_saldo_juros_mes_price(self):
        fi = FinanciamentoSacPrice(100000, 8.4, 200)
        juros = fi.get_saldo_juros_mes_price()
        self.assertEqual(juros[1], 698.3857523924441)


if __name__ == '__main__':
    unittest.main()
