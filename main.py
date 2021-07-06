from datetime import *
from playsound import playsound
dateInput = int(input("Enter the date:  "))
hourInput = int(input("Enter hour in 24 hours format:  "))
minuteInput = int(input("Enter minute:  "))
def myAlarm():
    current_time = datetime.now() 
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    if(dateInput==int(day)):
        if(hourInput==int(hour)):
            if(minuteInput==int(minute)):
                playsound("song.mp3")
                return True
            else:
                return False
        else:
            return False
    else:
        return False

while myAlarm!=True:
    myAlarm()
        

        