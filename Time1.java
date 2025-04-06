public class Time1{// Time1.java

    private int hour;// hour 0-23
    private int minute;// minute 0-59
    private int second;// second 0-59

    public void setTime(int hour, int minute, int second) {// set time
    
        if(hour<0 || hour >= 24 || minute< 0 || minute >= 60 || second<0 || second >= 60) {// check if the time is valid
    
            throw  new IllegalArgumentException("hour, minute and/or second was out of range");// throw an exception if the time is invalid
    
        }// end if
    
    this.hour = hour;// set the hour
    this.minute = minute;// set the minute
    this.second = second;// set the second

    }// end setTime method


    public String toUniversalString(){// convert time to string in universal time format

        return String.format("%02d:%02d:%02d", hour, minute, second);// format the string with leading zeros if necessary
    
    }// end toUniversalString method

    @Override// override the toString method to convert time to string in standard time format
    public String toString() {// convert time to string in 12 hour format with AM/PM

        return String.format("%d:%02d:%02d %s",((hour == 0 || hour == 12) ? 12 : hour % 12),minute,second,(hour < 12 ? "AM" : "PM"));// format the string with leading zeros if necessary

    }// end toString method

}// end Time1 class