import javax.swing.JFrame;//imports the JFrame class

public class DrawSmileyTest {// class DrawSmileyTest

    public static void main(String[] args) {// start of main method

        DrawSmiley panel = new DrawSmiley();// create DrawSmiley object
        
        JFrame application = new JFrame();// create JFrame object
   
        application.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);// set default close operation
        
        application.add(panel);// create JFrame object
        
        application.setSize(230, 250);// set size of JFrame object
        
        application.setVisible(true);// set JFrame object to visible
    
    }//end main

}//end class DrawSmileyTest
