from aluno import *

aluno1 = cadastrar_aluno("Breno", 79.5, 1.84)
aluno2 = cadastrar_aluno("Murilo", 120, 1.83)

for aluno in [aluno1, aluno2]:

    print("=== Ficha do Aluno ===")

    print(f"Nome: {aluno['nome']}")

    print(
        f"Peso: {aluno['peso']}kg | "
        f"Altura: {aluno['altura']}m"
    )

    print(f"IMC: {aluno['imc']:.2f}")

    print(f"Classificação: {aluno['classificacao']}")

    print(f"Treino sugerido: {aluno['treino']}")

    print()