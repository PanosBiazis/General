import java.security.SecureRandom; // Import SecureRandom class from java.security package

public class RollDie2 { // begin of class RollDie2 

    public static void main(String[] args) throws Exception { // Start of main method

        SecureRandom randomNumbers = new SecureRandom(); // Create SecureRandom object

        int [] frequency = new int [7]; // Array of frequency counters

        for (int roll = 1; roll <= 6000000; roll++) { // Loop 6,000,000 times

            ++frequency[1 + randomNumbers.nextInt(6)]; // Roll die 6,000,000 times

            } // End of for loop

            System.out.printf("%s%10s\n", "Face", "Frequency"); // Print table header

            for (int face = 1; face < frequency.length; face++) { // Loop through frequency array

                System.out.printf("%4d%10d\n", face, frequency[face]); // Print frequency of each face

            }//End of for loop
        

    }// End of main method


}// end of class RollDie2