def calcular_media(notas):
    media = 0
    for n in notas:
        media += n
    media /= len(notas)
    return media

def verificar_situacao(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else: 
        return "Reprovado"

def exibir_relatorio(nome, notas):
    cal_media = calcular_media(notas)
    situacao = verificar_situacao(cal_media)
    print("Aluno: ", nome)
    print("Notas: ", notas)
    print("Média: ", cal_media)
    print("Situação: ", situacao)
    
exibir_relatorio("João", [7, 8, 5, 9])