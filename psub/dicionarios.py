def ordena_dic(dic):
    novo_dic = {}
    for chave, valor in dic.items():
        novo_dic[chave] = sorted(valor)
    return novo_dic

x = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
y = {'nomes':['Gabriela', 'Jorge', 'Alvaro', 'Zulmira'],
     'sobrenomes':['Pontes', 'Silva', 'Arantes']}
print(ordena_dic(x))
print(ordena_dic(y))       


def mais_caros(dic):
    ordenado = sorted(dic.values(), reverse=True)
    return [ordenado[0], ordenado[1], ordenado[2]]


compra = {  
    'item1': 45.50,
    'item2':35,
    'item3': 41.30,
    'item4':55,
    'item5':24
}

top3 = mais_caros(compra)
print(top3)

# Exercício 03
def calcula_medias(lista_dic):
  outra = [] 
  media = 0
  for aluno in lista_dic:
    media = (aluno['P1'] + aluno['P2']) / 2
    outra.append({"RA" : aluno['RA'] , "Média" : media})

  return outra

notas_alunos = [{'RA':'0123', 'P1':6.5, 'P2':8.5},
                {'RA':'2189', 'P1':10.0, 'P2':6.0},
                {'RA':'3577', 'P1':3.5, 'P2':7.0}]
medias_alunos = calcula_medias(notas_alunos)
print(medias_alunos)

