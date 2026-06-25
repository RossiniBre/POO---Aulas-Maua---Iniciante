class Retangulo:
    def __init__(self, largura, altura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return self.largura*2 + self.altura*2


r = Retangulo(10, 5)
area = r.area()
perimetro = r.perimetro()

print(f"Area: {area} | Perimetro: {perimetro}")