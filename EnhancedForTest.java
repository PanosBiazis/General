public class EnhancedForTest {//start of class

    public static void main(String[] args) {//start of main method

        int[] array = {87, 68, 94, 100, 83, 78, 85, 91, 76, 87};//array of integers
        
        int total = 0;//initialize total

        for (int number : array) {//for each integer in array, add it to total

            total += number;//add number to total
        
        }//end of for loop

        System.out.printf("Total of array elements: %d%n", total);//display total of array elements

    }//end of main method
    
}//end of class
