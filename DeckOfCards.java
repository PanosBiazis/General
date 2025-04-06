import java.security.SecureRandom;//imports SecureRandom class

public class DeckOfCards {//begin class

    private Card[] deck;//array of Card objects

    private int currentCard;//index of next Card to be dealt (0-51)
    
    private static final int NUMBER_OF_CARDS = 52;//constant # of Cards in deck
    
    private static final SecureRandom randomNumbers = new SecureRandom();//random number generator

    public DeckOfCards(){//constructor fills deck of Cards

        String[] faces = {"Ace", "Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"};//array of Card faces
    
        String[] suits = {"Hearts", "Diamonds", "Clubs", "Spades"};//array of Card suits

        deck = new Card[NUMBER_OF_CARDS];//initialize deck array

        currentCard = 0;//initialize currentCard

        //populate deck with Card objects
        for(int count = 0; count < deck.length; count++){
    
            deck[count] = new Card(faces[count % 13], suits[count / 13]);//create Card
    
        }
    
    }//end constructor

    public void shuffle(){//shuffle deck of Cards with one-pass algorithm

        currentCard = 0;//reset currentCard

        //for each Card, pick another random Card and swap them
        for(int first = 0; first < deck.length; first++){
            //select a random number between 0 and 51
            int second = randomNumbers.nextInt(NUMBER_OF_CARDS);
            //swap current Card with randomly selected Card
            Card temp = deck[first];
    
            deck[first] = deck[second];//swap current Card with randomly selected Card
    
            deck[second] = temp;//swap
    
        }//end for
    
    }//end shuffle

            //deal one Card
            public Card dealCard(){
                //determine whether Cards remain to be dealt
                if(currentCard < deck.length){
    
                    return deck[currentCard++];
    
                }else{
    
                    return null;
    
                }//end if-else
    
            }//end method dealCard

}//end class