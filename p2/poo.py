class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __str__(self):
        return f"Retangulo {self.base}x{self.altura}"

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base + self.altura) * 2
    
r = Retangulo(8, 5)
j = Retangulo(20, 10)
print(r.area(), j.area())
print(r.perimetro(), j.perimetro())
print(r)

class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor 
        return self.saldo 

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo
        else:
            return "Saldo indisponivel"
    def ver_saldo(self):
        return f"{self.saldo}"
    
p = Conta(3000)
p.depositar(500)
p.sacar(200)
print(p.ver_saldo())

class Animal:
    def __init__(self, nome):
       self.nome = nome

    def falar(self):
        pass
    
class Gato(Animal):
    def falar(self):
        return f"{self.nome} diz miau"
    
class Cachorro(Animal):
    def falar(self):
        return f"{self.nome} diz au au"

gato = Gato("Alvin")
cachorro = Cachorro("Meg")
lista = [gato, cachorro]
for i in lista:
    print(i.falar())

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

p = Produto("Celular", 3000, 34)

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def remover(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                return

    def total_em_estoque(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco * produto.quantidade
        return total

estoque = Estoque()
estoque.adicionar(p) 
print(p)