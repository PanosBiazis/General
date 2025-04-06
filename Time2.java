public class Time2{

    private int hour;// 0-23
    private int minute;// 0-59
    private int second;// 0-59


    public Time2(){// default constructor

    this(0,0,0); //  default constructor

   }// end default constructor

   public Time2(int hour){// constructor with hour
   
    this(hour,0,0);// default constructor
   
   }// end constructor with hour

   public Time2(int hour, int minute){// constructor with hour and minute

   this(hour,minute,0);// call constructor with parameters

   }// end constructor with hour and minute

   public Time2(int hour, int minute, int second){// constructor with parameters

   if(hour < 0 || hour >=24){// check for valid hour

    throw new IllegalArgumentException("hour must be between 0 and 23");// throw exception

   }// end if

   if (minute < 0 || minute >= 60){// check for valid minute

    throw new IllegalArgumentException("minute must be between 0 and 59");// throw exception

   }// end if

   if (second < 0 || second >= 60){// check for valid second

    throw new IllegalArgumentException("second must be between 0 and 59");// throw exception

   }// end if

   this.hour = hour;// set hour
   this.minute = minute;// set minute
   this.second = second;// set second

}// end constructor with parameters

public Time2(Time2 time){// copy constructor

    this(time.getHour(), time.getMinute(), time.getSecond());// call constructor with parameters

}// end copy constructor

public void setTime(int hour,int minute,int second){// set time

    if(hour < 0 || hour >=24){// check for valid hour

    throw new IllegalArgumentException("hour must be between 0 and 23");// throw exception

   }// end if

   if (minute < 0 || minute >= 60){// check for valid minute

    throw new IllegalArgumentException("minute must be between 0 and 59");// throw exception

   }// end if

   if (second < 0 || second >= 60){// check for valid second

    throw new IllegalArgumentException("second must be between 0 and 59");// throw exception

   }// end if

this.hour = hour;// set hour
this.minute = minute;// set minute
this.second = second;// set second


}// end setTime

public void setHour(int hour){// set hour

    if (hour < 0 || hour >=24){// check for valid hour

    throw new IllegalArgumentException("hour must be between 0 and 23");// throw exception

   }// end if

   this.hour = hour;// set hour

}// end setHour

public void setMinute(int minute){// set minute

    if (minute < 0 || minute >= 60){// check for valid minute

    throw new IllegalArgumentException("minute must be between 0 and 59");// throw exception

    }// end if

    this.minute = minute;// set minute

}// end setMinute

public void setSecond(int second){// set second

    if (second < 0 || second >= 60){// check for valid second

    throw new IllegalArgumentException("second must be between 0 and 59");// throw exception

    }// end if

    this.second = second;// set second

}// end setSecond

public int getHour(){// get hour

    return hour;// return hour

}// end getHour

public int getMinute(){// get minute

    return minute;// return minute

}// end getMinute

public int getSecond(){// get second

    return second;// return second

}// end getSecond

public String  toUniversalString(){// convert time to string in universal time format

    return String.format("%02d:%02d:%02d", getHour(), getMinute(), getSecond());// return string in universal time format

}// end toUniversalString

public String toString(){// convert time to string in standard time format

    return String.format("%d:%02d:%02d %s",((getHour() == 0 || getHour() == 12) ? 12 : getHour() % 12),getMinute(),getSecond(),(getHour() < 12 ? "AM" : "PM"));// return string in standard time format

}// end toString

}// end Time2 class