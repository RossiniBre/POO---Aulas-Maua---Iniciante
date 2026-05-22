'''def contar_letras(texto):
    dicionario = {}

    for l in texto:
        if l in dicionario:
            dicionario[l]+=1
        else:
            dicionario[l] = 1  
    return dicionario

print(contar_letras("sociedadeesportivapalmeiras"))'''

'''def lista_alunos(alunos):

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

print(lista_alunos(alunos))'''

'''def contador_palavras(texto):
    texto = texto.lower()
    texto = texto.replace(",", "").replace(".", "")
    texto = texto.split()
    d = {}
    for palavra in texto:
        if palavra in d:
            d[palavra] += 1
        else:
            d[palavra] = 1

    ordenado = sorted(d.items(), key=lambda x: x[1], reverse=True)

    return ordenado

for palavra, total in contador_palavras("O rato roeu a roupa do rei de Roma. A rainha, com raiva, reclamou para o rei. O rei, surpreso, olhou para a roupa e viu que o rato ainda estava lá. O rato, sem vergonha, continuou roendo a roupa."):
    print(f"{palavra}: {total}")'''

'''def tradutor(palavra):
    
    if palavra in d:
        return d[palavra]
    else:
        return "Palavra não encontrada"

d = {
    "gato": "cat",
    "cachorro": "dog",
    "casa": "house",
    "carro": "car",
    "livro": "book",
    "água": "water",
    "comida": "food",
    "amigo": "friend",
    "sol": "sun",
    "lua": "moon"
    }

while True:
    palavra = input("Digite a palavra: ")

    if palavra == "sair":
        print("Saindo...")
        break
    else:
        print(tradutor(palavra))'''

