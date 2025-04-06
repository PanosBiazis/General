public class GradeBookTest {// GradeBookTest.java

      public static void main(String[] args) throws Exception {// main method
          
        int[] gradesArray = {87,68,94,100,83,78,85,91,76,87};// array of grades

        GradeBook myGradeBook = new GradeBook("CS101 Introduction to Java Programming",gradesArray);// create a GradeBook object

        System.out.printf("Welcome to the grade book for%n%s%n",myGradeBook.getCourseName());// print course name

        myGradeBook.processGrades();// process grades


      }  // end main method


}// end class GradeBookTest
