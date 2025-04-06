public class Student {//Student class definition
    
    private String name;//Student name
    
    private double average;//Student average

    public Student (String name, double average) {//constructor
        
        this.name = name;//assign name to instance variable name

        if(average > 0.0) {//if average is valid
            
            if(average <= 100.0) {//if average is valid
            
                this.average = average;
            
            }//end if
        
        }//end if
    
    }//end constructor

    public void setName(String name) {//set student name
        
        this.name = name;//assign name to instance variable name
    
    }//end method setName

    public String getName() {//get student name
        
        return name;//return name to caller
    
    }//end method getName

    public void setAverage(double average) {//set student average
        if(average > 0.0) {///if average is valid
            
            if(average <= 100.0) {//if average is valid
            
                this.average = average;//assign average to instance variable average
            
            }//end if
        
        }//end if
    
    }//end method setAverage

    public double getAverage() {//get student average
    
        return average;//return average to caller
    
    }//end method getAverage

    public String getLetterGrade() {//determine letter grade
        
        String letterGrade = "";//initially set letterGrade to empty string

        if(average >= 90.0) {//if average is valid
            
            letterGrade = "A";//assign letterGrade to A
        
        } //end if
        
        else if(average >= 80.0) {
         
            letterGrade = "B";//assign letterGrade to B
        
        } //end else if
        
        else if(average >= 70.0) {
        
            letterGrade = "C";//assign letterGrade to C
        
        }//end else if
        
        else if(average >= 60.0) {
        
            letterGrade = "D";//assign letterGrade to D
        }//end else if
        
        else {//if average is invalid
        
            letterGrade = "F";//assign letterGrade to F
        
        }//end else

        return letterGrade;//return letterGrade to caller
    
    }//end method getLetterGrade

}///end class Student
