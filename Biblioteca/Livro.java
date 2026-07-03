package Biblioteca;

public class Livro {

    private String titulo;
    private String autor;
    private int ano;
    private boolean disponivel;
    private static int contador = 1;
    private int id;

    public Livro(String titulo, String autor, int ano) {
      this.titulo = titulo;
      this.autor = autor;
      this.ano = ano;
      this.disponivel = true;
      this.id = contador++;
    }

    // Getters e Setters
    public String getTitulo() {
      return this.titulo;
    }
    public void setTitulo(String titulo) {
      this.titulo = titulo;
    }

    public String getAutor() {
      return this.autor;
    }
    public void setAutor(String autor) {
      this.autor = autor;
    }

    public int getAno() {
      return this.ano;
    }
    public void setAno(int ano) {
      if (ano >= 1800 && ano <= 2026){
            this.ano = ano;
        }
    }

    public boolean isDisponivel() {
      return this.disponivel;
    }

    public int getId(){
      return this.id;
    }


    // Comportamentos
    public void emprestar(){
        if (this.disponivel == true){
            System.out.println("Empréstimo de " + this.titulo + " concluído");
            disponivel = false;
        } else {
            System.out.println(this.titulo + " indisponível");
        }
    }

    public void devolver(){
         if (this.disponivel == false){
            System.out.println("Devolução de " + this.titulo + " concluída");
            disponivel = true;
        } else {
            System.out.println(this.titulo + " ja foi devolvido e está disponível");
        }
    }

    public void exibirInformacoes() {
      System.out.println("----------------");
      System.out.println("Título: " + this.titulo);
      System.out.println("Autor: " + this.autor);
      System.out.println("Ano: " + this.ano);
      System.out.println("Disponível: " + (this.disponivel ? "Sim" : "Não"));
      System.out.println("ID: " + this.id);
      System.out.println("----------------");
    }

}
