public class Increment {// class Increment definition

    public static void main(String[] args) {// main method

        int c = 5;// initialize c

        System.out.printf("c before increment: %d%n", c);// display c

        System.out.printf(" postincrementing c: %d%n", c++);// preincrement

        System.out.printf(" c after postincrement: %d%n", c);// display c

        System.out.println();// add a blank line

        c = 5;// initialize c

        System.out.printf("c before preincrement: %d%n", c);// display c

        System.out.printf(" preincrementing c: %d%n", ++c);// preincrement

        System.out.printf(" c after preincrement: %d%n", c);// display c
    
    }// end main

}// end class