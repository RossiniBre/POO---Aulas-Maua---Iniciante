sequencia = int(input("Qual o tamanho de sua sequência?: "))
lista = []

for i in range(sequencia):
    n = int(input(f"Digite o número {i + 1}: "))
    lista.append(n)

lista.sort()
print("Sua sequencia:", lista)
print("Maior número:", max(lista))
print("Menor número:", min(lista))
print("Soma da sequência:", sum(lista))