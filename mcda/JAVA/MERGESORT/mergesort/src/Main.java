
public class Main {
    public static void main(String[] args) {

        Integer[] array = {8, 2, 6, 7, 3, 0, 1, 5, 9, 4};

        for(Integer i = 0; i <= array.length - 1; i++)
        {
            if(i == 0)
            {
                System.out.println();
                System.out.print(array[i] + " ");
            }
            else if(i == array.length - 1)
            {
                System.out.print(array[i] + " ");
                System.out.println();
            }
            else
            {
                System.out.print(array[i] + " ");
            }
        }

        mergesort(array);

        for(Integer i = 0; i <= array.length - 1; i++)
        {
            if(i == 0)
            {
                System.out.println();
                System.out.print(array[i] + " ");
            }
            else if(i == array.length - 1)
            {
                System.out.print(array[i] + " ");
                System.out.println();
            }
            else
            {
                System.out.print(array[i] + " ");
            }
        }
    }

    private static void mergesort(Integer[] array)
    {
      Integer length = array.length;
      if(length <= 1)
      {
          return;
      }
      else
      {
          Integer middle = length / 2;
          Integer[] leftarray = new Integer[middle];
          Integer[] rightarray = new Integer[length - middle];
          Integer i = 0;
          Integer j = 0;

          for(i = 0; i < length; i++)
          {
              if(i < middle)
              {
                  leftarray[i] = array[i];
              }
              else
              {
                  rightarray[j] = array[i];
                  j++;
              }
          }
          mergesort(leftarray);
          mergesort(rightarray);
          mergee(leftarray, rightarray, array);
      }

    }

    private static void mergee(Integer[] leftarray, Integer[] rightarray, Integer[] array)
    {
      Integer i = 0;
      Integer l = 0;
      Integer r = 0;
      Integer leftsize = array.length / 2;
      Integer rightsize = array.length - leftsize;

      while(l < leftsize && r < rightsize)
      {
          if(leftarray[l] < rightarray[r])
          {
              array[i] = leftarray[l];
              i++;
              l++;
          }
          else
          {
              array[i] = rightarray[r];
              i++;
              r++;
          }
      }
      while(l < leftsize)
      {
          array[i] = leftarray[l];
          i++;
          l++;
      }
      while(r < rightsize)
      {
          array[i] = rightarray[r];
          i++;
          r++;
      }

    }
}