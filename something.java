import javax.swing.JOptionPane;

public class something{//start of class

    public static void main(String[] args) throws Exception { // Start of main method

        String name = JOptionPane.showInputDialog("What is your name?");
        String message = String.format("Welcome, %s, to Java Programming!", name);
        JOptionPane.showMessageDialog(null, message);

    }// end of main

}// end of class