contador = 0
frase = "A arara ama acerola"
frase = frase.lower()
for i in frase:
    if i == "a":
        contador += 1

print(contador)

isso = "  olá mundo  "
isso = isso.strip().upper()
print(isso)

banana = "BANANA"
banana = banana.lower().replace("a", "@")
print(banana)

nomes = "João,Maria,Carlos,Ana"
nomes = nomes.split(",")
nomes.sort()
# nomes = " ".join(nomes)
print(nomes)

mentira = ["Python", "é", "top"]
mentira = " ".join(mentira)
print(mentira)

duplicatas = [3, 1, 2, 3, 1, 4]
sem = []
for k in duplicatas:
    if k not in sem:
        sem.append(k)

print(sem)