import java.security.SecureRandom;// Import SecureRandom class

public class RandomIntegers {// Class RandomIntegers

    public static void main(String[] args) throws Exception {// main method
      
        SecureRandom randomNumbers = new SecureRandom();// Create SecureRandom object with random numbers

        // loop 20 times
        for (int counter = 1; counter <= 20; counter++) {
            // Pick random integer from 1 to 6
            int face = 1 + randomNumbers.nextInt(6);

            System.out.printf("%d ", face); // Display generated value

            // if counter is divisible by 5, start a new line of output
            if (counter % 5 == 0) {
         
                System.out.println();
         
            }// end if

        }// End of loop

    }// End of main method

}//class RandomIntegers