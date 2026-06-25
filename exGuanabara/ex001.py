class Diario:
    def __init__(self, senha):
        self.__segredos = []
        self.__senha = senha

    # segredos
    @property
    def segredo(self):
        return self.__segredos
    
    #senha
    @property
    def senha(self):
        return "Ninguem tem permissão a está senha"
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha
        return
        
        
    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha):
        if senha == self.__senha:
            return self.__segredos
        else:
            return f"Senha {senha} incorreta!"


d = Diario("3421")
d.escrever("Primeira mensagem")
d.escrever("Segunda mensagem")
d.senha = "2345"
print(d.ler("2345"))
print(d.senha)