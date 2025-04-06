public class Scope {// Start of class Scope
    
    private static int x = 1;// Private static variable x = 1

    public static void main(String[] args) throws Exception {// Start of method main

        int x = 5;// Local variable x = 5

        System.out.printf("local x in main is %d\n", x);// Print local x in main

        useLocalVariable();// Call method useLocalVariable

        useField();// Call method useField

        useLocalVariable();// Call method useLocalVariable

        useField();// Call method useField

        System.out.printf("\nlocal x in main is %d\n", x);// Print local x in main


    }// End of method main


    public static void useLocalVariable() {// Start of method useLocalVariable

        int x = 25;// Local variable x = 25

        System.out.printf("\nlocal x on entering method useLocalVariable is %d\n", x);// Print local x on entering method useLocalVariable

        ++x;// Increment x by 1

        System.out.printf("local x before exiting method useLocalVariable is %d\n", x);// Print local x before exiting method useLocalVariable

    }// End of method useLocalVariable


    public static void useField() {// Start of method useField

        System.out.printf("\nfield x on entering method useField is %d\n", x);// Print field x on entering method useField

        x *= 10;// Multiply x by 10

        System.out.printf("field x before exiting method useField is %d\n", x);// Print field x before exiting method useField

    }// End of method useField

}// End of class Scope
