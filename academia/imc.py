def calculo_imc(peso, altura):
    imc = peso/(altura**2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do Peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
    