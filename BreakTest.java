public class BreakTest {//class
    
public static void main(String[] args) {//main method

    int count;//initialization

    for (count = 1; count <= 10; count++) {//for loop

        if (count == 5) {
            break;
        }

        System.out.printf("%d ", count);//print counter

    }//end for loop

    System.out.println("\nBroke out of loop at count = " + count);//print message

}//end main method

}//class
