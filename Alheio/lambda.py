quadrado = lambda n: n ** 2
print(quadrado(5))

maior = lambda n, j: n if n > j else j
print(maior(8, 6))

letraA = lambda n: True if n.lower().startswith('a') else False
print(letraA("Alemanha"))

lista = lambda n: n[-1]
print(lista([1, 2, 3, 4, 5]))

impar_par = lambda n : "par" if n % 2 == 0 else "impar"
print(impar_par(10))