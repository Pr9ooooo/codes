import random 
import time   
def getrandom(startdate,enddate):
    print(f"printing date between{startdate} and {enddate}")
    randomgen=random.random()
    dateFormat="%m/%d/%y"
    starttime=time.mktime(time.strptime(startdate,dateFormat))
    endtime=time.mktime(time.strptime(enddate,dateFormat))
    if starttime>endtime:
        starttime,endtime=endtime,starttime
    randomtime=starttime+randomgen*(endtime-starttime)
    randomdate=time.stfrtime(dateFormat,time.localtime(randomtime))
    return randomdate
print("Random date-",getrandom(2/2/2024,31/12/2024))

