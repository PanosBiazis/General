public class MethodOverload {// Start of class MethodOverload
    
    public static void main(String[] args) throws Exception { // Start of main method
        
        System.out.println("Square of integer 7 is " + square(7)); // Call square method with integer 7
        
        System.out.println("Square of double 7.5 is " + square(7.5)); // Call square method with double 7.5

    }// End of main method

    public static int square(int intValue) { // Start of square method with integer parameter

        System.out.println("Called square with int argument: " + intValue);// Print message
        
        return intValue * intValue;// Return square of integer value

    } // End of square method

    public static double square(double doubleValue) { // Start of square method with double parameter

        System.out.println("Called square with double argument: " + doubleValue);// Print message 
        
        return doubleValue * doubleValue;// Return square of double value
        
    } // End of square method


}// End of class MethodOverload
