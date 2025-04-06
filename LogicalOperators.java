public class LogicalOperators {//class
    
    public static void main(String[] args){//main

        System.out.printf("%s%n%s:  %b%n%s:  %b%n%s:  %b%n%s:  %b%n%n","Conditional AND (&&)","false && false",false && false,"false && true",false && true,"true && false",true && false,"true && true",true && true);//print

        System.out.printf("%s%n%s:  %b%n%s:  %b%n%s:  %b%n%s:  %b%n%n","Conditional OR (||)","false || false",false || false,"false || true",false || true,"true || false",true || false,"true || true",true || true);//print
        
        System.out.printf("%s%n%s:  %b%n%s:  %b%n%s:  %b%n%s:  %b%n%n","Conditional AND (&)","false && false",false & false,"false & true",false & true,"true & false",true & false,"true & true",true & true);//print
        
        System.out.printf("%s%n%s:  %b%n%s:  %b%n%s:  %b%n%s:  %b%n%n","Conditional OR (|)","false | false",false | false,"false | true",false | true,"true | false",true | false,"true | true",true | true);//print
        
        System.out.printf("%s%n%s:  %b%n%s:  %b%n%s:  %b%n%s:  %b%n%n","Exclusive OR (^)","false ^ false",false ^ false,"false ^ true",false ^ true,"true ^ false",true ^ false,"true ^ true",true ^ true);//print
        
        System.out.printf("%s%n%s:  %b%n%s: %b%n","Logical NOT (!)","!false",!false,"!true",!true);//print


}//main

}//class