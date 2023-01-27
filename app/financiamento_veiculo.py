# Valor do Veiculo
# Valor da Entrada (Caso tenha)
# Taxa de Juros (Mensal)
# Numero de Parcelas

class FinanciamentoVeiculo:

    def __init__(self, valor_veiculo, valor_entrada, taxa_juros_mes, numero_parcela):
        self.valor_veiculo = valor_veiculo
        self.valor_entrada = valor_entrada
        self.taxa_juros_mes = taxa_juros_mes
        self.numero_parcela = numero_parcela

    def get_valor_financiado(self) -> float:
        return self.valor_veiculo - self.valor_entrada

    def get_taxa_juro_decimal(self) -> float:
        return self.taxa_juros_mes / 100

    def get_numero_parcela(self) -> int:
        return self.numero_parcela

    def get_valor_veiculo(self):
        return self.valor_veiculo

    def get_numerador(self) -> float:
        return (((1 + self.get_taxa_juro_decimal()) ** self.get_numero_parcela()) * self.get_valor_financiado()) * \
               self.get_taxa_juro_decimal()

    def get_denominador(self) -> float:
        return ((1 + self.get_taxa_juro_decimal()) ** self.get_numero_parcela()) - 1

    def calcula_prestacao(self) -> float:
        return self.get_numerador() / self.get_denominador()

    def calcula_valor_ipva(self):
        desconto = 4 / 100
        valor = self.get_valor_veiculo() * desconto
        return valor
