import static org.junit.Assert.*;

public class RectangleTest {

    private void checkClassification(int[][] rectangles, int expectedResult) {
        for (int[] rectangle: rectangles) {
            int rectangleType = Rectangle.classifyRectangle(rectangle[0], rectangle[1], rectangle[2], rectangle[3]);
            assertEquals(expectedResult, rectangleType);
        }
    }

    @org.junit.Test
    public void testInvalidRectangles() throws Exception {
        int[][] invalidRectangles = {{0, 1, 1, 1}, {1, 1, 1, 0}, {2, 3, 4, 5}, {-1, 1, 1, 1}, {1, -1, 1, 1}, {1, 1, -1, 1}, {1, 1, 1, -1}};
        checkClassification(invalidRectangles, Rectangle.INVALID);
    }

    @org.junit.Test
    public void testSquares() throws Exception {
        int[][] squares = {{1, 1, 1, 1}, {100, 100, 100, 100}, {99, 99, 99, 99}};
        checkClassification(squares, Rectangle.SQUARE);
    }

    @org.junit.Test
    public void testRectangles() throws Exception {
        int[][] rectangles = {{2, 3, 2, 3}, {1000, 900, 1000, 900}, {30, 16, 30, 16}};
        checkClassification(rectangles, Rectangle.RECTANGLE);
    }
}

