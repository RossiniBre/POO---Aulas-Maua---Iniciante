from quarto import definir_quarto
from diaria import calcular_diaria
from desconto import desconto

def cadastrar_hospede(nome, pessoas, dias, valor_dia):

    quarto = definir_quarto(pessoas)
    valor_total = calcular_diaria(dias, valor_dia)
    valor_final = desconto(valor_total, dias)

    cadastro = {
        'nome' : nome,
        'quarto' : quarto,
        'dias' : dias,
        'valor_total' : valor_total,
        'valor_final' : valor_final
    }

    return cadastro
