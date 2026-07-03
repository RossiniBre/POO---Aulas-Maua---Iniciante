package Biblioteca;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        Biblioteca biblioteca = new Biblioteca();

        while (true) {

            System.out.println("1 - Adicionar livro");
            System.out.println("2 - Listar livros");
            System.out.println("3 - Buscar livro");
            System.out.println("4 - Remover livro");
            System.out.println("0 - Sair");

            int opcao = input.nextInt();
            input.nextLine();

            switch (opcao) {

                case 1:
                    System.out.print("Titulo: ");
                    String titulo = input.nextLine();

                    System.out.print("Autor: ");
                    String autor = input.nextLine();

                    System.out.print("Ano: ");
                    int ano = input.nextInt();
                    input.nextLine();

                    biblioteca.adicionarLivro(titulo, autor, ano);
                    break;

                case 2:
                    biblioteca.listarLivros();
                    break;

                case 3:
                    System.out.print("Digite ID: ");
                    int idBusca = input.nextInt();
                    input.nextLine();

                    biblioteca.buscarLivro(idBusca);
                    break;

                case 4:
                    System.out.print("Digite ID: ");
                    int idRemove = input.nextInt();
                    input.nextLine();

                    biblioteca.removerLivro(idRemove);
                    break;

                case 0:
                    System.out.println("Saindo...");
                    input.close();
                    return;

                default:
                    System.out.println("Opção inválida!");
            }
        }
    }
}