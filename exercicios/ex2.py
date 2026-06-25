fila = [("A1", "normal"), ("A2", "urgente"), ("A3", "normal"), ("A4", "urgente")]
urgente = 0
comum = 0

for x in fila:
    if x[1] == "urgente":
        print(f"Atendendo senha {x[0]} (prioridade: {x[1]})")
        urgente += 1

for y in fila:
    if y[1] == "normal":
        print(f"Atendendo senha {y[0]} (prioridade: {y[1]})")
        comum += 1 

print(f"Urgentes atendidas: {urgente}")
print(f"Normais atendidas: {comum}")

lista = [("Ana", 8.5), ("Bruno", 6.0), ("Carla", 9.2)]
dic = {}
for i in lista:
    if i[1] >= 7:
        dic[i[0]] = i[1]

for i in dic.keys():
    print(i)
