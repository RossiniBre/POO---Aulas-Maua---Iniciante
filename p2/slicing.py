texto = "Python é incrivel"
print(texto[9:])

lista = [1, 2, 3, 4, 5]
lista = lista[::-1]
print(lista)

lista2 = [10, 20, 30, 40, 50, 60]
pares = []
for indice, valor in enumerate(lista2):
    if indice % 2 == 0:
        pares.append(valor)

print(pares)

texto2 = "abcdefghij"
texto2 = texto2[::-2]
print(texto2)

lista2 = [1,2,3]
lista3 = lista2[:]
lista3.append(4)
print(lista2)
print(lista3)