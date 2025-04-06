public class InitArray {// Class declaration
    
    public static void main(String[] args) {
       
        int[] array = new int[10];// array declaration

        System.out.println("Index\tValue");// print header

        for (int counter = 0; counter < array.length; counter++) {// for loop to print array

            System.out.println(counter + "\t" + array[counter]);// print array
        
        }// end of for loop


    }// end of main method

}// end of class InitArray