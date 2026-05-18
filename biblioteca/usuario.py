from livro import verificar_disponibilidade
from multa import calcular_multa

def cadastrar_usuario(nome, livro, quantidade, dias_atraso):
    cadastro = {
        'nome' : nome,
        'livro' : livro,
        'quantidade' : quantidade,
        'status' : verificar_disponibilidade(quantidade),
        'multa' : calcular_multa(dias_atraso)
    }
    return cadastro