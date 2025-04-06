import java.util.Scanner;

public class ClassAverage {//begin class

    public static void main(String[] args) throws Exception {//begin main
        
    java.util.Scanner input = new Scanner(System.in);//create scanner to obtain input from command window
    
    int total = 0;//initialize sum of grades entered by the user
    
    int gradeCounter = 1;//initialize # of grade to be entered next

    while (gradeCounter <= 10) {//loop 10 times
        
        System.out.print("Enter grade: ");//prompt
        
        int grade = input.nextInt();//read grade from user
        
        total = total + grade;//add grade to total
        
        gradeCounter = gradeCounter + 1;//increment counter by 1
    
    }//end while

    int average = total / 10;//integer division yields integer result

    System.out.printf("%nTotal of all 10 grades is %d%n", total);//display total of grades entered

    System.out.printf("Class average is %d%n", average);//display class average

    input.close();//close scanner

    }//end main   

}//end class
