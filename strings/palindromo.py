def palindromo(frase):
    frase = frase.lower().split(" ")
    nova_frase = "".join(frase)
    if nova_frase == nova_frase[::-1]:
        return f"{nova_frase} é palíndromo"
    else:
        return f"{nova_frase} não é palindromo"
    
frase = input("Digite: ")
print(palindromo(frase))