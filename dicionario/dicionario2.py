'''def agenda():
    d = {}
    while True:
        print("1 - Adicionar\n2 - Buscar\n3 - Remover\n4 - Sair")
        n = int(input("Oque deve ser feito? "))
        if n == 1:
            nome = input("Digite o nome: ").lower()
            telefone = input("Digite o telefone: ")
            d[nome] = telefone
            print(f"{nome} adicionado a sua agenda")
        elif n == 2:
            nome = input("Quem voce deseja buscar?: ").lower()
            if nome in d:
                print(f"{nome}: {d[nome]}")
            else:
                print("Nome não foi encontrado")
        elif n == 3:
            if not d:                       
                print("Agenda vazia")
            else:
                for nome, telefone in d.items():
                    print(f"{nome}: {telefone}")
                print()
                x = input("Quem você quer remover? ").lower()
                if x in d:
                    del d[x]
                    print(f"{x} removido")
                else:
                    print("Nome não foi encontrado")
                    
        elif n == 4:
            print("Saindo...")
            break

agenda()'''

