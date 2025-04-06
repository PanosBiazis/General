import java.util.Scanner;//import scanner

public class LetterGrades {//declare class

    public static void main(String[] args) {//declare main method
    
        int total = 0;//declare variables
        
        int gradeCounter = 0;//declare variables
        
        int aCount = 0;//declare variables
        
        int bCount = 0;//declare variables
        
        int cCount = 0;//declare variables   
        
        int dCount = 0;//declare variables
        
        int fCount = 0;//declare variables

        Scanner input = new Scanner(System.in);//create scanner

        System.out.printf("%s%n%s%n %s%n %s%n", "Enter the integer grades in the range 0-100", "Type the end-of-file indicator to terminate input:", "On UNIX/Linux/Mac OS X type <ctrl> d then press Enter", "On Windows type <ctrl> z then press Enter");//prompt

        System.out.print("Enter grade: ");//print

        while (input.hasNext()) {//while loop begins here

            System.out.print("Enter grade: ");

            int grade = input.nextInt();//read grade

            total += grade;//add grade to total
            
            ++gradeCounter;//increment gradeCounter

            switch (grade / 10) {//switch statement begins here

                case 9://case 9:

                case 10://case 10:
             
                    ++aCount;//increment aCount
             
                   break;//break statement terminates switch
             
                case 8://case 8
                    
                    ++bCount;//increment bCount
                
                    break;//break statement terminates switch
                
                case 7:///case 7
                
                    ++cCount;//increment cCount
                
                    break;//break statement terminates switch
                
                case 6://case 6
                
                    ++dCount;//increment dCount
                
                    break;//break statement terminates switch
                
                default://default case
                
                    ++fCount;//increment fCount
                
                    break;//break statement terminates switch
            
                }//end switch
        
        }//end while

        System.out.printf("%nGrade Report:%n");//print grade report

        if (gradeCounter != 0) {//if user entered at least one grade...
        
            double average = (double) total / gradeCounter;//integer division produces integer result

            System.out.printf("Total of all %d grades is %d%n", gradeCounter, total);//total of all grades
        
            System.out.printf("Class average is %.2f%n", average);//class average
        
            System.out.printf("Number of A's: %d%n", aCount);//number of A's
        
            System.out.printf("Number of B's: %d%n", bCount);//number of B's
        
            System.out.printf("Number of C's: %d%n", cCount);//number of C's
        
            System.out.printf("Number of D's: %d%n", dCount);//number of D's
        
            System.out.printf("Number of F's: %d%n", fCount);//number of F's
        
        }//end if
        
        else {//else
           
            System.out.println("No grades were entered");//no grades were entered
        
        }//end else
        
        input.close();//close scanner
    
    }//end main

}//end class
