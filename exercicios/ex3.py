produtos = [
    ("Caderno", "Papelaria", 12.90),
    ("Caneta", "Papelaria", 2.50),
    ("Mouse", "Eletrônicos", 45.00),
    ("Teclado", "Eletrônicos", 89.90),
    ("Borracha", "Papelaria", 1.80),
    ("Monitor", "Eletrônicos", 650.00),
]

dic = {}

for p in sorted(produtos, key=lambda n: n[-1]):
    if p[1] not in dic:
        dic[p[1]] = []
    dic[p[1]].append(p)

for chave, valor in dic.items():
    print(f"{chave} : {valor}")

medias = {}
for categoria, lista_produtos in dic.items():
    precos = [item[-1] for item in lista_produtos]
    medias[categoria] = sum(precos) / len(precos)

categoria_maior_media = max(medias, key=medias.get)

print(f"Categoria: {categoria_maior_media} | Preço médio: {medias[categoria_maior_media]:.2f}")