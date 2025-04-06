public class SumArray {// class definition SumArray
    
    public static void main(String[] args) throws Exception {// main method
    
        int[] array = {87,68,94,100,83,78,85,91,76,87}; // array definition
        int total = 0;// variable declaration

        for (int counter=0;counter<array.length;counter++){
            total += array[counter];
        }

        System.out.println("Total of array elements: " + total);


    }// end main method

}// end class SumArray
