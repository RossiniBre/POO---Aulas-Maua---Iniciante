import java.util.*;

public class Quiz {
    public static void main(String[] args) {
        Scanner resposta = new Scanner(System.in);
        Random gerador = new Random();

        int pontos = 0;

        while(true){
            int num1 = gerador.nextInt(1, 50);
            int num2 = gerador.nextInt(1, 50);
            int resultadoCorreto = num1 * num2;
            

            // alternativas
            ArrayList<Integer> alternativas = new ArrayList<>();
            alternativas.add(resultadoCorreto);
            alternativas.add(resultadoCorreto + 5);
            alternativas.add(resultadoCorreto - 3);
            alternativas.add(resultadoCorreto + 10);

            // embaralhar
            Collections.shuffle(alternativas);

            System.out.printf("Qual é o produto de %d x %d?\n", num1, num2);

            char letraCorreta = 'A';

            for (int i = 0; i < alternativas.size(); i++) {
                char letra = (char) ('A' + i);
                System.out.println(letra + ") " + alternativas.get(i));

                // descobrir qual é a correta
                if (alternativas.get(i) == resultadoCorreto) {
                    letraCorreta = letra;
                }
            }

            String escolha = resposta.next();

            if (escolha.equalsIgnoreCase(String.valueOf(letraCorreta))) {
                pontos++;
                System.out.println("Correto! Pontos: " + pontos);
            } else {
                System.out.println("Errado! Resposta correta era: " + letraCorreta  + " Pontos: " + pontos);
            }      

            if(pontos == 5){
                System.out.println("Pontuação Máxima Alcançada!");
                break;
            }
        }

        resposta.close();
    }
        
}