import java.awt.geom.Point2D;
import java.util.ArrayList;
import java.util.List;

public class RayCastingAlgorithm {

    public static class Point {
        double x;
        double y;

        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    public static class Polygon {
        List<Point> vertices;

        public Polygon() {
            vertices = new ArrayList<>();
        }

        public void addVertex(Point point) {
            vertices.add(point);
        }
    }

    public static boolean isPointInsidePolygon(Point point, Polygon polygon) {
        int intersections = 0;
        int numVertices = polygon.vertices.size();

        for (int i = 0; i < numVertices; i++) {
            Point p1 = polygon.vertices.get(i);
            Point p2 = polygon.vertices.get((i + 1) % numVertices);

            if (point.y > Math.min(p1.y, p2.y) && point.y <= Math.max(p1.y, p2.y)
                    && point.x <= Math.max(p1.x, p2.x) && p1.y != p2.y) {
                double xIntersection = (point.y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y) + p1.x;
                if (p1.x == p2.x || point.x <= xIntersection)
                    intersections++;
            }
        }

        return intersections % 2 != 0;
    }

    public static void main(String[] args) {
        // Create a sample polygon (square)
        Polygon polygon = new Polygon();
        polygon.addVertex(new Point(1, 1));
        polygon.addVertex(new Point(1, 4));
        polygon.addVertex(new Point(4, 4));
        polygon.addVertex(new Point(4, 1));

        // Test points
        Point point1 = new Point(2, 2);
        Point point2 = new Point(3, 3);
        Point point3 = new Point(5, 2);

        System.out.println("Is point1 inside the polygon? " + isPointInsidePolygon(point1, polygon)); // true
        System.out.println("Is point2 inside the polygon? " + isPointInsidePolygon(point2, polygon)); // true
        System.out.println("Is point3 inside the polygon? " + isPointInsidePolygon(point3, polygon)); // false
    }
}

