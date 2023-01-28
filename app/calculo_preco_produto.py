# https://www.sebrae-sc.com.br/blog/como-calcular-o-preco-de-um-produto
# CD (Custos Diretos) + CI (Custos Indiretos) + CF (Custos Fixos) + CV (Custos Variáveis) = CT (Custo Total).
class CalcularPrecoProduto:
    def __init__(self, custo_direto, custo_indireto, custo_fixo, custo_variavel):
        self.custo_direto = custo_direto
        self.custo_indireto = custo_indireto
        self.custo_fixo = custo_fixo
        self.custo_variavel = custo_variavel
