n = int(input("Numero positivo ao usuário: "))
maior = menor = soma = qntd = 0
numero = n
#quantidade
while numero > 0:
    ultimo = numero % 10
    numero = numero // 10
    soma += ultimo
    qntd += 1
    maior = ultimo if maior < ultimo else maior
    menor = ultimo
    menor = ultimo if menor > ultimo else menor

print(f"Quantidade de algarismos: {qntd}")
print(f"Soma dos algarismos: {soma}")
print(f"Maior dos algarismos: {maior}")
print(f"Menor dos algarismos: {menor}")
print("====================================\n")

meu_jeito = []
meu_jeito.extend(str(n))
print(f"Quantidade de algarismos: {len(meu_jeito)}")
print(f"Soma dos algarismos: {sum([int(s) for s in meu_jeito])}")
print(f"Maior dos algarismos: {max(meu_jeito)}")
print(f"Menor dos algarismos: {min(meu_jeito)}")