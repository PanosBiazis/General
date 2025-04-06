import  java.awt.Color;// importing the color class
import  java.awt.Graphics;// importing the graphics class

import  javax.swing.JPanel;// importing the jpanel class

public class DrawRainbow extends JPanel {// creating a class called DrawRainbow that extends JPanel
    
    private final static Color VIOLET = new Color(128, 0, 128);
    private final static Color INDIGO = new Color(75, 0, 130);

    private Color[] colors = {Color.WHITE,Color.WHITE,VIOLET,INDIGO,Color.BLUE, Color.GREEN,Color.YELLOW,Color.ORANGE,Color.RED};

    public DrawRainbow() {// constructor

        setBackground(Color.WHITE);// setting the background color to white

    }// end constructor

    public void paintComponent(Graphics g) { // start of paintComponent

        super.paintComponent(g);// calling the paintComponent method of the superclass

        int radius = 20; //radius of the bow

        int centerX = getWidth() / 2; //center of the bow

        int centerY = getHeight() - 10; //center of the bow

        for(int counter = colors.length; counter > 0; counter--) { //looping through the colors array

            g.setColor(colors[counter - 1]); //setting the color of the bow

            g.fillArc(centerX - counter * radius, centerY - counter * radius, counter * 2 * radius, counter * 2 * radius, 0, 180); //drawing the bow

        } //end for loop

    } // end of paintComponent

}// end of class
