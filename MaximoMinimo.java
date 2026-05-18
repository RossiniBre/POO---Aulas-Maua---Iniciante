import java.util.Arrays;

public class MaximoMinimo {
    public static void minMax(int[] arr) {
        Arrays.sort(arr);
        int min = arr[0];
        int max = arr[arr.length - 1];
        System.out.println("Max: " + max);
        System.out.println("Min: " + min);
    }

    public static void main(String[] args) {
        minMax(new int[]{3, 7, 1, 9, 4, 2});
    }
}