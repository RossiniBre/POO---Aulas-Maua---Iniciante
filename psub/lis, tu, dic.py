pares = sorted(n for n in [11, 12, 34, 56, 67, 35, 78] if n % 2 == 0)
print(pares)

produtos = {
    "garrafa" : 15.90,
    "caderno" : 12.90,
    "caneta" : 5.90
}

lista = sorted([(chave, valor) for chave, valor in produtos.items()], key=lambda n: n[1])
print(lista)

maior = lista[-1]
menor = lista[0]

print(maior)
print(menor)

alunoslista = [
    ("Ana", 8.5),
    ("Bruno", 5.0),
    ("Carlos", 6.0),
    ("Daniela", 9.2),
    ("Eduardo", 4.8),
    ("Fernanda", 7.1),
    ("Gabriel", 5.9)
]

aprovados = sorted([n for n in alunoslista if n[1] >= 6], key=lambda n: n[0])
reprovados = sorted([n for n in alunoslista if n[1] < 6], key=lambda n: n[0])

alunos = {
    "aprovados" : aprovados,
    "reprovados" : reprovados
}

for i in alunoslista:
    if i in aprovados:
        print(f"Aluno: {i[0]} | Nota: {i[1]} | Situação: Aprovado")
    else:
        print(f"Aluno: {i[0]} | Nota: {i[1]} | Situação: Reprovado")

print(alunos)