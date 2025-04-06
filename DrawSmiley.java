import java.awt.Color;// import necessary classes

import java.awt.Graphics;// import necessary classes

import javax.swing.JPanel;// import necessary classes

public class DrawSmiley extends JPanel {// start of class DrawSmiley extends Jpanel

    public void paintComponent(Graphics g) { // start of paintComponent

        super.paintComponent(g);// call super class paintComponent

        // draw the face
        g.setColor(Color.yellow);// set color to yellow

        g.fillOval(10, 10, 200, 200);// draw oval with radius 100 pixels

        // draw the eyes
        g.setColor(Color.black);// set color to black

        g.fillOval(55, 65, 30, 30);// creates ovals that are 30 pixels in both width and height

        g.fillOval(135, 65, 30, 30);// creates ovals that are 30 pixels in both width and height

        // draw the mouth
        g.fillOval(50, 110, 120, 60);// draw oval with width 120 pixels and height 60 pixels

        // draw the mouth smile
        g.setColor(Color.yellow);// set color to yellow

        g.fillRect(50, 110, 120, 30);// draw rectangle with width 120 pixels and height 30 pixels

        g.fillRect(50, 120, 120, 40);// draw rectangle with width 120 pixels and height 40 pixels
    
}//end of paintComponent

}// End of class DrawSmiley
/*
 * First parameter (55 and 135): The x-coordinate position for each eye
 *Second parameter (65): The y-coordinate position for both eyes
 *Third parameter (30): The width of each eye
 *Fourth parameter (30): The height of each eye
 */