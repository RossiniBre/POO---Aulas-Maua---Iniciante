from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, taxa_juros, titular, saldo):
        super().__init__(titular, saldo)
        self._taxa_juros =  taxa_juros

    # taxa juros
    @property
    def taxa_juros(self):
        return self._taxa_juros

    @taxa_juros.setter
    def taxa_juros(self, juros):
        if juros < 0 or juros > 1.0:
            raise ValueError("Taxa inválida")
        else:
            self._taxa_juros = juros
        
    def render_juros(self):
        juros = self._saldo * self._taxa_juros
        self._saldo += juros
        self._historico.append(f"Juros de {juros} aplicados | Saldo: {self._saldo}")


