//single line comments

/*  
 * multi line comments
 * 
 */


import java.util.Scanner;// import the Scanner class
// import java.awt.Toolkit;// import the Toolkit class
import javax.swing.JOptionPane;// import the JOptionPane class




public class App {// class of name App of the main program

    public class Account {// class of name Account
    
        private String name;// private variable of type String
        private double balance;// private variable of type double

        public Account(String name, double balance) {
            this.name = name;
            this.balance = balance;
        }

        public void  setName(String name){// public method of type void
        
            this.name = name;// set the value of the name variable
            
        }


        public void setBalance(double balance){// public method of type void
        
            this.balance = balance;// set the value of the balance variable
            
        }


        public double getBalance(){// public method of type double
        
            return balance;// return the value of the balance variable
        
        }
            
        public String getName(){// public method of type String
            
            return name;// return the value of the name variable
               
        }// end of method
    
            
    }// end of class

        // ANSI escape codes for colors
        public static final String RESET = "\u001B[0m";
        public static final String RED = "\u001B[31m";
        public static final String GREEN = "\u001B[32m";
        public static final String YELLOW = "\u001B[33m";
        public static final String BLUE = "\u001B[34m";
        public static final String PURPLE = "\u001B[35m";
        public static final String CYAN = "\u001B[36m";
        public static final String WHITE = "\u001B[37m";
        public static final String BLACK = "\u001B[30m";

        // Bright/Bold colors
        public static final String BRIGHT_BLACK = "\u001B[90m";
        public static final String BRIGHT_RED = "\u001B[91m";
        public static final String BRIGHT_GREEN = "\u001B[92m";
        public static final String BRIGHT_YELLOW = "\u001B[93m";
        public static final String BRIGHT_BLUE = "\u001B[94m";
        public static final String BRIGHT_PURPLE = "\u001B[95m";
        public static final String BRIGHT_CYAN = "\u001B[96m";
        public static final String BRIGHT_WHITE = "\u001B[97m";

        // Background colors
        public static final String BG_BLACK = "\u001B[40m";
        public static final String BG_RED = "\u001B[41m";
        public static final String BG_GREEN = "\u001B[42m";
        public static final String BG_YELLOW = "\u001B[43m";
        public static final String BG_BLUE = "\u001B[44m";
        public static final String BG_PURPLE = "\u001B[45m";
        public static final String BG_CYAN = "\u001B[46m";
        public static final String BG_WHITE = "\u001B[47m";

        // Bright Background colors
        public static final String BG_BRIGHT_BLACK = "\u001B[100m";
        public static final String BG_BRIGHT_RED = "\u001B[101m";
        public static final String BG_BRIGHT_GREEN = "\u001B[102m";
        public static final String BG_BRIGHT_YELLOW = "\u001B[103m";
        public static final String BG_BRIGHT_BLUE = "\u001B[104m";
        public static final String BG_BRIGHT_PURPLE = "\u001B[105m";
        public static final String BG_BRIGHT_CYAN = "\u001B[106m";
        public static final String BG_BRIGHT_WHITE = "\u001B[107m";

