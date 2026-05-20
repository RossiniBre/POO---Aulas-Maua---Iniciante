def inverter_palavras(frase):
    frase = frase.split()
    frase.reverse()
    nova_frase = " ".join(frase)
    return nova_frase

frase = input("Digite: ")
print(inverter_palavras(frase))
