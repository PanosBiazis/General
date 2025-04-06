public class InitArray5 {// class InitArray5
    
    public static void main(String[] args) throws Exception {// main method


        if (args.length != 3) {// if (args.length != 3)

            System.out.printf("Error: Please re-enter the entire command, including%n"+"an array size, initial value and increment.%n");//  print error message
            
            // System.exit(1);// exit program

        } else {

            int arrayLength = Integer.parseInt(args[0]);// get array size from command line
            
            int[] array  = new int[arrayLength];// array of integers


            int initialValue = Integer.parseInt(args[1]);// get the initial value from the command line
            
            int increment = Integer.parseInt(args[2]);// increment

            for (int counter = 0; counter < array.length; counter++) {// for loop

                array[counter] = initialValue + increment * counter;// array[counter] = initialValue + increment * counter;

                System.out.printf("%5d%8d%n", counter,array[counter]);// print array elements
            
            }// end for
        
        }// end if-else

    }// end main

}// end class InitArray5
