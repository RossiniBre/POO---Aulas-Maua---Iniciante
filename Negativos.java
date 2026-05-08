public class Negativos {

    public static int contarNegativos(int[] arr){
        int n = 0;

        for(int i = 0; i < arr.length; i++){
            if (arr[i] < 0){
                n++;
            }
        }
        return n;
    }

    public static void main(String [] args){
        int quantos = contarNegativos(new int[]{-1, 2, -3, 4, -5, 6});
        System.out.printf("Existem %d números negativos", quantos);
    }
}