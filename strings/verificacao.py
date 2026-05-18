while True: 
    senha = input("Digite a senha: ")
    if senha == "0":
        break

    def verificacao(senha):
        maiusculo = False
        numero = False
        
        for i in senha:
            if i.isupper():
                maiusculo = True
            if i.isdigit():
                numero = True

        if len(senha) >= 8 and maiusculo and numero:
            return "Senha valida"
        else:
            return "Senha inválida"

    print(verificacao(senha))