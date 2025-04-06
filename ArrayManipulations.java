import  java.util.Arrays;

public class ArrayManipulations {// class definition
    
    public static void main(String[] args) throws Exception {// main method definition
        
        double [] doubleArray = {8.4,9.3,0.2,7.9,3.4};// array declaration and initialization

        Arrays.sort(doubleArray);//sort array

        System.out.printf("%ndoubleArray: ");// print array name

        for(double value:doubleArray)//for loop to print array
        {// for loop definition
        
            System.out.printf("%.1f ",value);// print array values
        
        }// end of for loop

        int [] filledIntArray = new int[10];// create an array of size 10

        Arrays.fill(filledIntArray, 7);// fill the array with 7

        displayArray(filledIntArray, "filledIntArray");// call method to display array

        int [] intArray = {1,2,3,4,5,6};// array declaration and initialization

        int[] intArrayCopy = new int[intArray.length];// create a copy of the array

        System.arraycopy(intArray, 0, intArrayCopy, 0, intArray.length);// copy the array

        displayArray(intArray, "intArray");// call method to display array

        displayArray(intArrayCopy, "intArrayCopy");// call method to display array

        boolean b = Arrays.equals(intArray, intArrayCopy);// check if two arrays are equal

        System.out.printf("%n%nintArray %s intArrayCopy%n",(b ? "==" : "!="));// print result

        b = Arrays.equals(intArray, filledIntArray);// check if two arrays are equal

        System.out.printf("intArray %s filledIntArray%n", (b ? "==" : "!="));// print result

        int location = Arrays.binarySearch(intArray, 5);// find the location of 5 in the array

        if (location >= 0)
        {
         System.out.printf("Found 5 at element %d in intArray%n", location);// print result
        }
        else{
            System.out.printf("5 not found in intArray%n");// print result
        }

        location = Arrays.binarySearch(intArray, 8763);// find the location of 8763 in the array

        if(location >= 0){// check if the value is found
            System.out.printf("Found 8763 at element %d in intArray%n", location);// print result
        } else{
            System.out.printf("8763 not found in intArray%n");// print result
        }

    }// end of main method

    public static void displayArray(int[] array, String description){// method to display array

        System.out.printf("%n%s: ",description);

        for(int value:array){// iterate over the array
            System.out.printf("%d ", value);
        }

    }// end of displayArray method

}// end of class definition
