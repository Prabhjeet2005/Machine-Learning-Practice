// Abstract class
abstract class Shape {
  abstract void numberOfSides();
}

class Trapezoid extends Shape {
  void numberOfSides() {
    System.out.println("Trapezoid has 4 sides.");
  }
}

class Triangle extends Shape {
  void numberOfSides() {
    System.out.println("Triangle has 3 sides.");
  }
}

class Rectangle extends Shape {
  void numberOfSides() {
    System.out.println("Rectangle has 4 sides.");
  }
}

class Hexagon extends Shape {
  void numberOfSides() {
    System.out.println("Hexagon has 6 sides.");
  }
}

public class AbstractShape {
  public static void main(String[] args) {

    Trapezoid trapezoid = new Trapezoid();
    trapezoid.numberOfSides();

    Triangle triangle = new Triangle();
    triangle.numberOfSides();

    Rectangle rectangle = new Rectangle();
    rectangle.numberOfSides();

    Hexagon hexagon = new Hexagon();
    hexagon.numberOfSides();
  }
}
