from imc import calculo_imc, classificar_imc
from treino import sugerir_treino


def cadastrar_aluno(nome, peso, altura):

    imc = calculo_imc(peso, altura)
    classificacao = classificar_imc(imc)
    treino = sugerir_treino(classificacao)

    cadastro = {
        "nome": nome,
        "peso": peso,
        "altura": altura,
        "imc": imc,
        "classificacao": classificacao,
        "treino": treino
    }

    return cadastro