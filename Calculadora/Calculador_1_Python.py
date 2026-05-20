import math

while (True):
    print("Se quiser sair digite 0\n")
    n1 = float(input("Digite um valor: \n"))
    if n1 == 0:
        print("Saindo...\n")
        break 
    n2 = float(input("Digite um valor: \n"))
    print("=========================================")
    operador = input("Digite um dos operadores:\n | * | | / | | + | | - | :\n")
    print("=========================================")

    resultado = 0
   
    if operador == "*":
        resultado = n1 * n2
    elif operador == "+":
        resultado = n1 + n2
    elif operador == "/":
        resultado = n1/n2
    elif operador == "-":
        resultado = n1 - n2
    else:
        print("Operador selecionado inválido.")

    print(f"O resultado é {resultado: .2f}\n")