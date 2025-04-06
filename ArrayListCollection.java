import java.util.ArrayList;// (1) import the ArrayList class

import javax.swing.plaf.basic.BasicInternalFrameUI;

public class ArrayListCollection {// <--- ArrayListCollection class
    
    public static void main(String[] args) throws  Exception {// <--- main method

        ArrayList<String> items = new ArrayList<String>();// (2) create an ArrayList of Strings

        items.add("red"); // (3) add an item to the ArrayList

        items.add(0,"yellow");// (4) add an item at the beginning of the ArrayList

        System.out.print("Display list contents with counter-controlled loop:");// (5) print a message

        for (int i = 0; i < items.size(); i++) {// (6) use a counter-controlled loop to display the ArrayList contents

            System.out.printf(" %s",items.get(i));

        }// end for

        display(items,"%nDisplay list contents with enhanced for statement:"); // (7) call the display method

        items.add("green");// (8) add an item to the ArrayList

        items.add("yellow");// (9) add an item to the ArrayList

        display(items,"List with two new elements:");// (10) call the display method

        items.remove("yellow");// (11) remove an item from the ArrayList

        display(items,"Remove first instance of yellow:");// (12) call the display method

        items.remove(1);// (13) remove an item from the ArrayList

        display(items,"Remove second list element (green):");// (14) call the display method

        System.out.printf("\"red\" is %sin the list%n",items.contains("red") ? "":"not ");// (15) check if an item is in the ArrayList

        System.out.printf("Size: %s%n", items.size()); // (16) print the size of the ArrayList
    
    }// end main method


    public static void display(ArrayList<String> items, String header) {// <--- display method

        System.out.print(header);// (17) print the header

        for (String item : items) {// (18) use a for-each loop to display the ArrayList contents

            System.out.printf(" %s",item);

        }// end for

        System.out.println();

    }// end display method


}// end class ArrayListCollection
