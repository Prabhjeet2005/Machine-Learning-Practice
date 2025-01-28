import java.util.*;
import java.lang.*;

class Hello {
  public static void main(String s[]) {
    Scanner sc = new Scanner(System.in); // Create Scanner for num
    System.out.print("Enter a number: ");
    double num = sc.nextDouble(); // Take num as a double
    double sqrt = Math.sqrt(num); // Calculate square root
    System.out.println("Square root of " + num + " is: " + sqrt); // Display result
  }
}
