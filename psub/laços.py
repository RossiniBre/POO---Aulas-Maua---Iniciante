# for i in range(1, 50 + 1):
#     if i % 3 == 0:
#         print(i)

soma = 0
i = 0
while True:
    n = input(f"Digite o numero {i+1}: ")

    if n == "sair":
        break
    i +=1

    soma += int(n)
   
media = soma/i if i > 0 else 0
print("Soma dos números:", soma)
print("Média dos números:", media)
print("Qntd de números:", i)