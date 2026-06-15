nomes = sorted(["Carlos", "Ana", "Beatriz", "Zé"], key=lambda n: len(n))
print(nomes)

absoluto = sorted([-5, 2, -1, 4, -3], key=lambda n: abs(n))
print(absoluto)

frutas = sorted(["banana", "uva", "abacaxi", "pera"], key=lambda n: n[-1])
print(frutas)


produtos = [
    {"nome": "café", "preco": 8},
    {"nome": "pão", "preco": 3},
    {"nome": "leite", "preco": 5},
]

preco = sorted(produtos, key=lambda n: n['preco'])
print(preco)

nome = sorted(produtos, key=lambda n: len(n['nome']))
print(nome)

nomes_ignora = sorted( ["Ana", "alberto", "Beatriz", "abel"], key=lambda n: n.lower())
print(nomes_ignora)