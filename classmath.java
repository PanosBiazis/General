public class classmath {// Define a class named classmath

    public static void main(String[] args) throws Exception { // Define a main method

        double x = 3.0;
        double y = 4.0;

        // Call methods of Math class
        System.out.printf("The value of pi is: %.2f%n", Math.PI);


        long randomNumber = (long) (Math.random() * 100);
        System.out.printf("A random number between 0 and 100 is: %d%n", randomNumber);

        System.out.printf("The square root of %.2f is: %.2f%n", x, Math.sqrt(x));

        System.out.printf("The value of e is: %.2f%n", Math.E);

        System.out.printf("The absolute value of %.2f is: %.2f%n", x, Math.abs(x));

        System.out.printf("The value of 3 to the power of 4 is: %.2f%n", Math.pow(3, 4));

        System.out.printf("The value of 3 to the power of 4 is: %.2f%n", Math.pow(3, 4));

        System.out.printf("The value of the sine of %.2f is: %.2f%n", x, Math.sin(x));

        System.out.printf("The value of the cosine of %.2f is: %.2f%n", x, Math.cos(x));

        System.out.printf("The value of the tangent of %.2f is: %.2f%n", x, Math.tan(x));

        System.out.printf("The value of the angle in radians of %.2f is: %.2f%n", x, Math.toRadians(x));

        System.out.printf("The value of the angle in degrees of %.2f is: %.2f%n", x, Math.toDegrees(x));

        System.out.printf("The value of the maximum of %.2f and %.2f is: %.2f%n", x, y, Math.max(x, y));

        System.out.printf("The value of the minimum of %.2f and %.2f is: %.2f%n", x, y, Math.min(x, y));

        System.out.printf("The value of the Ceil of %.2f is: %.2f%n", x, Math.ceil(x));

        System.out.printf("The value of the Floor of %.2f is: %.2f%n", x, Math.floor(x));

        System.out.printf("The value of the Rint of %.2f is: %.2f%n", x, Math.rint(x));

        System.out.printf("The value of the Round of %.2f is: %.2f%n", x, (double)Math.round(x));



    }//end of main method

}//end of classmath
