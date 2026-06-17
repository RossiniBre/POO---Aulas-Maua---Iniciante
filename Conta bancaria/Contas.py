from ContaBancaria import ContaBancaria
from ContaPoupanca import ContaPoupanca

# Conta bancária comum
conta = ContaBancaria("Breno", 1000)

print("=== CONTA BANCÁRIA ===")
print("Titular:", conta.titular)
print("Saldo inicial:", conta.saldo)
print("ID:", conta.id)

conta.depositar(500)
conta.sacar(200)

print("Saldo final:", conta.saldo)
print(conta.extrato())

print()

# Conta poupança
poupanca = ContaPoupanca(0.05, "Gabrielly", 1000)

print("=== CONTA POUPANÇA ===")
print("Titular:", poupanca.titular)
print("Saldo inicial:", poupanca.saldo)
print("Taxa de juros:", poupanca.taxa_juros)
print("ID:", poupanca.id)

poupanca.render_juros()

print("Saldo após juros:", poupanca.saldo)
print(poupanca.extrato())

print()

# Testando IDs diferentes
print("ID conta comum:", conta.id)
print("ID conta poupança:", poupanca.id)

print()

# Testando atributo privado
try:
    print(conta.__id_auto)
except AttributeError as e:
    print("Erro esperado:", e)

# Testando name mangling
print("Acesso via name mangling:")
print(conta._ContaBancaria__id_auto)