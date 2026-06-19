# Lista de materiais
global materiais
materiais = [
    {"material": ("caderno", 1001), "preco": 12.50, "quant": 20},
    {"material": ("caneta azul", 1002), "preco": 2.00, "quant": 100},
    {"material": ("caneta preta", 1003), "preco": 2.00, "quant": 95},
    {"material": ("lápis", 1004), "preco": 1.50, "quant": 150},
    {"material": ("borracha", 1005), "preco": 1.20, "quant": 80},
    {"material": ("apontador", 1006), "preco": 2.50, "quant": 60},
    {"material": ("tesoura", 1007), "preco": 5.00, "quant": 35},
    {"material": ("cola branca", 1008), "preco": 4.30, "quant": 40},
    {"material": ("régua 30cm", 1009), "preco": 3.00, "quant": 50},
    {"material": ("marca-texto", 1010), "preco": 3.80, "quant": 45},
    {"material": ("corretivo", 1011), "preco": 3.20, "quant": 25},
    {"material": ("grampeador", 1012), "preco": 12.90, "quant": 15},
    {"material": ("folhas A4 (pacote)", 1013), "preco": 22.00, "quant": 30},
    {"material": ("pincel", 1014), "preco": 3.70, "quant": 20},
    {"material": ("tinta guache", 1015), "preco": 6.50, "quant": 18}
]

def insere_material():
    while True:
        n = input("Insira um material: ")
        existe = False
        for i in materiais:
            if n == i['material'][0]:
                existe = True
                break
        if existe:
            print("Material já existe! Insira outro.")
        else:
            preco = float(input("Digite o preço: "))
            qtd = int(input("Digite a quantidade: "))
            novo_codigo = max(m['material'][1] for m in materiais) + 1
            materiais.append({"material": (n, novo_codigo), "preco": preco, "quant": qtd})
            print(f"Material '{n}' inserido com sucesso!")
            break

insere_material()
print(materiais[-1])