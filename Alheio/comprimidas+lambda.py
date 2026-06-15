dobro = lambda n: n * 2
dobrar = [dobro(n) for n in [1, 2, 3, 4, 5]]
print(dobrar)

tamanho = lambda n: len(n) > 3
nomes = [n for n in ["ana", "beto", "carlos", "di"] if tamanho(n)]
print(nomes)

par = lambda n : n % 2 == 0
pares = [par(n) for n in [1, 2, 3, 4, 5, 6]]
print(pares)

nomes_outra = lambda n : n.strip().upper()
novo_nomes = [nomes_outra(n) for n in ["  ana  ", " beto", "carlos "]]
print(novo_nomes)

lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
soma = lambda i, j: i + j
listasoma = [soma(i, j) for i, j in zip(lista1, lista2)]
print(listasoma)