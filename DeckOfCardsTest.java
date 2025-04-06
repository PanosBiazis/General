public class DeckOfCardsTest {//main class
    
    public static void main(String[] args) {//main method
        
        DeckOfCards myDeckOfCards = new DeckOfCards();//create deck of cards
        
        myDeckOfCards.shuffle();//shuffle deck

        for(int i = 1; i <= 52; i++) {//deal and display cards
            
            System.out.printf("%-19s", myDeckOfCards.dealCard());// display card
            
            if (i % 4 == 0) {//new line after every 4 cards
               
                System.out.println();//new line
            
            }//end if

        }//end for

    }//end main


}//end class
