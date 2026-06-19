notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5,
         4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]

alunos = ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Fábio", "Gabriela",
         "Hugo", "Isabela", "João", "Karina", "Lucas", "Mariana", "Nicolas", "Olivia"]

soma = sum(notas)
print(soma)
media = soma / len(notas)
print(f"{media:.2f}")

aprovados = sorted([f"Aluno: {aluno} | Nota: {nota}" for aluno, nota in zip(alunos, notas) if nota >= 6], key=lambda n: n, reverse = True)

for i in aprovados:
    print(i)


numeros = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]


pares = sorted([n for n in numeros if n % 2 == 0])
impares = sorted([n for n in numeros if n % 2 == 1])
print(pares)
print(impares)