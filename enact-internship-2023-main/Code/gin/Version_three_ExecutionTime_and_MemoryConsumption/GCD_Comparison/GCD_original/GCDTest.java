import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class GCDTest {

    @Test
    public void testFindGCD() {
        int a = 54;
        int b = 24;
        int c = 18;
        int expected = 6;
        int result = GCD.findGCD(a, b, c);
        assertEquals("GCD of " + a + ", " + b + ", and " + c + " should be " + expected, expected, result);
    }

    @Test
    public void testInvalidInput() {
        int a = -5;
        int b = 24;
        int c = 18;
        int expected = GCD.INVALID;
        int result = GCD.findGCD(a, b, c);
        assertEquals("GCD with negative numbers should be invalid", expected, result);
    }

    @Test
    public void testWithZeroes() {
        assertEquals(GCD.INVALID, GCD.findGCD(0, 24, 18));
        assertEquals(GCD.INVALID, GCD.findGCD(54, 0, 18));
        assertEquals(GCD.INVALID, GCD.findGCD(54, 24, 0));
    }

    @Test
    public void testWithPrimes() {
        assertEquals(1, GCD.findGCD(17, 19, 23));
    }

    @Test
    public void testWithSameNumbers() {
        assertEquals(42, GCD.findGCD(42, 42, 42));
    }

    @Test
    public void testWithDifferentCombinations() {
        assertEquals(4, GCD.findGCD(16, 36, 24));
        assertEquals(3, GCD.findGCD(9, 15, 27));
        assertEquals(2, GCD.findGCD(10, 22, 14));
    }
}

