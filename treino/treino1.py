estoque = {
    "eletronicos": {"mouse": 15, "teclado": 8, "monitor": 3},
    "papelaria": {"caneta": 50, "caderno": 20, "borracha": 30},
    "limpeza": {"detergente": 12, "sabao": 25}
}

def produto_mais_estocado(estoque):
    mais_estocado = ()
    qntd_atual = 0
    for categoria, produtos in estoque.items():
        for produto, quantidade in produtos.items():
            if quantidade > qntd_atual:
                qntd_atual = quantidade
                mais_estocado = (categoria, produto, quantidade)
            
    return mais_estocado

print(produto_mais_estocado(estoque))

def estoque_para_lista(estoque):
    lista_d = []
    for categoria, produtos in estoque.items():
        for produto, quantidade in produtos.items():
            d = {}
            d["Categoria"] = categoria
            d["Produto"] = produto
            d["Quantidade"] = quantidade
            lista_d.append(d)
    return lista_d

print(estoque_para_lista(estoque))
