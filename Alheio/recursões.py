#n = int(input("Digite um número: "))
# n = input("Digite o texto: ")

'''def contagem(n):

    print(n)

    if n == 0:
        return 
    
    return contagem(n-1)

contagem(n)'''
        
'''def soma(n):

    if n == 0:
        return 0
    
    return n + soma(n-1)

print(soma(n))'''

'''y = int(input("Digite Y: "))

def potencia(n, y):
    if y == 0:
        return 1
    
    return n * potencia(n, y-1)

print(potencia(n, y))'''


'''def contar_digitos(n):
    if n == 0:
        return 1

    return 1 + contar_digitos(n // 10)

print(contar_digitos(n))'''

'''def fibonnaci(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonnaci(n - 1) + fibonnaci(n - 2)

print(fibonnaci(n))'''

'''def inverter_string(n):
    if n == "":
        return ""
        
    return inverter_string(n[1:]) + n[0]
    
print(inverter_string(n))'''

'''texto = input("Digite o texto: ")
procurado = input("Digite oque deve ser procurado: ")

def contar_ocorrencias(texto, procurado):
    if texto == "":
        return 0
    
    if texto[0] == procurado:
        return 1 + contar_ocorrencias(texto[1:], procurado)
    else:
        return contar_ocorrencias(texto[1:], procurado)
    
print(contar_ocorrencias(texto, procurado))'''

'''def somar_digitos(n):
    if n == 0:
        return 0
    
    return somar_digitos(n//10) + n % 10

print(somar_digitos(n))'''

'''texto = input("Digite o texto: ")
def contar_letras(texto):
    if texto == "":
        return 0
    
    return 1 + contar_letras(texto[1:]) 

print(contar_letras(texto))'''


'''def listar_maior(lista):
    if len(lista) == 1:
        return lista[0]
    
    primeiro = lista[0]
    maior_do_resto = listar_maior(lista[1:])

    if primeiro > maior_do_resto:
        return primeiro
    else:
        return maior_do_resto
    
print(listar_maior([2, 5, 1, 9, 13, 4, 21, 7, 19]))'''

'''def contar_pares(lista):
    if len(lista) == 1:
        if lista[0] % 2 == 0:
            return 1
        else:
            return 0 
    
    proximo = contar_pares(lista[1:])

    if lista[0] % 2 == 0:
        return 1 + proximo
    else:
        return proximo
    
print(contar_pares([2, 4, 5, 7, 8, 9, 11, 12, 14, 17]))'''

'''def achatar_lista(lista):
    if len(lista) == 1:
        return lista[0]
    
    atual = lista[0]

    return atual + achatar_lista(lista[1:])

print(achatar_lista([12, 4, 23, 2, 7, 18]))'''

'''texto = input("Digite essa bagaça doida: ")
def contar_palavras(texto):
    if texto == "":
        return 1
    
    if texto[0] == " ":
        return 1 + contar_palavras(texto[1:])
    else:
        return contar_palavras(texto[1:])
    
print(contar_palavras(texto))'''

'''n = int(input("Digite: "))
def e_primo(n, divisor):
    if n == 0 or n == 1:
        return False
    
    if n == divisor:
        return True
    elif n % divisor == 0:
        return False 
    else: 
        return e_primo(n, divisor + 1)
    
    
print(e_primo(n, divisor=2))'''