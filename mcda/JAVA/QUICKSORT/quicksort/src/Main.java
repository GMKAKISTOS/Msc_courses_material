//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Integer[] array = {8, 2, 5, 3, 9, 4, 7, 6, 1};

        for (Integer i = 0; i <= array.length; i++) {
            if (i == 0) {
                System.out.println();
                System.out.print(array[i] + " ");
            } else if (i < array.length) {
                System.out.print(array[i] + " ");
            } else {
                System.out.println();
            }
        }

        quickSort(array, 0, array.length - 1);

        for (Integer i = 0; i <= array.length; i++) {
            if (i == 0) {
                System.out.println();
                System.out.print(array[i] + " ");
            } else if (i < array.length) {
                System.out.print(array[i] + " ");
            } else {
                System.out.println();
            }
        }

    }

    private static void quickSort(Integer[] array, Integer start, Integer end)
    {
        if ( end <= start)
        {
            return;
        }
        else
        {
            Integer pivot = partition(array, start, end);
            quickSort(array, start , pivot - 1);
            quickSort(array, pivot + 1, end);
        }
    }

    private static Integer partition(Integer[] array, Integer start, Integer end)
    {
        Integer pivot = array[end];
        Integer i = start - 1;

        for(Integer j = start; j <= end - 1; j++)
        {
            if(array[j] < pivot)
            {
                i++;
                Integer temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        i++;
        Integer temp = array[i];
        array[i] = array[end];
        array[end] = temp;

        return i;
    }

}