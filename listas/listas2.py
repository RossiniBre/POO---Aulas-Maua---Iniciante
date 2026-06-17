alunos = [
    {"nome": "Carlos", "nota": 5},
    {"nome": "Ana", "nota": 9},
    {"nome": "Zé", "nota": 6},
    {"nome": "Beatriz", "nota": 3},
    {"nome": "Diego", "nota": 7},
]

aprovados = sorted([aluno for aluno in alunos if aluno['nota'] >= 6], key=lambda n: n['nome'])
print(aprovados)

frutas = ["banana", "uva", "abacaxi", "pera", "kiwi"]
frutas = sorted([fruta.upper() for fruta in frutas if len(fruta) > 4], key=lambda n: len(n))
print(frutas)

produtos = [
    {"nome": "café", "preco": 8},
    {"nome": "água", "preco": 2},
    {"nome": "suco", "preco": 12},
    {"nome": "pão", "preco": 5},
]

ex3 = sorted([preco for preco in produtos if preco['preco'] < 10], key=lambda n: n['preco'])
print(ex3)

quadradosnegativos = sorted([quadrado **2 for quadrado in [-3, -1, 2, -5, 4, 0] if quadrado < 0], reverse = True)
print(quadradosnegativos)

alunos = [
    {"nome": "Carlos", "nota": 7},
    {"nome": "Ana", "nota": 9},
    {"nome": "Zé", "nota": 5},
]

nome_nota = sorted(alunos, key=lambda n: n['nota'], reverse=True)
nome_nota = [f"{aluno['nome']}: {aluno['nota']}" for aluno in nome_nota]
print(nome_nota)