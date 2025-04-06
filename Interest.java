public class Interest {//class
    
    public static void main(String[] args) {//main method
        
        double principal = 1000;//initial principal
        
        double rate = 0.05;//initial rate
        
        double amount;//amount on deposit at end of each year

        System.out.println("Year\tAmount on deposit");//heading

        for (int year = 1; year <= 10; year++) {///for loop
            
            amount = principal * Math.pow(1.0 + rate, year);//calculate new amount for specified year
            
            System.out.printf("%4d%,20.2f\n", year, amount);//display the year and the amount
        
        }//end for
    
    }//end main


}//end class Interest
