n = 5
if n > 0:
    print("Positivo")
elif n == 0:
    print("Zero")
else:
    print("Negativo")

numeros = [50, 40, 30]
num1, num2, num3 = numeros
if num1 > num2 and num1 > num3:
    print("numero 1 é o maior")
elif num2 > num1 and num2 > num3:
    print("numero 2 é o maior")
else:
    print("numero 3 é o maior")

ano = int(input("Digite o ano: "))
if ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0 :
    print("É bissexto")
else:
    print("Não é bissexto")
if ano % 100 <= 34: # pesquisei como ver os ultimos digitos do numero
    print("Começo do ano")
elif ano % 100 >= 35 and ano % 100 <= 74:
    print("Meio do ano")
else:
    print("Fim do ano")

