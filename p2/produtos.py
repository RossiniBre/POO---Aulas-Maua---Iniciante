produtos = [
    {"nome": "caderno", "preco": 12.50},
    {"nome": "caneta", "preco": 2.00},
    {"nome": "tesoura", "preco": 5.00},
    {"nome": "cola", "preco": 4.30},
]

produto = [n['nome'] for n in produtos if n["preco"] >= 5]
print(produto)

maior = sorted([n for n in produtos], key= lambda n: n["preco"], reverse = True)
print(maior)

alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "Carla", "nota": 9.2},
    {"nome": "Diego", "nota": 5.5},
]

aluno_nova = sorted([f"Nome: {n["nome"]}" for n in alunos if n["nota"] >= 7], key=lambda n: n['nota'])
print(aluno_nova)