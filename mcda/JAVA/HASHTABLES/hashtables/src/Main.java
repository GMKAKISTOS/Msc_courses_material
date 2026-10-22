import java.util.Hashtable;
import java.util.Map;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Hashtable<String, Integer> hashtable = new Hashtable<>(10);

        hashtable.put("panagiwths", 100);
        hashtable.put("nikolaos", 102);
        hashtable.put("alexandros", 109);
        hashtable.put("swthrhs", 101);
        hashtable.put("ioannis", 108);
        hashtable.put("mhxalhs", 105);
        hashtable.put("fwths", 107);
        hashtable.put("basilhs", 106);
        hashtable.put("antreas", 104);
        hashtable.put("kwnstantinos", 103);

        System.out.println();
        for(String key: hashtable.keySet())
        {
       System.out.println("Key: " + key + ", Value: " + hashtable.get(key));
        }
        System.out.println();

        for(String key: hashtable.keySet())
        {
            if(key.contains("panagiwths"))
            {
                System.out.println("Key: " + key);
                System.out.println("Value: " + hashtable.get(key));
            }
        }
        System.out.println();

        for(Map.Entry<String, Integer> key: hashtable.entrySet())
        {
            System.out.println("Key: " + key.getKey() + ", Value: " + key.getValue());
        }

        System.out.println();
        for(String key3: hashtable.keySet())
        {

            System.out.println("Key: " + key3 + ", " + hashtable.get(key3) + ", " + (Math.floorMod(key3.hashCode(), 10)) + " - " + key3.hashCode());
        }

        Hashtable<Integer, String> hashtable2 = new Hashtable<>(10);

        hashtable2.put(100, "panagiwths");
        hashtable2.put(102, "nikolaos");
        hashtable2.put(109, "alexandros");
        hashtable2.put(101, "swthrhs");
        hashtable2.put(108, "ioannis");
        hashtable2.put(105, "mhxalhs");
        hashtable2.put(107, "fwths");
        hashtable2.put(106, "basilhs");
        hashtable2.put(104, "antreas");
        hashtable2.put(103, "kwnstantinos");

        System.out.println();
        for(Integer key2: hashtable2.keySet())
    {
        System.out.println("Key: " + key2 + ", " + hashtable2.get(key2) + ", " + (key2.hashCode() % 10) + " - " + key2.hashCode());
    }

        hashtable2.remove(109);

        System.out.println();
        for(Integer key2: hashtable2.keySet())
        {
            System.out.println("Key: " + key2 + ", " + hashtable2.get(key2) + ", " + (key2.hashCode() % 10) + " - " + key2.hashCode());
        }

    }}
