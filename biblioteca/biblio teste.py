from Biblioteca import Livro
from livroraro import LivroRaro

def linha(titulo):
    print("\n" + "=" * 50)
    print(titulo)
    print("=" * 50)

# ---------------------------------------------------------
livro1 = Livro("Dom Casmurro", "Machado de Assis", "1234567890123")
livro2 = Livro("O Cortiço", "Aluísio Azevedo", "9876543210123")

print(livro1.emprestar())   # Emprestimo realizado
print(livro1.emprestar())   # Livro indisponivel (já emprestado)
print(livro1.devolver())    # Emprestimo finalizado
print(livro1.devolver())    # Voce ja devolveu este livro