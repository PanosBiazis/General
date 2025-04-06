// /**
//  * A strongly typed main class.
//  */
// package javaproj;

// /**
//  * A strongly typed main class.
//  */

// import java.util.Scanner;

// public class MainJ {

// 	/**
// 	 * A constructor that takes no arguments.
// 	 */
// 	public MainJ() {
// 		// TODO Auto-generated constructor stub
// 		System.out.println("Main constructor");
// 	}

// 	/**
// 	 * A main method that takes an array of strings as an argument and returns nothing.
// 	 * @param args An array of strings.
// 	 */
// 	public static void main(String[] args) {
// 		// TODO Auto-generated method stub
// 		System.out.println("Hello Java!!!");
// 		System.out.print("Press Enter to continue...");
//         Scanner scanner = new Scanner(System.in);
//         scanner.nextLine(); // wait for user to press Enter
// 		scanner.close();
// 	}

// }

package javaproj;

import java.util.Scanner;

public class MainJ {

    /**
     * A constructor that takes no arguments.
     */
    public MainJ() {
        System.out.println("Main constructor");
    }

    /**
     * A main method that takes an array of strings as an argument and returns nothing.
     * @param args An array of strings.
     */
    public static void main(String[] args) {
        System.out.println("Hello Java!!!");
        System.out.print("Press Enter to continue...");

        // Using try-with-resources to automatically close the Scanner
        try (Scanner scanner = new Scanner(System.in)) {
            scanner.nextLine(); // wait for user to press Enter
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}

