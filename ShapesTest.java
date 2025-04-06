import javax.swing.JFrame;//imports the JFrame class

import javax.swing.JOptionPane;//imports the JOptionPane class

public class ShapesTest {//class ShapesTest
    
    public static void main(String[] args) {//main method
    
        String input = JOptionPane.showInputDialog("Enter 1 to draw rectangles\n" +"Enter 2 to draw ovals");//prompts the user to enter 1 or 2
      
        int choice = Integer.parseInt(input);//converts the input to an integer

        input = JOptionPane.showInputDialog("Enter the number of shapes");//prompts the user to enter the number of shapes
        
        int times = Integer.parseInt(input);//converts the input to an integer
      
        Shapes panel = new Shapes(choice, times);//creates a Shapes object

        JFrame application = new JFrame();//creates a JFrame object
      
        application.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//sets the default close operation
      
        application.add(panel);//adds the Shapes object to the JFrame object
      
        application.setSize(1200, 1200);//sets the size of the JFrame object
      
        application.setVisible(true);//makes the JFrame object visible
    
    }

}
