class Livro:
    codigo = 0
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self._isbn = isbn
        Livro.codigo += 1
        self.__cod = Livro.codigo
        self._disponivel = True

    #isbn
    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, isbn):
        if len(str(isbn)) != 13 or not str(isbn).isnumeric():
            raise ValueError("Deve ter 13 caracteres")
        else: 
            self._isbn = isbn
        
    #disponibilidade
    @property
    def disponivel(self):
        return self._disponivel
    
    #codigo interno
    @property
    def cod(self):
        return self.__cod
    
    # comportamentos
    def emprestar(self):
        if self._disponivel == False:
            return "Livro indisponivel"
        else:
            self._disponivel = False
            return "Emprestimo realizado"
        
    def devolver(self):
        if self._disponivel == False:
            self._disponivel = True
            return "Emprestimo finalizado"
        else:
            return "Voce ja devolveu este livro"
