def contar_vogais(texto):
    vogal = 0
    texto = texto.lower()
    for v in texto:
        if v in "aeiou":
            vogal += 1
           
    return f"Existem {vogal} vogais"

texto = input("Digite: ")
print(contar_vogais(texto))