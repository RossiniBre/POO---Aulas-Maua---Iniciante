import java.util.Scanner;

public class Calculadora{
    public static void main(String [] args){
        Scanner calculadora = new Scanner(System.in);

    double result = 0;
    String separar = "=======================";

    while (true){
        System.out.println(separar);
        System.out.println("Digite 0 para sair.");
        System.out.println(separar);
        System.out.println("Digite o primeiro valor: ");
        double n1 = calculadora.nextDouble();
        System.out.println(separar);

            if (n1 == 0){
                System.out.println("Saindo...");
                System.out.println(separar);
                break;
            }

        System.out.println("Digite o segundo valor: ");
        double n2 = calculadora.nextDouble();
        System.out.println(separar);

        System.out.println("Digite o operador (+ - * /): ");
        String operador = calculadora.next();
        System.out.println(separar);

        if (operador.equals("+")){
            result = n1 + n2;
        } else if (operador.equals("-")) {
            result = n1 - n2;
        } else if (operador.equals("*")) {
            result = n1 * n2;
        } else if (operador.equals("/")) {
            if (n2 == 0){
                System.out.println("Impossível dividir por zero.");
            } else {
                result = n1 / n2;
            }
            
        } else {
            System.out.println(separar);
            System.out.println("Operador inválido");
            System.out.println(separar);
        }
        System.out.println(separar);
        System.out.printf("Resultado: %.2f\n", result);
        }

        calculadora.close();
    }
}



