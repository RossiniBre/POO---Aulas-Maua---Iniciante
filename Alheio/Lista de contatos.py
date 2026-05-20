contatos = []

while True:
    print("\n[1] Adicionar Contato")
    print("[2] Remover Contato")
    print("[3] Alterar Contato")
    print("[4] Buscar Contato")
    print("[5] Mostrar todos contatos")
    print("[6] Ordenar [A-Z]")
    print("[7] Ordenar [Z-A]")
    print("[8] Sair")

    Oque_fazer = int(input("Oque deve ser fazido? "))

    if Oque_fazer == 1:
        add_Nome = input("Nome do contato: ")
        add_Telefone = input("Telefone do contato: ")
        contato = {"nome": add_Nome, "telefone": add_Telefone}
        contatos.append(contato)
        print(f"Contato '{add_Nome}' adicionado com sucesso!")

    elif Oque_fazer == 2:
        if not contatos:
            print("Nenhum contato cadastrado.")
        else:
            busca = input("Nome do contato a remover: ")
            encontrado = None
            for c in contatos:
                if c["nome"].lower() == busca.lower():
                    encontrado = c
                    break
            if encontrado:
                contatos.remove(encontrado)
                print(f"Contato '{busca}' removido com sucesso!")
            else:
                print("Contato não encontrado.")

    elif Oque_fazer == 3:
        if not contatos:
            print("Nenhum contato cadastrado.")
        else:
            busca = input("Nome do contato a alterar: ")
            encontrado = None
            for c in contatos:
                if c["nome"].lower() == busca.lower():
                    encontrado = c
                    break
            if encontrado:
                novo_nome = input(f"Novo nome ({encontrado['nome']}): ") or encontrado["nome"]
                novo_tel = input(f"Novo telefone ({encontrado['telefone']}): ") or encontrado["telefone"]
                encontrado["nome"] = novo_nome
                encontrado["telefone"] = novo_tel
                print("Contato alterado com sucesso!")
            else:
                print("Contato não encontrado.")

    elif Oque_fazer == 4:
        if not contatos:
            print("Nenhum contato cadastrado.")
        else:
            busca = input("Nome do contato a buscar: ")
            encontrados = [c for c in contatos if busca.lower() in c["nome"].lower()]
            if encontrados:
                print(f"\n{len(encontrados)} contato(s) encontrado(s):")
                for c in encontrados:
                    print(f"  Nome: {c['nome']} | Telefone: {c['telefone']}")
            else:
                print("Nenhum contato encontrado.")

    elif Oque_fazer == 5:
        if not contatos:
            print("Nenhum contato cadastrado.")
        else:
            print(f"\nTotal: {len(contatos)} contato(s):")
            for i, c in enumerate(contatos, 1):
                print(f"  {i}. Nome: {c['nome']} | Telefone: {c['telefone']}")

    elif Oque_fazer == 6:
        if not contatos:
            print("Nenhum contato cadastrado.")
        else:
            contatos.sort(key=lambda c: c["nome"].lower())
            print("Contatos ordenados de A-Z:")
            for i, c in enumerate(contatos, 1):
                print(f"  {i}. Nome: {c['nome']} | Telefone: {c['telefone']}")

    elif Oque_fazer == 7:
        if not contatos:
            print("Nenhum contato cadastrado.")
        else:
            contatos.sort(key=lambda c: c["nome"].lower(), reverse=True)
            print("Contatos ordenados de Z-A:")
            for i, c in enumerate(contatos, 1):
                print(f"  {i}. Nome: {c['nome']} | Telefone: {c['telefone']}")

    elif Oque_fazer == 8:
        print("Saindo... Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")