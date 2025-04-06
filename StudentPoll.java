public class StudentPoll {//class declaration StudentPoll
    
    public static void main(String[] args){ //throws Exception {//main method
 
        int[] responses = { 1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 14 };//array of responses

        int[] frequency = new int[6];//array of frequency counters

        for (int answer = 0; answer < responses.length; answer++){//for loop to count frequency of responses

            try{//try block
            
                ++frequency[responses[answer] - 1];//increment frequency counter

            }//end try

            catch(ArrayIndexOutOfBoundsException e){//catch block
                
                System.out.println(e);//print error message
                
                System.out.println("Invalid response: " + responses[answer]);//print error message
            
            }//end catch


        }//end for loop
        

        System.out.println("Rating\tFrequency");//print header


        for (int rating = 1; rating < frequency.length; rating++){//for loop to print frequency of responses


            System.out.println(rating + "\t" + frequency[rating]);//print frequency of responses
            
        
        }//end for loop


    }//end main


}//end class StudentPoll
