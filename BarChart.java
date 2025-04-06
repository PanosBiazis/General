public class BarChart {// class definition BarChart
    
    public static void main(String[] args) throws Exception {//main method definition
        
        int[] array = {0,0,0,0,0,0,1,2,4,2,1};//array of grades

        System.out.println("Grade distribution:");//print header

        for(int counter = 0; counter < array.length; counter++) {//for loop to print the bar chart

            if(counter == 10) {//print 100: if counter is 10
            
                System.out.printf("%5d: ", 100);//print 100:
            
            } else {// else print range of grades
            
                System.out.printf("%02d-%02d: ", counter * 10, counter * 10 + 9);//print range of grades
            
            }// end if-else block
            
            // Print stars on the same line
            for(int stars = 0; stars < array[counter]; stars++) {//for loop to print stars

                System.out.print("*");//print star
            
            }// end for loop to print stars
            
            
            System.out.println(); //move to next line after printing stars
        
        }//end for loop to print bar chart

        
    }//end main method


}//end class BarChart
