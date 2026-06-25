def soma_digitos(n):
    if n <= 0:
        return n
    
    return soma_digitos(n //10) + n % 10

print(soma_digitos(1234))


def letra(texto):
    texto = texto.split()
    nova_texto = []
    for i in texto:
        nova_texto.append(i[0].upper() + i[1:])

    nova_texto = " ".join(nova_texto)
    return nova_texto

print(letra("será que tá certo isso?"))