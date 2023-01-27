# Cálculo de financiamento SAC
# Sistema de amortização constante

class FinanciamentoSacPrice:

    def __init__(self, valor_financiado, taxa_juros_ano, numero_parcela):
        self.valor_financiado = valor_financiado
        self.taxa_juros_ano = taxa_juros_ano
        self.numero_parcela = numero_parcela

    def get_taxa_juro_ano_decimal(self) -> float:
        return self.taxa_juros_ano / 100

    def get_taxa_juro_mes_decimal(self) -> float:
        return (self.taxa_juros_ano / 12) / 100

    def get_valor_financiado(self) -> float:
        return self.valor_financiado

    def get_numero_parcela(self) -> int:
        return self.numero_parcela

    def calcula_valor_total(self, parcelas) -> float:
        total = 0
        for parcela in parcelas:
            total += parcela
        return total

    def calcula_valor_total_em_juros(self, parcelas) -> float:
        total = 0
        for parcela in parcelas:
            total += parcela
        return total - self.get_valor_financiado()

    # SAC
    def get_amortizacao_sac(self) -> float:
        return self.get_valor_financiado() / self.get_numero_parcela()

    def get_saldo_juros_mes_sac(self) -> list:
        parcelas = []
        total = self.get_valor_financiado()
        while total > 0:
            parcelas.append(total * self.get_taxa_juro_mes_decimal())
            if total > self.get_amortizacao_sac():
                total -= self.get_amortizacao_sac()
            else:
                total -= total
        return parcelas

    def calcula_valor_parcela_mes_sac(self, juros_metodo) -> list:
        parcelas = []
        for parcela in juros_metodo:
            parcelas.append(parcela + self.get_amortizacao_sac())
        return parcelas

    # PRICE
    def get_valor_parcela_price(self) -> float:
        numerador = ((1 + self.get_taxa_juro_mes_decimal()) ** self.get_numero_parcela()) \
                    * self.get_taxa_juro_mes_decimal()
        denominador = ((1 + self.get_taxa_juro_mes_decimal()) ** self.get_numero_parcela()) - 1
        total = self.get_valor_financiado() * (numerador / denominador)
        return total

    def get_amortizacao_price(self) -> list:
        amortizacao = []
        for juros in self.get_saldo_juros_mes_price():
            amortizacao.append(self.get_valor_parcela_price() - juros)
        return amortizacao

    def get_saldo_juros_mes_price(self) -> list:
        parcelas = []
        total = self.get_valor_financiado()
        while total > 0:
            juros = total * self.get_taxa_juro_mes_decimal()
            parcelas.append(juros)
            if total > self.get_valor_parcela_price():
                total -= (self.get_valor_parcela_price() - juros)
            else:
                total -= total
        return parcelas
