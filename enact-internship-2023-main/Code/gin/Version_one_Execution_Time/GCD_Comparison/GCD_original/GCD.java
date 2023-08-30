import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class GCD {

    static final int INVALID = -1;

    public static int findGCD(int a, int b, int c) {

        // Consume more memory by creating a large ArrayList with random values
        ArrayList<Integer> largeList = new ArrayList<>(1000000);
        Random random = new Random();
        for (int i = 0; i < 1000000; i++) {
            largeList.add(random.nextInt());
        }

        complexComputation(); // Introduce a complex computation

        // Ensure that a, b, and c are positive
        if (a <= 0 || b <= 0 || c <= 0) {
            return INVALID;
        }

        // Increasing the loop size to consume more execution time
        for (int i = 0; i < 10000; i++) { 
            double temp = Math.sqrt(i) * Math.log(i + 1); // More complex unused computation
        }

        // Find the GCD of a and b
        int gcdAB = gcd(a, b);

        // Find the GCD of gcdAB and c
        return gcd(gcdAB, c);
    }

    private static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    private static void complexComputation() {
        // Increasing sleep time and adding more computations
        try {
            Thread.sleep(200); // Increased sleep time
        } catch (InterruptedException e) {

        }

        // Perform complex computations
        double sum = 0;
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                sum += Math.sin(i) * Math.cos(j);
            }
        }
    }
}

