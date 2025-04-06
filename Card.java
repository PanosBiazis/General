public class Card {//class card
    
    private final String face;//instance variable face

    private final String suit;//instance variable suit

    public Card(String face, String suit) {//constructor

        this.face = face;//assigning the value of the instance variable

        this.suit = suit;//assigning the value of the instance variable

        }//end constructor

    public String toString() {//method toString

        return face + " of " + suit;//returning the value of the instance variable

    }//end method toString

}//end class card