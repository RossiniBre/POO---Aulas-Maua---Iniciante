import random

print(
    "Qual o melhor sistema?\n" \
    "1 - Windows\n" \
    "2 - Unix\n" \
    "3 - Linux\n" \
    "4 - Netware\n" \
    "5 - Mac Os\n" \
    "6 - Outro\n"
    )

votos = [0, 0, 0, 0, 0, 0]
nomes = ["Windows", "Unix", "Linux", "Netware", "Mac", "Outro"]

for i in range(8800):
    escolha = random.choice([1, 2, 3, 4, 5, 6])
    votos[escolha - 1] += 1

total = sum(votos)

print("====================")
for nome, qtd in zip(nomes, votos):
    percentual = (qtd / total) * 100
    print(f"{nome}: {qtd} ({percentual:.0f}%)")
print("====================")
print("Total de votos:", total)