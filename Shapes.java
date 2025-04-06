import java.awt.Graphics;//importing the graphics class

import javax.swing.JPanel;//importing the jpanel class

public class Shapes extends JPanel{//creating a class called shapes that extends the jpanel class

    private int choice;//declaring a private integer variable called choice

    private int times;//declaring a private integer variable called times

    public Shapes(int userChoice, int userTimes){//creating a constructor that takes an integer parameter called userChoice
     
        choice = userChoice;//setting the value of choice to the value of userChoice
    
        times = userTimes;//setting the value of times to the value of userTimes

    }

    public void paintComponent(Graphics g){//creating a method called paintComponent that takes a graphics object as a parameter

        super.paintComponent(g);//calling the paintComponent method of the superclass

        for(int i = 0;  i < times; i++){//creating a for loop that will run 10 times

            switch(choice){//creating a switch statement that will check the value of choice

                case 1://case 1
                    
                    g.drawRect(10+i*10,10+i*10,50+i*10,50+i*10);//drawing a rectangle

                    break;//breaking out of the switch statement

                case 2://case 2

                    g.drawOval(10+i*10,50+i*10,50+i*10,10+i*10);//drawing an oval

                    break;//breaking out of the switch statement

            }//end of switch statement

        }//end of for loop

    }//end of paintComponent method


}//end of class
