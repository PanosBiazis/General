import javax.swing.JFrame;// import javax.swing.JComponent;

public class DrawRainbowTest {// class DrawRainbowTest
    
    public static void main(String[] args) throws Exception {// main method
        
        DrawRainbow panel = new DrawRainbow();// create DrawRainbow object

        JFrame application = new JFrame();// create JFrame object

        application.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);// set default close operation

        application.add(panel);// add DrawRainbow object to JFrame object

        application.setSize(400, 250);// set size of JFrame object

        application.setVisible(true);// make JFrame object visible

    }// end of main

}// end of class DrawRainbowTest
