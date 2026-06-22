from random import choice

def criar_baralho():
    baralho = {
        ("ás", 1) : 4,
        ("valete", 10): 4,
        ("dama", 10) : 4,
        ("rei", 10) : 4,
        ("2", 2) : 4,
        ("3", 3) : 4,
        ("4", 4) : 4,
        ("5", 5) : 4,
        ("6", 6) : 4,
        ("7", 7) : 4,
        ("8", 8) : 4,
        ("9", 9) : 4,
        ("10" , 10) : 4,
        ("coringa", 0) : 2
    }

    return baralho

def valor_mao(baralho, num_cartas):
    mao = 0
    lista = list(baralho.keys())
    for carta in range(num_cartas):
        carta = choice(lista)
        print(carta[0])
        mao += carta[1]

    return mao


global baralho 
baralho = criar_baralho()
valor = valor_mao(baralho, 4)
print('\nValor da mão:', valor)