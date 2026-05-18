from hospede import cadastrar_hospede

hospede1 = cadastrar_hospede("Cleber", 3, 5, 80)
hospede2 = cadastrar_hospede("Leandro", 2, 14, 80)

for h in [hospede1, hospede2]:

    print("===== Ficha de Hóspede =====")

    print(f"Cliente: {h['nome']}")

    print(f"Quarto: {h['quarto']}")

    print(f"Dias: {h['dias']}")

    print(f"Valor total: {h['valor_total']:.2f}")

    print(f"Valor final: {h['valor_final']:.2f}")

    print()