import java.util.Scanner;

public class ClassAverage1 {//begin class

    public static void main(String[] args) throws Exception {//begin main
        
    java.util.Scanner input = new Scanner(System.in);//create scanner to obtain input from command window
    
    int total = 0;//initialize sum of grades entered by the user
    
    int gradeCounter = 0;//initialize # of grade to be entered next

    System.out.print("Enter grade or -1 to quit: ");//prompt
        
    int grade = input.nextInt();//read grade from user
    
    if (grade == -1) {
        System.out.println("Exiting");//prompt
        System.exit(0);//exit program
        input.close();//close scanner
        return;//close scanner
        }//end if

    while (gradeCounter != -1) {//

        total = total + grade;//add grade to total
        
        gradeCounter = gradeCounter + 1;//increment counter by 1
        
        System.out.print("Enter grade or -1 to quit: ");//prompt
        
        grade = input.nextInt();//read grade from user

        if (grade == -1) {
            break;
            }//end if
        
        
    
    }//end while

    if (gradeCounter != 0) {//if user entered at least one grade...

        double average = (double) total / gradeCounter;//calculate average of all grades entered

        System.out.printf("%nTotal of all %d grades is %d%n", gradeCounter, total);//display total of grades entered

        System.out.printf("Class average is %.2f%n", average);//display class average

    }//end if
    else {//if no grades were entered, output message

        System.out.println("No grades were entered");

    }//end else

    // int average = total / 10;//integer division yields integer result

    // System.out.printf("%nTotal of all 10 grades is %d%n", total);//display total of grades entered

    // System.out.printf("Class average is %d%n", average);//display class average

    input.close();//close scanner

    }//end main   

}//end class