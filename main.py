# https://flask.palletsprojects.com/en/2.2.x/quickstart/
import json

from flask import Flask, request, abort

from app.financiamento_sac_price import FinanciamentoSacPrice
from app.financiamento_veiculo import FinanciamentoVeiculo

app = Flask(__name__)


@app.post("/financiamentos/sac")
def financiamentos_sac():
    request_data = request.get_json()
    try:
        valor_financiado = float(request_data['valor_financiado'])
        taxa_juros_ano = float(request_data['taxa_juros_ano'])
        numero_parcela = int(request_data['numero_parcela'])
        app.logger.debug(f'Log test {request_data}')
        fin = FinanciamentoSacPrice(valor_financiado, taxa_juros_ano,
                                    numero_parcela)
        juros_parcela = fin.get_saldo_juros_mes_sac()
        fin_mes = fin.calcula_valor_parcela_mes_sac(juros_parcela)
        obj = {
            "valor_financiado": fin.get_valor_financiado(),
            "taxa_juros_mes": fin.get_taxa_juro_mes_decimal() * 100,
            "taxa_juros_ano": fin.get_taxa_juro_ano_decimal() * 100,
            "salario_base": fin_mes[0] / 0.3,
            "primeira_parcela": fin_mes[0],
            "ultima_parcela": fin_mes[len(fin_mes) - 1],
            "numero_parcelas": fin.get_numero_parcela(),
            "amortizacao": fin.get_amortizacao_sac(),
            "juros_parcela": juros_parcela,
            "valor_parcela": fin_mes,
            "total_juros": fin.calcula_valor_total_em_juros(fin_mes,
                                                            valor_financiado),
            "total": fin.calcula_valor_total(fin_mes)
        }
        return json.dumps(obj)
    except Exception as e:
        print("This is not a number. Please enter a valid number")
        app.logger.error('An error occurred')
        abort(400, e)


@app.post("/financiamentos/price")
def financiamentos_price():
    request_data = request.get_json()
    try:
        valor_financiado = float(request_data['valor_financiado'])
        taxa_juros_ano = float(request_data['taxa_juros_ano'])
        numero_parcela = int(request_data['numero_parcela'])
        app.logger.debug(f'Log test {request_data}')
        fin = FinanciamentoSacPrice(valor_financiado, taxa_juros_ano,
                                    numero_parcela)
        mes = fin.get_valor_parcela_price()
        juros = fin.get_saldo_juros_mes_price()
        valor_parcela = fin.get_valor_parcela_price()
        obj = {
            "valor_financiado": fin.get_valor_financiado(),
            "taxa_juros_mes": fin.get_taxa_juro_mes_decimal() * 100,
            "taxa_juros_ano": fin.get_taxa_juro_ano_decimal() * 100,
            "numero_parcelas": fin.get_numero_parcela(),
            "amortizacao": fin.get_amortizacao_price(),
            "juros_parcela": juros,
            "valor_parcela": valor_parcela,
            "salario_base": valor_parcela / 0.3,
            "total_juros": fin.calcula_valor_total_em_juros(juros, 0),
            "total": mes * numero_parcela
        }
        return json.dumps(obj)
    except Exception as e:
        print("This is not a number. Please enter a valid number")
        app.logger.error('An error occurred')
        abort(400, e)


@app.post("/financiamentos/veiculos")
def financiamentos_carros():
    request_data = request.get_json()
    try:
        valor_veiculo = float(request_data['valor_veiculo'])
        valor_entrada = float(request_data['valor_entrada'])
        taxa_juros_mes = float(request_data['taxa_juros_mes'])
        numero_parcela = int(request_data['numero_parcela'])
        app.logger.debug(f'Log test {request_data}')
        fin = FinanciamentoVeiculo(valor_veiculo, valor_entrada,
                                   taxa_juros_mes,
                                   numero_parcela)

        obj = {
            "valor_veiculo": fin.get_valor_veiculo(),
            "valor_entrada": valor_entrada,
            "numero_parcelas": fin.get_numero_parcela(),
            "valor_ipva": fin.calcula_valor_ipva(),
            "valor_prestacao": fin.calcula_prestacao(),
            "juros_parcela": fin.get_taxa_juro_decimal() * 100,
            "denominador": fin.get_denominador(),
            "numerador": fin.get_numerador(),
            "total": fin.calcula_prestacao() * fin.get_numero_parcela()
        }
        return json.dumps(obj)
    except Exception as e:
        print("This is not a number. Please enter a valid number")
        app.logger.error('An error occurred')
        abort(400, e)


if __name__ == "__main__":
    app.run(debug=True)
