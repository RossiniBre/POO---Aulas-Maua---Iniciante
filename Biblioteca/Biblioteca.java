package Biblioteca;

import java.util.ArrayList;

public class Biblioteca {

    private ArrayList<Livro> livros = new ArrayList<>();

    public void adicionarLivro(String titulo, String autor, int ano) {
        livros.add(new Livro(titulo, autor, ano));
        System.out.println("Livro adicionado!");
    }

    public void listarLivros() {
        if (livros.isEmpty()) {
            System.out.println("Não há livros!");
            return;
        }

        for (Livro livro : livros) {
            livro.exibirInformacoes();
        }
    }

    public void buscarLivro(int id) {

        for (Livro livro : livros) {
            if (livro.getId() == id) {
                livro.exibirInformacoes();
                return;
            }
        }

        System.out.println("Livro não encontrado");
    }

    public void removerLivro(int id) {

        for (int i = 0; i < livros.size(); i++) {
            if (livros.get(i).getId() == id) {
                livros.remove(i);
                System.out.println("Livro removido!");
                return;
            }
        }

        System.out.println("Livro não encontrado");
    }
}