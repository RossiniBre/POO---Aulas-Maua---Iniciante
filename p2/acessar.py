frutas = ["maçã", "banana", "uva", "manga"]
penultimo = frutas[-2]
print(penultimo)

texto = "radar"
for indice, valor in enumerate(texto):
    print(f"{indice} - {valor}")

coisa_ruim = [[1,2],[3,4],[5,6]]
print(coisa_ruim[1][1])

palavra = input("Palavra: ")
print("primeira:", palavra[0])
print("ultima:", palavra[-1])