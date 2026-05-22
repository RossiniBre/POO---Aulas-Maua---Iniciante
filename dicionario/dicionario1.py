'''def contar_letras(texto):
    dicionario = {}

    for l in texto:
        if l in dicionario:
            dicionario[l]+=1
        else:
            dicionario[l] = 1  
    return dicionario

print(contar_letras("sociedadeesportivapalmeiras"))'''

def lista_alunos(alunos):

    aprovados = []
    
    for aluno in alunos:
        soma = 0
        for nota in aluno["notas"]:
            soma += nota

        media = soma/len(aluno["notas"])

        if media >= 6:
            aprovados.append(aluno)

    return aprovados

alunos = [
    {"nome": "João", "notas": [7, 8, 6]},
    {"nome": "Ana",  "notas": [4, 3, 5]}
]

print(lista_alunos(alunos))

