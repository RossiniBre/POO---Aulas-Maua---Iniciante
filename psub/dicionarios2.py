import unicodedata
import matplotlib.pyplot as plt

def hist_palavras(txt):
  dic = {}
  txt = txt.lower()
  txt = txt = unicodedata.normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
  for i in txt:
     if i.isalpha():
        dic[i] = 0
  for i in txt:
    if i.isalpha():
        dic[i] += 1

  return dic

# Texto de entrada
texto = '''Minha terra tem palmeiras,
Onde canta o Sabiá;
As aves, que aqui gorjeiam,
Não gorjeiam como lá.'''

# Gera o histograma
frequencia = hist_palavras(texto)


# Imprime o dicionário
print(frequencia)

# Gráfico
letras = list(frequencia.keys())
contagens = list(frequencia.values())

plt.bar(letras, contagens)
plt.xlabel('Letra')
plt.ylabel('Frequência')
plt.title('Histograma de letras')
plt.show()



#funcao inverter
def inverter_histograma(hist):
   invert = {}
   novo_valor = []
   for chave, valor in hist.items():
      if valor in invert:     
        novo_valor.append(chave)
      else:
       invert[valor] = novo_valor

   return invert

# Inverte o histograma
invertido = inverter_histograma(frequencia)


# Exibe o dicionário invertido ordenado por frequência
print(invertido)