public class Pares {

    public static int sumEven(int[] arr){
        int soma = 0;

        for(int i = 0; i < arr.length; i++){
            if (arr[i] % 2 == 0){
                soma += arr[i];
            }
        }
        return soma;
    }

    public static void main(String[] args) {
        int resultado = sumEven(new int[]{56, 44, 67, 68, 22, 11});
        System.out.printf("A soma dos números pares é: " + resultado);
    }
}