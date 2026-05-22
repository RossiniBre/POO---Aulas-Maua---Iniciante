'''def apresentar(nome, idade, altura):
    return f"Nome: {nome} | Idade: {idade} anos | Altura: {altura}m"

print(apresentar("Breno", 18, 1.84))'''

'''def classificar_idade(idade):
    if idade < 12:
        classe = "Criança"
    elif 12 <= idade <= 17:
        classe = "Adolescente"
    elif 18 <= idade <= 59:
        classe = "Adulto"
    elif idade >= 60:
        classe = "Idoso"

    return classe

print(f"Classificação: {classificar_idade(18)}")'''

'''def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

tabuada(10)'''

'''
def resumo(numeros):
    d = {}
    d['maior'] = max(numeros)
    d['menor']  = min(numeros)
    d['soma']  = sum(numeros)
    d['media'] = round(soma/len(numeros), 2)

    return d

print(resumo([2, 5, 6, 7, 9, 11, 3, 4]))'''

def analisar_texto(texto):
    palavras = texto.split()

    # contar vogais do jeito que você já fez antes
    vogais = 0
    for c in texto.lower():
        if c in "aeiou":
            vogais += 1

    # palavra mais longa do jeito manual
    longa = palavras[0]
    for palavra in palavras:
        if len(palavra) > len(longa):
            longa = palavra

    return {
        "quantidade de palavras": len(palavras),
        "vogais": vogais,
        "palavra mais longa": longa
    }

print(analisar_texto("I wish I was special, But Im a creep"))