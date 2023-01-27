# https://flask.palletsprojects.com/en/2.2.x/quickstart/
import json

from flask import Flask, request, abort

from app.financiamento_sac_price import FinanciamentoSacPrice

app = Flask(__name__)


@app.post("/financiamentos/sac")
def financiamentos_sac():
    request_data = request.get_json()
    try:
        valor_financiado = float(request_data['valor_financiado'])
        taxa_juros_ano = float(request_data['taxa_juros_ano'])
        numero_parcela = int(request_data['numero_parcela'])
        app.logger.debug(f'Log test {request_data}')
        sac = FinanciamentoSacPrice(valor_financiado, taxa_juros_ano, numero_parcela)
        juros_parcela = sac.get_saldo_juros_mes_sac()
        sac_mes = sac.calcula_valor_parcela_mes_sac(juros_parcela)
        obj = {
            "valor_financiado": sac.get_valor_financiado(),
            "taxa_juros_mes": sac.get_taxa_juro_mes_decimal() * 100,
            "taxa_juros_ano": sac.get_taxa_juro_ano_decimal() * 100,
            "numero_parcelas": sac.get_numero_parcela(),
            "amortizacao": sac.get_amortizacao_sac(),
            "juros_parcela": juros_parcela,
            "valor_parcela": sac_mes,
            "total_juros": sac.calcula_valor_total_em_juros(sac_mes),
            "total": sac.calcula_valor_total(sac_mes)
        }
        return json.dumps(obj)
    except Exception as e:
        print("This is not a number. Please enter a valid number")
        app.logger.error('An error occurred')
        abort(400, e)


@app.post("/financiamentos/price")
def financiamentos_price():
    return "<p>Hello, World!</p>"


@app.post("/financiamentos/carros")
def financiamentos_carros():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
