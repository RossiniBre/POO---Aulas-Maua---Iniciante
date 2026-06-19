import time
from math import *

divisores = []

try:
    numero = int(input())
    if numero > 0:
        inicio = time.time()
        for divisor in range(1, int(sqrt(numero)) + 1):
            if numero % divisor == 0:
                if divisor == numero // divisor:
                    divisores.append(divisor)
                else:
                    divisores.append(divisor)
                    divisores.append(numero // divisor)
        fim = time.time()
        tempo = fim - inicio
        divisores.sort()
        print(divisores)
        print(f"Tempo total: {tempo:.2f}")
    else:
        raise ValueError("Digite apenas número maiores que 0")
    

except: 
    print("Digite apenas número maiores que 0")