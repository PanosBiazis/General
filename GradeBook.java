public class GradeBook {//class GradeBook
    
    private String courseName;//instance variable courseName
    private int[] grades;//instance variable grades

    public GradeBook(String courseName, int[] grades) {//constructor

        this.courseName = courseName;//assign courseName to instance variable courseName

        this.grades = grades;//assign grades to instance variable grades

    }//end constructor

    public void setCourseName(String courseName) {//method setCourseName

       this.courseName = courseName;//assign courseName to instance variable courseName
    
    }//end method setCourseName

    public String getCourseName() {//method getCourseName

        return courseName;//returning the value of the instance variable courseName
    
    }//end method getCourseName


    public void processGrades() {//method processGrades

        outputGrades();// calling method outputGrades

        System.out.printf("%nClass average: %.2f%n", getAverage());// calling method getAverage and printing the result

        System.out.printf("Lowest grade is %d%nHighest grade is %d%n", getMinimum(), getMaximum());// calling methods getMinimum and getMaximum and printing the results

        outputBarChart();// calling method outputBarChart

    }//end of method processGrades


    public int getMinimum(){//method getMinimum

        int lowGrade = grades[0];//the first grade is the lowest grade

        for (int grade : grades) {//for each grade in the array

            if (grade < lowGrade) {//if the grade is less than the current lowest grade

                lowGrade = grade;//assign the grade to the lowest grade

            }//end if

        }//end for

        return lowGrade;//returning the lowest grade

    }//end method getMinimum


    public int getMaximum(){//method getMaximum

        int highGrade = grades[0];//the first grade is the highest grade

        for (int grade : grades) {//for each grade in the array

            if (grade > highGrade) {//if the grade is greater than the current highest grade

                highGrade = grade;//assign the grade to the highest grade

            }//end if

        }//end for

        return highGrade;//returning the highest grade

    }//end method getMaximum


    public double getAverage(){//method getAverage

        int total = 0;//initialize total to 0

        for (int grade : grades) {//for each grade in the array

            total += grade;//add the grade to the total

        }//end for

        return (double) total / grades.length;//returning the average

    }//end method getAverage


    public void outputBarChart(){//method outputBarChart

        System.out.println("Grade distribution: ");//print header

        int[] frequency = new int[11];//initialize an array to hold the frequency of each grade

        for (int grade : grades) {//for each grade in the array

            ++frequency[grade / 10];//increment the frequency of the grade

        }//end for

        for (int counter = 0; counter < frequency.length; counter++) {//for loop to print the bar chart

            if (counter == 10) {//print 100: if counter is 10

                System.out.printf("%5d: ", 100);//print 100:

            } else {// else print range of grades

                System.out.printf("%02d-%02d: ", counter * 10, counter * 10 + 9);//print range of grades

            }// end if-else block

            for (int stars = 0; stars < frequency[counter]; stars++) {//for loop to print stars

                System.out.print("*");//print star

            }// end for loop to print stars

            System.out.println();//move to next line after printing stars

        }//end for loop to print bar chart

    }//end method outputBarChart


    public void outputGrades(){//method outputGrades

        System.out.printf("The grades are:%n%n");//print header

        for (int student=0;student<grades.length;student++){// for loop to print each grade

            System.out.printf("Student %2d: %3d%n",student+1,grades[student]);//print student number and grade

        }//end for

        } // end method outputGrades


}//end of class GradeBook
