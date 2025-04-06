
public class PassArray {//class PassArray

    public static void main(String[] args) throws Exception {//starts the main method
        
        int[] array = {1,2,3,4,5};//array of integers

        System.out.printf("Effects of passing reference to entire array:%n"+"The values of the original array are:%n");

        for(int value:array)//for loop to print array
            System.out.printf("   %d",value);//print array

        modifyArray(array);//pass a report to the array

        System.out.printf("%n%nThe values of the modified array are:%n");// print modified array

        for(int value:array)//for loop to print array
            System.out.printf("   %d",value);//print array

        
        System.out.printf("%n%nEffects of passing array element value:%n"+"array[3] before modifyElement: %d%n",array[3]);//print before modifyElement
        
        modifyElement(array[3]);//pass a report to the element

        System.out.printf("array[3] after modifyElement: %d%n",array[3]);//print after modifyElement

    }//end main method


    public static void modifyArray(int array2[]){// method to modify array

        for(int counter = 0;counter < array2.length;counter++){// for loop to modify array

            array2[counter] *= 2;// calculation to modify array
        
        }//end of loop

    }//end of method


    public static void modifyElement(int element){// method to modify element

        element *= 2;// calculation to modify element
    
        System.out.printf("Value of element in modifyElement: %d%n",element);//print element
    
    }//end of method


}//end of class PassArray