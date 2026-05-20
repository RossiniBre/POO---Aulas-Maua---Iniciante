"========================="
'''def impar_ou_par():
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        return f"{num} é par"
    else:
        return f"{num} é ímpar"
    
print(impar_ou_par())'''
"========================="
'''def temperatura():
    temp = float(input("Qual a temperatura atual?: "))
    if temp < 15:
        return f"{temp} está frio!"
    elif temp >= 15 and temp <= 25:
        return f"{temp} é uma Temperatura agradável!"
    else:
        return f"{temp} está quente!"
    
print(temperatura())'''
"========================="
'''def tabuada(num):
    for i in range(1, 11):
        produto = i * num
        print(f"{num} x {i} = {produto}")

num = int(input("Digite um valor: "))
tabuada(num)'''
"========================="
'''def soma_lista(lista):
    total = 0
    for i in lista:
        total += i
    return total

lista = [1, 4, 6, 7]
print(soma_lista(lista))'''
"========================="
'''def filtrar_pares(lista, elementos):
    for i in range(elementos):
        indice = int(input(f"Digite {i+1}º valor: "))
        if indice % 2 == 0:
            lista.append(indice)
            lista.sort()        
    return lista

elementos = int(input("Qual o tamanho da lista?: "))
lista = []
print(filtrar_pares(lista, elementos))'''
"========================="
'''import math
def hipotenusa(cat1, cat2):
    hip = (cat1**2) + (cat2**2)
    hip = math.sqrt(hip)
    return f"{hip:.2f}"

cat1 = float(input("Qual o valor do primeiro cateto?: "))
cat2 = float(input("Qual o valor do segundo cateto?: "))
print(hipotenusa(cat1, cat2))'''
"========================="
'''def entrada(user, senha):
    mensagem = ""
    if user == "admin" and senha == "1234":
        mensagem = "Bem vindo, admin!"
    elif user != 'admin' and senha == "1234": 
        mensagem = "Usuário incorreto"
    elif user == "admin" and senha != "1234":
        mensagem = "Senha incorreta!"
    else:
        mensagem = "Usuário e senha incorretos"
    
    return mensagem

user = input("Digite o usuário: ").lower()
senha = input("Digite a senha: ").lower()
print(entrada(user, senha))'''
"========================="
'''def contagem(inicio):
    for i in range(inicio, -1, -1):
        print(i)
    return i 

inicio = int(input("Digite um valor: "))
(contagem(inicio))
print("Lançamento!")'''
"========================="

