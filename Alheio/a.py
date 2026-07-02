MEDIA_APROVACAO = 6


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def exibir_resultado(nota1, nota2, media, psub=None):
    status = "Aprovado" if media >= MEDIA_APROVACAO else "Reprovado"
    if psub is not None:
        print(f"{status} | P1: {nota1} | P2: {nota2} | PSub: {psub} | MP: {media:.2f}")
    else:
        print(f"{status} | P1: {nota1} | P2: {nota2} | MP: {media:.2f}")


def aplicar_substitutiva(p1, p2, psub):
    nova_p1 = psub if psub > p1 else p1
    nova_p2 = psub if psub > p2 else p2
    nova_media = calcular_media(nova_p1, nova_p2)

    exibir_resultado(p1, p2, nova_media, psub=psub)
    return nova_media


def avaliacao(p1, p2):
    media = calcular_media(p1, p2)
    exibir_resultado(p1, p2, media)

    if media < MEDIA_APROVACAO:
        print("PSub necessária!")
        psub = float(input("Digite sua nota da PSub: "))
        media = aplicar_substitutiva(p1, p2, psub)

    return media


def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")


if __name__ == "__main__":
    p1 = ler_nota("Digite sua nota na P1: ")
    p2 = ler_nota("Digite sua nota na P2: ")
    avaliacao(p1, p2)
