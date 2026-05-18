user = input("digite o user: ")

def analise(user):
    start = False
    tamanho = user[1:]
    t = False
    Letras_Numeros = False

    if user.startswith("@"):
        start = True
    if len(user[1:]) >= 5:
        t = True
    if tamanho.isalnum():
        Letras_Numeros = True

    if start and t and Letras_Numeros:
        return "User atende as condições"
    else:
        return "User não atende condições"
    
print(analise(user))
print(f"Quantidade de letras A: {user.lower().count("a")}")
print(f"Username maiusculo: {user.upper()}")
print(f"Username invertido: {user[::-1]}")