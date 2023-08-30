import java.util.Arrays;

public class Rectangle {
    
    static final int INVALID = 0;
    static final int RECTANGLE = 1;
    static final int SQUARE = 2;

    public static int classifyRectangle(int a, int b, int c, int d) {
        // Consume more memory by creating a large array
        int[] largeArray = new int[1000000];
        Arrays.fill(largeArray, 0);
        
        // Adding a delay
        try {
            // Pausing for 2 seconds (2000 milliseconds)
            Thread.sleep(200);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // A rectangle or square will be invalid if any side length is less than or equal to 0
        if(a <= 0 || b <= 0 || c <= 0 || d <= 0){
            return INVALID;
        }

        // If all sides are equal
        else if(a == b && b == c && c == d){
            return SQUARE;
        }

        // If opposite sides are equal
        else if(a == c && b == d){
            return RECTANGLE;
        }

        // If the given sides can't form a rectangle or square
        else{
            return INVALID;
        }

    }
}

