def calcula_frequencia(faltas, total_aulas):
    frequencia = (total_aulas - faltas) / total_aulas * 100
    return round(frequencia, 1)

alunos = ['Ana', 'Bruno', 'Carla', 'Diego', 'Elena']
faltas = [2, 8, 1, 5, 10]
total_aulas = [20, 20, 20, 20, 20]

def dicionario_frequencia(alunos, faltas, total_aulas):
    d = {}
    for aluno, falta, total in zip(alunos, faltas, total_aulas):
        d[aluno] = calcula_frequencia(falta, total)

    return d

def pega_frequencia(item):
    return item[1]  

def ordena_frequencia(d):
    return dict(sorted(d.items(), key=pega_frequencia))

d = dicionario_frequencia(alunos, faltas, total_aulas)
print(ordena_frequencia(d))