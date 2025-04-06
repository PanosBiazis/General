import javax.swing.JFrame;//imports the JFrame class

public class DrawPanelTest {//main class

    public static void main(String[] args) {//main method
        
        DrawPanel panel = new DrawPanel();//create DrawPanel object

        JFrame application = new JFrame();//create JFrame object

        application.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//set default close operation

        application.add(panel);//add DrawPanel object to JFrame object

        application.setSize(300, 300);//set size of JFrame object

        application.setVisible(true);//make JFrame object visible
    
    }//end main
    
}//end class DrawPanelTest
