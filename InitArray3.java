public class InitArray3 {// Class declaration
    
    public static void main(String[] args) {// Main method declaration
       
        final int array_length = 10;// array declaration
        int[] array = new int[array_length];// array initialization

        System.out.println("Index\tValue");// print header

        for (int counter = 0; counter < array.length; counter++) {// for loop to print array

            array[counter] = 2 + 2 *counter;// assign value to array element 

            System.out.println(counter + "\t" + array[counter]);// print array
        
        }// end of for loop


    }// end of main method

}// end of class InitArray