        /*Bold: "\u001B[1m"
        Underline: "\u001B[4m"
        Background colors: "\u001B[41m" (red background) */

    
    public static void main(String[] args) throws Exception {// main method
        
        System.out.println("Hello, World!");// print Hello, World!

        System.out.print("Welcome to ");// print Welcome to

        System.out.println(" Java Programming!");// print Java Programming! and a new line

        System.out.println("Welcome\nto\nJava\nProgramming!");// print Welcome to Java Programming! and a new line

        System.out.println("new line");// print new line

        System.out.print("\nnew line\n");// print new line

        System.out.print("tab\ttab\n");// print tab tab

        System.out.print("return line\rreturn line\n");// print return line return line

        System.out.print("backspace\bbackspace\n");// print backspace backspace

        System.out.println("escape sequence \t\\t\n");// print escape sequence \t and a new line

        System.out.println("escape sequence \n\\n\n");// print escape sequence \n and a new line

        System.out.println("escape sequence \b\\b\n");// print escape sequence \b and a new line

        System.out.println("escape sequence \r\\r\n");// print escape sequence \r and a new line

        System.out.println("escape sequence \f\\f\n");// print escape sequence \f and a new line

        System.out.println("\\");// print \

        System.out.println("\"in quotes\"");// print "in quotes"

        System.out.println("\'in quotes\'");// print 'in quotes'

        // Make a beep sound
        // Toolkit.getDefaultToolkit().beep();
        
        // System.out.println("You should hear a beep!");

        System.out.printf("Hello, %s!\n", "World");// print Hello, World! and a new line

        // System.out.printf("Hello, %s!\n", "World");// print Hello, World! and a new line

        System.out.printf("%s\u0020%s%n","Welcome to","Java Programming!");// print Welcome to<space character>Java Programming! and a new line

        Scanner scanner = new Scanner(System.in);// create a new Scanner object

        int number,// declare a variable of type int
            number2,// declare a variable of type int
            result;// declare a variable of type int

        /*
         * int number,// declare a variable of type int
         * int number2,// declare a variable of type int
         * int result;// declare a variable of type int
         */

        System.out.print("Enter a number: ");// print Enter a number:

        number = scanner.nextInt();// read a number from the user

        System.out.print("Enter another number: ");// print Enter another number:

        number2 = scanner.nextInt();// read another number from the user

        result = number + number2;// add the two numbers

        System.out.printf("%d + %d = %d\n", number, number2, result);// print the result

        scanner.nextLine();// read the newline character

        System.out.print("Write something: ");// print Write something:

        String input = scanner.nextLine();// read a string from the user

        System.out.println("You wrote: " + input);// print You wrote: <input>
        
        System.out.println("Sum of 10 and 20 is " + (10 + 20));// print Sum of 10 and 20 is 30

        System.out.println("Sum of 10 and 20 is " + 10 + 20);// print Sum of 10 and 20 is 1020

        System.out.printf("The Sum is %d\n",(number + number2));// print The Sum is <result>

        // scanner.close();// close the scanner

        //comparison semi-program

        int number3,// declare a variable of type int
            number4;// declare a variable of type int

        System.out.println("Enter a number: ");
        
        number3 = scanner.nextInt();
        
        System.out.println("Enter another number: ");
        
        number4 = scanner.nextInt();

        if(number3 == number4){// if the two numbers are equal

            System.out.printf("%d == %d\n", number3, number4);// print <number3> === <number4>

        }

        if(number3 != number4){// if the two numbers are not equal

            System.out.printf("%d != %d\n", number3, number4);// print <number3> !== <number4>

        }
        
        if(number3 > number4){// if the first number is greater than the second number

            System.out.printf("%d > %d\n", number3, number4);// print <number3> > <number4>
        
        }
        
        if(number3 < number4){// if the first number is less than the second number
        
            System.out.printf("%d < %d\n", number3, number4);// print <number3> < <number4>
        
        }
        
        if(number3 >= number4){// if the first number is greater than or equal to the second number
        
            System.out.printf("%d >= %d\n", number3, number4);// print <number3> >= <number4>
        
        }
        if(number3 <= number4){// if the first number is less than or equal to the second number
        
            System.out.printf("%d <= %d\n", number3, number4);// print <number3> <= <number4>
        
        }

        System.out.println(RED+"..........*********...........***............*...........*............\n"+RESET);// 
        System.out.println(GREEN+"..........*.......*........*.......*........***........*...*..........\n"+RESET);//
        System.out.println(YELLOW+"..........*.......*.......*.........*......*****......*.....*.........\n"+RESET);//
        System.out.println(BLUE+"..........*.......*.......*.........*........*.......*.......*........\n"+RESET);//
        System.out.println(PURPLE+"..........*.......*.......*.........*........*.....*...........*......\n"+RESET);//
        System.out.println(CYAN+"..........*.......*.......*.........*........*.......*.......*........\n"+RESET);//
        System.out.println(WHITE+"..........*.......*.......*.........*........*........*.....*.........\n"+RESET);//
        System.out.println(BRIGHT_RED+"..........*.......*........*.......*.........*.........*...*..........\n"+RESET);//
        System.out.println(BRIGHT_BLUE+"..........*********...........***............*...........*............\n"+RESET);//

        // scanner2.close();// close the scanner

        


        // Account account1 = new Account();// create a new Account object
        // Account account2 = new Account();// create a new Account object

        // account1.setName("John Doe");// set the name of the first object
        // account1.setBalance(1000.9912);// set the balance of the first object
        // account2.setName("Jane Doe");// set the name of the second object
        // account2.setBalance(2000.6445);// set the balance of the second object

        // // display initial balance of each object

        // System.out.printf("%s balance: $%4.2f\n", account1.getName(), account1.getBalance());
        // System.out.printf("%s balance: $%4.2f\n", account2.getName(), account2.getBalance());

        String name = JOptionPane.showInputDialog("Enter your name: ");// declare a variable of type string

        int age = Integer.parseInt(JOptionPane.showInputDialog("Enter your age: "));// declare a variable of type int

        String message = String.format("Hello %s, you are %d years old.", name, age);// declare a variable of type string
        String message2;

        JOptionPane.showMessageDialog(null, message);// display the message

        if(age < 18){// if the age is less than 18
            message2 = String.format("You are %d years old my little child\nyou have a little time to live\n Enjoy it.",age);// declare a variable of type string
            JOptionPane.showMessageDialog(null, message2);
        }
        else{
            message2 = String.format("You are %d years old my old friend\nYOU HAVE TO DIE!!!",age);// declare a variable of type string
            JOptionPane.showMessageDialog(null, message2);
        }    



        int studentgrades;

        // Scanner input3 = new Scanner(System.in);

        // input3.useDelimiter("\n");

        System.out.println("Enter your grades: ");// prompt the user to enter the grades
        // studentgrades = input3.nextInt();
        studentgrades = scanner.nextInt();// read the grades

        System.out.println("Your grades are: " + studentgrades);// display the grades

        System.out.println(studentgrades >= 90 ? "A" : studentgrades >= 80 ? "B" : studentgrades >= 70 ? "C" : studentgrades >= 60 ? "D" : "F");// display the grades

        // input3.close();// close the scanner

        scanner.close();// close the scanner
       

    }// end of main

}// end of class
// panos@panos-IdeaPad-Slim-9-14ITL5:/media/panos/SAMSUNG T7/panag/Documents/Java/JavaProject/myjavaproject$ javac src/App.java
// panos@panos-IdeaPad-Slim-9-14ITL5:/media/panos/SAMSUNG T7/panag/Documents/Java/JavaProject/myjavaproject$ java -cp src App