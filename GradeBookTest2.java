public class GradeBookTest2 {// GradeBookTest2.java
    
public static void main(String[] args) throws  Exception {// main method
    
    int[][] gradesArray = { {87,96,70}, 
                            {68,87,90}, 
                            {94,100,90}, 
                            {100,81,82}, 
                            {83,65,85}, 
                            {78,77,39}, 
                            {79,92,18}, 
                            {67,70,93}, 
                            {88,99,50}, 
                            {75,86,96} };

    GradeBook2 myGradeBook = new GradeBook2("CS101 Introduction to Java Programming",gradesArray);// create a GradeBook object
    
    System.out.printf("Welcome to the grade book for%n%s%n",myGradeBook.getCourseName()); // print course name

    myGradeBook.processGrades(); // process grades


}// End of main


}// end class GradeBookTest2
