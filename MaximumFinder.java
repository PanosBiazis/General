import java.util.Scanner;// Import the Scanner class

public class MaximumFinder {// Define a class named MaximumFinder
    
    public static void main(String[] args) throws Exception {// Define a main method
        
        Scanner input = new Scanner(System.in);// Create a Scanner object to obtain input from command window

        System.out.println("Enter three floating-point values separated by spaces: ");// Prompt

        double number1 = input.nextDouble();// Read first double from user
        double number2 = input.nextDouble();// Read second double from user
        double number3 = input.nextDouble();// Read third double from user

        double result = maximum(number1, number2, number3);// Call maximum method

        System.out.printf("%nMaximum is %.2f%n", result);// Display maximum value

        input.close();// Close the Scanner object to release resources

    }//end main method

    public static double maximum(double x, double y, double z) {// Define a method named maximum

        double maximumValue = x;// Assume x is the largest value
        
        if (y > maximumValue) {// If y is greater than maximumValue
            maximumValue = y;// Set maximumValue to y
        }
        if (z > maximumValue) {// If z is greater than maximumValue
            maximumValue = z;// Set maximumValue to z
        }

        return maximumValue;// Return maximumValue

    }//end method maximum

}//end class MaximumFinder
