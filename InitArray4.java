public class InitArray4 {// public class of type InitArray4
    
    public static void main(String[] args) throws Exception {// public static void main of type String[] of type args throws Exception

        int[][] array1 = {{1,2,3},{4,5,6}};
        int[][] array2 = {{1,2},{3},{4,5,6}};

        System.out.println("Values in array1 are");// System.out.printf of type String of type "Values in array1 are"

        outputArray(array1);// call method outputArray of type array1

        System.out.printf("%nValues in array2 are%n");// System.out.printf of type String of type "Values in array2 are"

        outputArray(array2);// call method outputArray of type array2
        


    }// end main

    public static void outputArray(int[][] array) throws Exception {// public static void outputArray of type int[][] of type array throws Exception

        for (int row = 0; row < array.length; row++) {// for each row in array

            for (int column = 0; column < array[row].length; column++) {// for each column in row

                System.out.printf("%d ", array[row][column]);// print array[row][column]

            }

            System.out.println();
        }

    }// end outputArray

}// end class InitArray4
