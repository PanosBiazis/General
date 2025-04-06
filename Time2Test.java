public class Time2Test {// Time2Test class

public static void main(String[] args) {// main method

    Time2 t1 = new Time2();// create a Time2 object 00:00:00

    Time2 t2 = new Time2(2);// create a Time2 object 02:00:00

    Time2 t3 = new Time2(21,34);// create a Time2 object 21:34:00

    Time2 t4 = new Time2(12,25,42);// create a Time2 object 12:25:42

    Time2 t5 = new Time2(t4); // create a Time2 object 12:25:42 by copying t4

    System.out.println("Constructed with:");// print the constructor used

    displayTime("t1: all default arguments", t1);// display t1

    displayTime("t2: hour specified; default minute and second", t2);// display t2

    displayTime("t3: hour and minute specified; default second", t3);// display t3

    displayTime("t4: hour,minute and second specified", t4);// display t4

    displayTime("t5: Time2 object t4 specified", t5);// display t5

    try {// try block
        
        Time2 t6 = new Time2(27, 74, 99);// create a Time2 object with invalid hour, minute, and second

    } catch (IllegalArgumentException e) {// catch the exception

        System.out.printf("%nException while initializing t6: %s%n",e.getMessage());// print the exception message

    }// end catch


}// end main method


private static void displayTime(String header, Time2 t) {// displayTime method

    System.out.printf("%s%n  %s%n  %s%n",header,t.toUniversalString(),t.toString());// print the header and the time in universal and standard format

}// end displayTime method


}// end Time2Test


