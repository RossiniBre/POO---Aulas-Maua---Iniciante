lista = [1, 2, 3, 4, 5]

multiplicado3 = [n * 3 for n in lista]
print(multiplicado3)

impares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = [n for n in impares if n % 2 == 1]
print(impares)

nomes = ["ana", "beto", "carlos", "di"]
tamanho = [len(n) for n in nomes] 
print(tamanho)

novo_nomes = [n for n in nomes if len(n) > 3]
print(novo_nomes)

semespaco = ["  ana  ", " beto", "carlos "]
semespaco = [n.strip().upper() for n in semespaco]
print(semespaco)

soma = [1, 2, 3]
soma2 = [10, 20, 30]
soma_final = [i + j for i, j in zip(soma, soma2)]
print(soma_final)

quadrados = [n **2 for n in [1, 2, 3, 4, 5, 6] if n % 2 == 0]
print(quadrados)

