vendas = [
    {"categoria": "eletronicos", "produto": "mouse", "valor": 50},
    {"categoria": "eletronicos", "produto": "teclado", "valor": 120},
    {"categoria": "papelaria", "produto": "caneta", "valor": 5},
    {"categoria": "papelaria", "produto": "caderno", "valor": 15},
    {"categoria": "papelaria", "produto": "borracha", "valor": 3},
    {"categoria": "limpeza", "produto": "detergente", "valor": 8},
]

def total_por_categoria(vendas):
    valor_total = {}
    for dic in vendas:
        valor_total.setdefault(dic["categoria"], 0)
        valor_total[dic["categoria"]] += dic["valor"] 

    return valor_total

print(total_por_categoria(vendas))