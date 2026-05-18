def sugerir_treino(classificacao):
    if classificacao == "Abaixo do peso":
        return "Treino de força"
    elif classificacao == "Normal":
        return "Treino misto"
    elif classificacao == "Sobrepeso":
        return "Treino cardio"
    elif classificacao == "Obesidade":
        return "Treino leve + acompanhamento"