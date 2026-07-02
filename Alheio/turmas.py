turmas = {
    "3A": [("Ana", 8.5), ("Bruno", 6.0), ("Carla", 9.2)],
    "3B": [("Diego", 7.0), ("Elisa", 9.5), ("Fabio", 8.8)],
    "3C": [("Gustavo", 9.9), ("Helena", 4.0)]
}


def melhor_aluno_por_turma(turmas):
    melhor = {}
    for turma, alunos in turmas.items():
        melhor[turma] = max(alunos, key=lambda n: n[-1])
    return melhor

print(melhor_aluno_por_turma(turmas))

estoque = {
    "eletronicos": {"mouse": 15, "teclado": 8, "monitor": 3},
    "papelaria": {"caneta": 0, "caderno": 2, "borracha": 0},
    "limpeza": {"detergente": 12, "sabao": 0, "esponja": 30}
}

def produtos_em_falta(estoque):
    em_falta = []
    for categoria, produtos in estoque.items():
        for produto, quantidade in produtos.items():
            if quantidade == 0:
                em_falta.append(produto)
            
    return em_falta

print(produtos_em_falta(estoque))