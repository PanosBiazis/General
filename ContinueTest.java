public class ContinueTest {//class

    public static void main(String[] args) {//main method

        for (int count = 1; count <= 10; count++) {//for loop

            if (count == 5) {//if statement

                continue;//continue statement

            }

            System.out.printf("%d\t", count);//print counter

            
        }//end for loop

        System.out.printf("%nUsed continue to skip printing 5%n");//print message


}//end main method

}//end class