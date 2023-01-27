import unittest

from app.financiamento_sac_price import FinanciamentoSacPrice


class FinanciamentoSacTeste(unittest.TestCase):

    def test_taxa_juro_mes_decimal(self):
        fi = FinanciamentoSacPrice(100000, 7, 200)
        self.assertEqual(fi.get_taxa_juro_mes_decimal(), 0.005833333333333334)

    def test_taxa_juro_ano_decimal(self):
        fi = FinanciamentoSacPrice(100000, 7, 200)
        self.assertEqual(fi.get_taxa_juro_ano_decimal(), 0.07)

    def test_amortizacao_sac(self):
        fi = FinanciamentoSacPrice(100000, 7, 200)
        self.assertEqual(fi.get_amortizacao_sac(), 500)

    def test_get_saldo_juros_mes_sac(self):
        fi = FinanciamentoSacPrice(100000, 8.4, 200)
        parcelas = fi.get_saldo_juros_mes_sac()
        numero_parcelas = len(parcelas)
        self.assertEqual(parcelas[0], 700.0000000000001)
        self.assertEqual(parcelas[numero_parcelas - 1], 3.5000000000000004)
        self.assertEqual(numero_parcelas, 200)

    def test_calcula_valor_parcela_mes(self):
        fi = FinanciamentoSacPrice(100000, 8.4, 200)
        parcelas = fi.get_saldo_juros_mes_sac()
        parcelas = fi.calcula_valor_parcela_mes_sac(parcelas)
        numero_parcelas = len(parcelas)
        self.assertEqual(parcelas[0], 1200.0000000000001)
        self.assertEqual(parcelas[numero_parcelas - 1], 503.5000000000000004)
        self.assertEqual(numero_parcelas, 200)

    def test_calcula_valor_total_em_juros(self):
        fi = FinanciamentoSacPrice(360000, 7, 360)
        parcelas = fi.get_saldo_juros_mes_sac()
        parcelas = fi.calcula_valor_parcela_mes_sac(parcelas)
        self.assertEqual(fi.get_amortizacao_sac(), 1000)
        self.assertEqual(fi.calcula_valor_total_em_juros(parcelas, fi.get_valor_financiado()), 379050.0)

    def test_calcula_valor_total(self):
        fi = FinanciamentoSacPrice(360000, 7, 360)
        parcelas = fi.get_saldo_juros_mes_sac()
        parcelas = fi.calcula_valor_parcela_mes_sac(parcelas)
        self.assertEqual(fi.calcula_valor_total(parcelas), 739050.0)


if __name__ == '__main__':
    unittest.main()
