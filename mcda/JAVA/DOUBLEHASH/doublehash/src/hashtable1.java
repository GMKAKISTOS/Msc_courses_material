public class hashtable1 {

    String[] hasharray;
    Integer arraysize;
    Integer size = 0;

    public hashtable1(int numberofslots)
    {
       if(isprime(numberofslots))
       {
           hasharray = new String[numberofslots];
           arraysize = numberofslots;
       }
       else
       {
           int primecount = getnextprime(numberofslots);
           hasharray = new String[primecount];
           arraysize = primecount;

           System.out.println("hash table size given " + numberofslots + " is not a prime!");
           System.out.println("hash table size changed to: " + primecount + "!");
           System.out.println();
       }
    }

    private boolean isprime(Integer num) {
        for (Integer i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    private int getnextprime(int minimumnumber) {
       for(Integer i = minimumnumber; true; i++)
       {
           if(isprime(i))
           {
               return i;
           }
       }
    }

    private int hashfunction1(String word)
    {
        int hasvalue = word.hashCode();
        hasvalue = hasvalue % arraysize;
        if(hasvalue < 0)
        {
            hasvalue += arraysize;
        }
        return hasvalue;
    }

    private int hashfunction2(String word) {
        int hasvalue = word.hashCode();
        hasvalue = hasvalue % arraysize;
        if (hasvalue < 0) {
            hasvalue += arraysize;
        }
        return 3 - hasvalue % 3;
    }

    public void insert(String word)
    {
        int hashvalue = hashfunction1(word);
        int stepsize = hashfunction2(word);

        while(hasharray[hashvalue] != null)
        {
            hashvalue = hashvalue + stepsize;
            hashvalue = hashvalue % arraysize;
        }
        hasharray[hashvalue] = word;
        System.out.println("inserted word: " + word + "!");
        size++;
    }

    public String find(String word)
    {
        int hashvalue = hashfunction1(word);
        int stepsize = hashfunction2(word);

        while(hasharray[hashvalue] != null)
        {
            if (hasharray[hashvalue].equalsIgnoreCase(word))
            {
                return hasharray[hashvalue];
            }
            hashvalue = hashvalue + stepsize;
            hashvalue = hashvalue % arraysize;
        }
       return hasharray[hashvalue];
    }

    public void displaytable()
    {
        System.out.println("Table: ");
        System.out.println();
        for(Integer i = 0; i < arraysize; i++)
        {
            if(hasharray[i] != null)
            {
                System.out.print(hasharray[i] + " ");
                //System.out.println(hasharray[i] + " ");
            }
            else{
                System.out.print("** ");
                //System.out.println("** ");
            }
            System.out.println("");
        }
    }
}
