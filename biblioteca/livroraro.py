from Biblioteca import Livro

class LivroRaro(Livro):
    def __init__(self, titulo, autor, isbn, valor_seguro):
        super().__init__(titulo, autor, isbn)
        self._valor_seguro = valor_seguro
        self._diasMaximos = 3

    #valor seguro
    @property
    def valor_seguro(self):
        return self._valor_seguro
    
    @valor_seguro.setter
    def valor_seguro(self, valor_seguro):
        if valor_seguro <= 0:
         raise ValueError("Valor não é seguro")
        else:
           self._valor_seguro = valor_seguro
    
    def emprestar(self):
       print(
             f"O valor do empréstimo é de R${self._valor_seguro} e voce tem no máximo {self._diasMaximos} dias para devolver"
       )
       return super().emprestar()

raro = LivroRaro("Bíblia de Gutenberg", "Desconhecido", "1234567890123", 50000)
raro.emprestar()
# imprime o aviso
# depois imprime/retorna "Emprestimo realizado"

raro.emprestar()
# imprime o aviso de novo
# depois "Livro indisponivel" (porque já está emprestado)

raro.valor_seguro = 20  # ValueError