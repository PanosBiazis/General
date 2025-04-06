public class InitArray2 {// Class declaration
    
    public static void main(String[] args) {// Main method declaration
       
        int[] array = {32,27,64,18,95,14,90,70,60,37};// array declaration

        System.out.println("Index\tValue");// print header

        for (int counter = 0; counter < array.length; counter++) {// for loop to print array

            System.out.println(counter + "\t" + array[counter]);// print array
        
        }// end of for loop


    }// end of main method

}// end of class InitArray