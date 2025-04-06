

public class GradeBook2 {// GradeBook2.java
    
    private String courseName;// name of the course

    private int[][] grades;// 2D array of grades

    public GradeBook2(String courseName, int[][] grades) {// constructor

        this.courseName = courseName;

        this.grades = grades;

    }// end of constructor

    public void setCourseName(String courseName) {// set course name

        this.courseName = courseName; // set the course name

    }// end method setCourseName


    public String getCourseName() {// get course name

        return courseName; // return the course name

    }// end method getCourseName

    public void processGrades() {// method processGrades

        outputGrades(); // call method outputGrades

        System.out.printf("%n%s %d%n%s %d%n%n", "Lowest grade is", getMinimum(), "Highest grade is", getMaximum()); // print minimum and maximum grades

        outputBarChart();

    }// end method processGrades


    public int getMinimum() {// method getMinimum

        int lowGrade = grades[0][0]; // the first grade is the lowest grade

        for (int[] studentGrades : grades) { // for each student

            for (int grade : studentGrades) { // for each grade

                if (grade < lowGrade) { // if the grade is less than the current lowest grade

                    lowGrade = grade; // assign the grade to the lowest grade

                } // end if

            } // end for

        } // end for

        return lowGrade; // return the lowest grade

    }// end method getMinimum


    public int getMaximum() { // method getMaximum

        int highGrade = grades[0][0]; // the first grade is the highest grade

        for (int[] studentGrades : grades) { // for each student

            for (int grade : studentGrades) { // for each grade

                if (grade > highGrade) { // if the grade is greater than the current highest grade

                    highGrade = grade; // assign the grade to the highest grade

                } // end if

            } // end for

        } // end for

        return highGrade; // return the highest grade


    }// end method getMaximum

    public double getAverage(int[] setOfGrades) { // method getAverage

        int total = 0; // initialize total to 0

        for (int grade : setOfGrades) { // for each grade in the array

            total += grade; // add the grade to the total

        } // end for

        return (double) total / setOfGrades.length; // return the average

    }// end method getAverage


    public void outputBarChart() { // method outputBarChart

        System.out.println("Overall grade distribution:"); // print header

        int[] frequency = new int[11]; // initialize an array to hold the frequency of each grade

        for (int[] studentGrades : grades) { // for each student

            for (int grade : studentGrades) { // for each grade

                ++frequency[grade / 10]; // increment the frequency of the grade

            } // end for

        } // end for


        for (int count = 0; count < frequency.length; count++) {// for each  frequency of grades,print a bar chart

            if (count == 10) { // print 100: if count is 10

                System.out.printf("%5d: ", 100); // print 100:

            } else { // else print range of grades

                System.out.printf("%02d-%02d: ", count * 10, count * 10 + 9); // print range of grades

            } // end if-else block

            for (int stars = 0; stars < frequency[count]; stars++) { // for loop to print stars

                System.out.print("*"); // print star

            } // end for loop to print stars

            System.out.println(); // move to next line
            
        }// end for

    }// end method outputBarChart


    public void outputGrades() { // method outputGrades

        System.out.printf("The grades are:%n%n"); // print header

        System.out.print("              ");

        for (int test = 0; test < grades[0].length; test++) { // for each test

            System.out.printf("Test %d\t", test + 1); // print test number

        } // end for

        System.out.println("Average"); // print average

        for (int student = 0; student < grades.length; student++) { // for each student

            System.out.printf("\rStudent %2d: ", student + 1); // print student number

            for (int test : grades[student]) { // for each test

                System.out.printf("%8d", test); // print test grade

            } // end for

            double average = getAverage(grades[student]); // get the average

            System.out.printf("%9.2f%n", average); // print average

        } // end for

    } // end method outputGrades


}// end class GradeBook2
