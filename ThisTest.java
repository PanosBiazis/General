public class ThisTest{

    public static void main(String[] args) {

        SimpleTime time = new SimpleTime(15,30,19); // Create a new SimpleTest object called time

        System.out.println(time.buildString());// Print the time object as a string

    }// End of main method

}// End of ThisTest class


class SimpleTime{


    private int hour;
    private int minute;
    private int second;

    public SimpleTime(int hour, int minute, int second) {

        this.hour = hour;
        this.minute = minute;
        this.second = second;
    
    }

    public String buildString() {

        return String.format("%24s: %s%n%24s: %s","this.toUniversalString()",this.toUniversalString(),"toUniversalString()",toUniversalString());

    }


    public String toUniversalString() {

        return String.format("%02d:%02d:%02d", this.hour, this.minute, this.second);

    }


}// End of SimpleTime class