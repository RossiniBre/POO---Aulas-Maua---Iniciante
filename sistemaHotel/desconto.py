def desconto(valor_total, dias):
    if dias >= 7:
        desconto = valor_total * (15/100)
        valor_total -= desconto 
        return valor_total
    else:
        return valor_total

    