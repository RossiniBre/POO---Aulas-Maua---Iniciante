from L20 import *

def distribuicao(num_jogadores):
    global baralho
    
    maos = {}
    for i in range(1, num_jogadores + 1):
        maos["jogador" + str(i)] = 0

    while len(baralho) > 0:
        for jogador in maos:
            if len(baralho) == 0:
                break

            lista = list(baralho.keys())
            remover = choice(lista)

            maos[jogador] += remover[1]  # soma o valor de pontos da carta

            if baralho[remover] == 1:
                del baralho[remover]
            else:
                baralho[remover] -= 1

    return maos


a = distribuicao(5)
print(a)