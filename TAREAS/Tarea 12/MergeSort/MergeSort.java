public class MergeSort {

    public static void mergeSort(int[] data) {
        if (data.length > 1) {
            int mitad = data.length / 2;

            // Dividir el arreglo en mitades
            int[] izquierda = new int[mitad];
            int[] derecha = new int[data.length - mitad];

            System.arraycopy(data, 0, izquierda, 0, mitad);
            System.arraycopy(data, mitad, derecha, 0, data.length - mitad);

            System.out.println(java.util.Arrays.toString(izquierda) + " --- " + java.util.Arrays.toString(derecha));

            mergeSort(izquierda);
            mergeSort(derecha);

            // Mezclar
            int i = 0, d = 0, k = 0;
            while (i < izquierda.length && d < derecha.length) {
                if (izquierda[i] < derecha[d]) {
                    data[k] = izquierda[i];
                    i++;
                } else {
                    data[k] = derecha[d];
                    d++;
                }
                k++;
            }

            // Acomodar los restantes
            while (i < izquierda.length) {
                data[k] = izquierda[i];
                i++;
                k++;
            }

            while (d < derecha.length) {
                data[k] = derecha[d];
                d++;
                k++;
            }
        }
        System.out.println("regreso de rec: " + java.util.Arrays.toString(data));
    }

    public static void main(String[] args) {
        System.out.println(".-.-.-.-.-.- MERGE --.-.-.-.-");
        int[] info = {38, 27, 43, 3, 9, 82, 10, 19, 50, 61};
        mergeSort(info);
        System.out.println(java.util.Arrays.toString(info));
        System.out.println(".-.-.-. suma recursiva --------");
    }
}
