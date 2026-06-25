def triangulo(a, b, c):
    lista_temp = [a, b, c]
    lista_temp.sort()
    maior = lista_temp.pop(-1)
    soma = sum(x**2 for x in lista_temp)

    
    if (a + b) > c and (b + c) > a and (a + c) > b:
        if a == b == c:
            print("equilatero")
        elif a == b or b == c or a == c:
            print("isósceles")
        elif a != b and b != c and a != c:
            print("escaleno")
        
        if maior**2 < soma:
            print("acutangulo")
        elif maior**2 > soma:
            print("obtusangulo")
        else:
            print("retangulo")
    else:
        print("triangulo inválido!")
    
    
for lados in [(3, 4, 5), (5, 5, 6), (5, 5, 5), (5, 5, 8), (2, 2, 3.9), (1, 1, 5)]:
    print(lados, "->")
    triangulo(*lados)
    print()