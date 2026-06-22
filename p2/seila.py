numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
print(pares)

nomes = ["ana", "bruno", "carla", "diego"]
maiusculo = [n.upper() for n in nomes]
print(maiusculo)

maior = sorted([34, 12, 56, 8, 23, 45], reverse = True)
menor = sorted([34, 12, 56, 8, 23, 45])

print(maior)
print(menor)

produtos = sorted([("caderno", 12.50), ("caneta", 2.00), ("tesoura", 5.00), ("lápis", 1.50)], key=lambda n: n[1])
print(produtos)

dobro = lambda n: n * 2
print(dobro(5))

aluno = {
    'nome' : 'Breno',
    'idade' : 18,
    'nota' : 8.1
}

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")