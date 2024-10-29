public class MergeSort {

    public static void mergeSort(int[] data) {
        if (data.length > 1) {
            int mid = data.length / 2;

            // Dividir el arreglo en dos mitades
            int[] left = new int[mid];
            int[] right = new int[data.length - mid];

            System.arraycopy(data, 0, left, 0, mid);
            System.arraycopy(data, mid, right, 0, data.length - mid);

            System.out.println("División: Izquierda " + java.util.Arrays.toString(left) + " | Derecha " + java.util.Arrays.toString(right));

            mergeSort(left);
            mergeSort(right);

            // Mezcla de las mitades
            int i = 0, j = 0, k = 0;
            while (i < left.length && j < right.length) {
                if (left[i] <= right[j]) {
                    data[k] = left[i];
                    i++;
                } else {
                    data[k] = right[j];
                    j++;
                }
                k++;
            }

            // Acomodar los elementos restantes
            while (i < left.length) {
                data[k] = left[i];
                i++;
                k++;
            }

            while (j < right.length) {
                data[k] = right[j];
                j++;
                k++;
            }
        }
        System.out.println("Resultado parcial: " + java.util.Arrays.toString(data));
    }

    public static void main(String[] args) {
        System.out.println("=== Iniciando Merge Sort ===");
        int[] info = {38, 27, 43, 3, 9, 82, 10, 19, 50, 61};
        mergeSort(info);
        System.out.println("Arreglo ordenado: " + java.util.Arrays.toString(info));
        System.out.println("=== Fin de Merge Sort ===");
    }
}
