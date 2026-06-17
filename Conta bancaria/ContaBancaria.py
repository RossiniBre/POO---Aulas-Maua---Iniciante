class ContaBancaria:
    id_auto = 0
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo
        self._historico = []
        ContaBancaria.id_auto += 1
        self.__id_auto = ContaBancaria.id_auto

    # saldo ==================================
    @property
    def saldo(self):
        return self._saldo 
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo inválido")
        self._saldo = valor
        
    # id ==================================
    @property
    def id(self):
        return self.__id_auto
    
    #comportamentos
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.append(f"Novo depósito de {valor} | Saldo atual: {self._saldo} | Realizada Por: {self.titular}")
        else:
            return f"Apenas faça depósitos válidos"
        return self._saldo

    def sacar(self, valor):
        if self._saldo > 0 and self._saldo >= valor:
            self._saldo -= valor
            self._historico.append(f"Novo saque de {valor} | Saldo atual: {self._saldo} | Realizada Por: {self.titular}")
        else:
            return f"Saque indisponível, seu saldo atual é de {self._saldo}"

        return self._saldo
    
    def extrato(self):
        return f"O histórico de transações: {self._historico}"