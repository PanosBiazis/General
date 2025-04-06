public class AutoPolicy {//class
    
    private int accountNumber;//instance variable

    private String makeAndModel;//instance variable
    
    private String state;//instance variable

    public AutoPolicy(int accountNumber, String makeAndModel, String state) {//constructor
    
        this.accountNumber = accountNumber;//assigning the value of the instance variable
    
        this.makeAndModel = makeAndModel;//assigning the value of the instance variable
    
        this.state = state;//assigning the value of the instance variable
    
    }//end constructor

    public int getAccountNumber() {//method
        
        return accountNumber;//returning the value of the instance variable
    
    }//end method

    public String getMakeAndModel() {//method

        return makeAndModel;//returning the value of the instance variable
    
    }// end method

    public String getState() {//method

        return state;//returning the value of the instance variable
    
    }//end method

    public void setAccountNumber(int accountNumber) {//method
        
        this.accountNumber = accountNumber;//assigning the value of the instance variable

    }//end method

    public void setMakeAndModel(String makeAndModel) {//method

        this.makeAndModel = makeAndModel;//assigning the value of the instance variable
    
    }//end method

    public void setState(String state) {//method

        this.state = state;//assigning the value of the instance variable
    
    }//end method


    public boolean isNoFaultState() {//method
        
        boolean noFaultState;//local variable

        switch (getState()) {//switch statement
            case "MA": case "NJ": case "NY": case "PA"://case statement
                
                noFaultState = true;//assigning the value of the local variable

                break;//break statement
            
            default://default case
                
                noFaultState = false;//assigning the value of the local variable

                break;//break statement

        }//end switch statement

        return noFaultState;//returning the value of the local variable

    }//end method

}//end class
