while True:
    n = int(input("Digite um valor (0 para sair): "))

    if n == 0:
        break

    numero = n
    soma = 0
    maior = 0
    menor = 10

    while numero > 0:
        ultimo = numero % 10
        numero //= 10

        soma += ultimo

        if ultimo > maior:
            maior = ultimo

        if ultimo < menor:
            menor = ultimo

    if soma % 2 == 0 and maior > (menor + 5):
        print(f"{n} é especial!")
    else:
        print(f"{n} não é especial!")