import java.util.Scanner;//import Scanner class

public class Analysis {//start of class
    
    public static void main(String[] args) throws Exception {//start of main
        
        Scanner input = new Scanner(System.in);//create Scanner object to obtain input from command window

        int passes = 0;//number of passes
        int failures = 0;//number of failures
        int studentCounter = 1;//student counter

        while (studentCounter <= 10) {//loop 10 times

            System.out.print("Enter result (1 = pass, 2 = fail): ");//prompt

            int result = input.nextInt();//read result from user

            if (result == 1) {
                passes = passes + 1;//increment passes by 1
            }
            else {
                failures = failures + 1;//increment failures by 1
            }

            studentCounter = studentCounter + 1;//increment student counter by 1

        }//end while loop

        System.out.println("Passed: " + passes);//display number of passes
        System.out.println("Failed: " + failures);//display number of failures

        if (passes > 8)
            System.out.println("Bonus to instructor!");//display bonus message

        input.close();//close Scanner object

}//end of main


}//end of class