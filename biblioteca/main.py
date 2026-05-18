from usuario import *

user1 = cadastrar_usuario("Breno", "Harry Potter", 2, 12)
user2 = cadastrar_usuario("Pedro", "Duna", 0, 0)

for user in [user1, user2]:
    print("===== Ficha de Usuário =====")

    print(f"Nome: {user['nome']}")

    print(f"Livro: {user['livro']}")

    print(f"Status: {user['status']}", " | ",
          f"Quantidade: {user['quantidade']}")
    
    print(f"Multa: {user['multa']:.2f}R$")

    print()