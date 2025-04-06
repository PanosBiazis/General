import java.awt.Graphics;//imports the Graphics class
import javax.swing.JPanel;//imports the JPanel class

public class DrawPanel extends JPanel {//extends JPanel
    
    public void paintComponent(Graphics g){//overrides the paintComponent method
     
        super.paintComponent(g);//calls the paintComponent method
     
        int width = getWidth();//gets the width of the panel
     
        int height = getHeight();//gets the height of the panel
     
        g.drawLine(0,0,width,height);//draws a line from the top left corner to the bottom right corner
     
        g.drawLine(0,height,width,0);//draws a line from the top right corner to the bottom left corner
    
    }//end of paintComponent method

}//end of DrawPanel class
