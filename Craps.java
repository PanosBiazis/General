import java.security.SecureRandom;// Import SecureRandom class

public class Craps {// Class Craps
    
private static final SecureRandom randomNumbers = new SecureRandom();// SecureRandom object with random numbers

private enum Status {CONTINUE, WON, LOST};// Enum Status

private static final int SNAKE_EYES = 2;// Constant for snake eyes

private static final int TREY = 3;// Constant for trey

private static final int SEVEN = 7;// Constant for seven

private static final int YO_LEVEN = 11;// Constant for yo eleven

private static final int BOX_CARS = 12;// Constant for box cars

    public static void main(String[] args) throws Exception {// Main method

        int myPoint = 0;// Point if no win or loss on first roll

        Status gameStatus;// Can contain CONTINUE, WON, or LOST

        int sumOfDice = rollDice();// First roll of the dice

        switch (sumOfDice) {// Determine game status and point based on first roll

            case SEVEN: // Win with 7 on first roll

            case YO_LEVEN: // Win with 11 on first roll

            gameStatus = Status.WON;// Player wins

            break;// Exit switch

            case SNAKE_EYES: // Lose with 2 on first roll

            case TREY: // Lose with 3 on first roll

            case BOX_CARS: // Lose with 12 on first roll

            gameStatus = Status.LOST;// Player loses

            break;// Exit switch

            default: // Did not win or lose, so remember point

            gameStatus = Status.CONTINUE;// Player must keep rolling

            myPoint = sumOfDice;// First roll of the dice

            System.out.printf("Point is %d\n", myPoint);// Player's point

            break;// Exit switch

            }// End switch

        while (gameStatus == Status.CONTINUE) {// Play until player wins or loses

            sumOfDice = rollDice();// Roll dice again

            // Determine game status

            if (sumOfDice == myPoint) {// Win by making point

                gameStatus = Status.WON;// Player wins
                
            }// End win by making point

            else {// Win by making point

                if (sumOfDice == SEVEN) {// Lose by rolling 7 before point

                    gameStatus = Status.LOST;// Player loses

                }// End lose by rolling 7 before point

            }// End lose by rolling 7 before point

            if(gameStatus == Status.WON){// Win by making point

                System.out.println("You win!");// Player wins

            }// End win by making point

            else{/// Lose by rolling 7 before point

                System.out.println("You lose!");// Player loses

            }// End lose by rolling 7 before point

            }// End while

            }// End main method

            private static int rollDice() {// Roll two dice and return their sum

                int die1 = 1 + randomNumbers.nextInt(6);// First die

                int die2 = 1 + randomNumbers.nextInt(6);// Second die

                int sum = die1 + die2;// Calculate sum of dice

                System.out.printf("Player rolled %d + %d = %d\n", die1, die2, sum);// Display sum of dice

                return sum;// Return sum of dice

            }// End rollDice method


}//End Class Craps
