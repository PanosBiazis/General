public class Time1Test{// Start of class

    public static void main(String[] args) {// Start of main method
        
        Time1 time = new Time1();// Create a new Time1 object called time

        displayTime("After time object is created",time);// Call the displayTime method and pass time as an argument

        System.out.println("");// Empty line for better readability

        time.setTime(13, 27, 6);// Set the time to 13:27:06

        displayTime("After calling setTime",time);// Call the displayTime method and pass time as an argument

        System.out.println("");// Empty line for better readability

        try {// Start of try block
            
            time.setTime(99, 99, 99);// Attempt to set the time to 99:99:99

        } catch (IllegalArgumentException e) {// Start of catch block

            System.out.printf("Exception: %s%n%n",e.getMessage());// Print the exception message

        }// End of catch block

        displayTime("After calling setTime with invalid values",time);// Call the displayTime method and pass time as an argument

    }// End of main method


    private static void displayTime(String header, Time1 t) {// Start of displayTime method
    
    System.out.printf("%s%nUniversal time: %s%nStandard time: %s%n", header, t.toUniversalString(), t.toString());// Print the time in both universal and standard formats
    
    }// End of displayTime method

}// End of Time1Test class