import java.security.SecureRandom; // Import SecureRandom class from java.security package

public class RollDie {// Class declaration
    
    public static void main(String[] args) throws Exception {// Main method

        SecureRandom randomNumbers = new SecureRandom(); // Create SecureRandom object with random numbers

        int frequency1 = 0; // Counter for 1
        
        int frequency2 = 0; // Counter for 2
        
        int frequency3 = 0; // Counter for 3
        
        int frequency4 = 0; // Counter for 4
        
        int frequency5 = 0; // Counter for 5
        
        int frequency6 = 0; // Counter for 6

        for (int roll = 1; roll <= 6000000; roll++) { // Loop 6,000,000 times

            int face = 1 + randomNumbers.nextInt(6); // Generate random number between 1 and 6

            switch (face) { // Switch statement to increment counter for each face

                case 1:// case 1
        
                ++frequency1;// Increment counter for face 1
        
                break;// Break statement to exit switch statement
        
                case 2:// case 2
        
                ++frequency2;// Increment counter for face 2
        
                break;// Break statement to exit switch statement
        
                case 3:// case 3
        
                ++frequency3;// Increment counter for face 3
        
                break;// Break statement to exit switch statement
        
                case 4:// case 4
        
                ++frequency4;// Increment counter for face 4
        
                break;// Break statement to exit switch statement
        
                case 5:/// case 5
        
                ++frequency5;// Increment counter for face 5
        
                break;// Break statement to exit switch statement
        
                case 6:// case 6
        
                ++frequency6;// Increment counter for face 6
        
                break;// Break statement to exit switch statement

            } // End of switch statement

        
        } // End of for loop

        
        System.out.println("Face\tFrequency"); // Print heading

        
        System.out.printf("1\t%d\n2\t%d\n3\t%d\n4\t%d\n5\t%d\n6\t%d\n", frequency1, frequency2, frequency3, frequency4, frequency5, frequency6);// Print heading



    }// End of main method

    
}//class RollDie
