# https://www.bcb.gov.br/estatisticas/txjuros

import tabula


class TaxaJurosBancoCentral:
    def __init__(self):
        pass

    def read_aquisicao_veiculo_pessoa_fisica(self):
        # https://www.bcb.gov.br/estatisticas/reporttxjuros/?parametros=tipopessoa:1;modalidade:401;encargo:101
        tabela = tabula.read_pdf("../relatorios-bancocentral/aquisicao_veiculo_pessoa_fisica.pdf", pages="all")
        tabela = tabela.drop("Posição", axis=1)
        print(len(tabela))
        for tab in tabela:
            print(tab)
