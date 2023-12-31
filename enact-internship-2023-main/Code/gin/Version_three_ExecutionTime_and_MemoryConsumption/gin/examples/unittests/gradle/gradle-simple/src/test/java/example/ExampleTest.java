package example;/*
 * This Java source file was generated by the Gradle 'init' task.
 */
import org.junit.Test;
import static org.junit.Assert.*;

public class ExampleTest {

    @Test
    public void profileEnumTest() {

        long start = System.currentTimeMillis();

        while (true) {

            ExampleEnum[] vals = ExampleEnum.values();

            long now = System.currentTimeMillis();
            if (now - start > 2000) {
                break;
            }

        }

        assertTrue(true);

    }

    //calculate primes to give JFR something to sample
    @Test
    public void jfrPrimeTest() {
        int[] primes = new int[30000];

        int index = 1;
        primes[0] = 2;
        int current = 3;

        while (index<30000) {
            boolean check = true;
            for (int i = 0;i<index;i++) {
                if (current%primes[i]==0) {
                    check = false;
                    break;
                }
            }
            if (check) {
                primes[index] = current;
                index++;
            }
            current++;
        }

        assertTrue(true);
    }

}