produtos = [
    {'nome': 'Arroz Integral', 'preco': 5.90, 'categoria': 'Alimentos'},
    {'nome': 'Feijão Carioca', 'preco': 6.30, 'categoria': 'Alimentos'},
    {'nome': 'Macarrão Penne', 'preco': 4.20, 'categoria': 'Alimentos'},
    {'nome': 'Azeite de Oliva', 'preco': 17.90, 'categoria': 'Alimentos'},
    {'nome': 'Café Torrado', 'preco': 9.80, 'categoria': 'Alimentos'},
    {'nome': 'Shampoo Neutro', 'preco': 12.50, 'categoria': 'Higiene'},
    {'nome': 'Sabonete de Coco', 'preco': 2.90, 'categoria': 'Higiene'},
    {'nome': 'Creme Dental Menta', 'preco': 3.50, 'categoria': 'Higiene'},
    {'nome': 'Desodorante Spray', 'preco': 8.70, 'categoria': 'Higiene'},
    {'nome': 'Fio Dental 50m', 'preco': 5.60, 'categoria': 'Higiene'},
    {'nome': 'Detergente Limão', 'preco': 3.50, 'categoria': 'Limpeza'},
    {'nome': 'Sabão em Barra', 'preco': 4.00, 'categoria': 'Limpeza'},
    {'nome': 'Desinfetante Pinho', 'preco': 6.25, 'categoria': 'Limpeza'},
    {'nome': 'Esponja Multiuso', 'preco': 1.90, 'categoria': 'Limpeza'},
    {'nome': 'Álcool 70%', 'preco': 4.90, 'categoria': 'Limpeza'},
    {'nome': 'Liquidificador 500W', 'preco': 149.00, 'categoria': 'Eletrodomésticos'},
    {'nome': 'Ferro de Passar', 'preco': 89.90, 'categoria': 'Eletrodomésticos'},
    {'nome': 'Batedeira Compacta', 'preco': 119.90, 'categoria': 'Eletrodomésticos'},
    {'nome': 'Sanduicheira Grill', 'preco': 79.00, 'categoria': 'Eletrodomésticos'},
    {'nome': 'Ventilador Mesa 30cm', 'preco': 159.90, 'categoria': 'Eletrodomésticos'},
    {'nome': 'Pão de Forma', 'preco': 6.80, 'categoria': 'Alimentos'},
    {'nome': 'Leite Integral 1L', 'preco': 4.70, 'categoria': 'Alimentos'},
    {'nome': 'Achocolatado Pó', 'preco': 7.60, 'categoria': 'Alimentos'},
    {'nome': 'Escova de Dente', 'preco': 3.20, 'categoria': 'Higiene'},
    {'nome': 'Água Sanitária', 'preco': 2.50, 'categoria': 'Limpeza'},
    {'nome': 'Arroz Agulhinha', 'preco': 5.70, 'categoria': 'Alimentos'},
    {'nome': 'Arroz Parboilizado', 'preco': 6.10, 'categoria': 'Alimentos'},
    {'nome': 'Feijão Preto', 'preco': 6.90, 'categoria': 'Alimentos'},
    {'nome': 'Feijão Carioca Premium', 'preco': 7.50, 'categoria': 'Alimentos'},
    {'nome': 'Macarrão Espaguete', 'preco': 3.90, 'categoria': 'Alimentos'},
    {'nome': 'Macarrão Integral', 'preco': 4.80, 'categoria': 'Alimentos'},
    {'nome': 'Azeite Extra Virgem', 'preco': 22.50, 'categoria': 'Alimentos'},
    {'nome': 'Café Solúvel', 'preco': 10.90, 'categoria': 'Alimentos'},
    {'nome': 'Café Torrado Tradicional', 'preco': 8.90, 'categoria': 'Alimentos'},
    {'nome': 'Shampoo Anticaspa', 'preco': 13.40, 'categoria': 'Higiene'},
    {'nome': 'Shampoo Infantil', 'preco': 11.30, 'categoria': 'Higiene'},
    {'nome': 'Sabonete Neutro', 'preco': 3.10, 'categoria': 'Higiene'},
    {'nome': 'Creme Dental Infantil', 'preco': 4.20, 'categoria': 'Higiene'},
    {'nome': 'Desodorante Roll-on', 'preco': 7.90, 'categoria': 'Higiene'},
    {'nome': 'Desodorante Aerosol', 'preco': 9.40, 'categoria': 'Higiene'},
    {'nome': 'Detergente Neutro', 'preco': 3.20, 'categoria': 'Limpeza'},
    {'nome': 'Detergente Maçã', 'preco': 3.10, 'categoria': 'Limpeza'},
    {'nome': 'Sabão em Barra Neutro', 'preco': 4.10, 'categoria': 'Limpeza'},
    {'nome': 'Desinfetante Lavanda', 'preco': 6.40, 'categoria': 'Limpeza'},
    {'nome': 'Desinfetante Floral', 'preco': 6.15, 'categoria': 'Limpeza'},
    {'nome': 'Esponja Aço Inox', 'preco': 2.90, 'categoria': 'Limpeza'},
    {'nome': 'Álcool Gel', 'preco': 5.80, 'categoria': 'Limpeza'},
    {'nome': 'Liquidificador Turbo 700W', 'preco': 179.90, 'categoria': 'Eletrodomésticos'},
    {'nome': 'Ferro a Vapor', 'preco': 119.00, 'categoria': 'Eletrodomésticos'},
    {'nome': 'Batedeira Planetária', 'preco': 219.90, 'categoria': 'Eletrodomésticos'},
    {'nome': 'Sanduicheira Dupla', 'preco': 99.00, 'categoria': 'Eletrodomésticos'},
    {'nome': 'Ventilador Coluna', 'preco': 189.90, 'categoria': 'Eletrodomésticos'},
    {'nome': 'Ventilador Turbo', 'preco': 179.90, 'categoria': 'Eletrodomésticos'},
    {'nome': 'Leite Desnatado 1L', 'preco': 4.60, 'categoria': 'Alimentos'},
    {'nome': 'Leite Semidesnatado 1L', 'preco': 4.80, 'categoria': 'Alimentos'}
]

def filtrar_por_nome(lista, palavra):
    resultado = []
    for produto in lista:
        if palavra.lower() in produto["nome"].lower():
            resultado.append(produto)
    return resultado

print("Busca por 'arroz':")
for prod in filtrar_por_nome(produtos, 'arroz'):
  print(prod)
print("\nBusca por 'shampoo':")
for prod in filtrar_por_nome(produtos, 'shampoo'):
  print(prod)