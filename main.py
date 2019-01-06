import time
from selenium import webdriver
d=time.localtime()
hour1=d.tm_hour
min1=d.tm_min
in_hr=int(input("enter alarm set in  hr(24)\n"))
in_min=int(input('enter min(60):\n'))
print(in_min-min1)
if hour1 > in_hr:
    print("ït will ring tomorrow")
else:
    set_alarm_ringtone = input("set your alarm ringtone")
    delay =(in_hr-hour1)*60
    delay2=in_min-min1
    delay=delay + delay2
print("your alarm will ring in "+str(delay) +"min")
time.sleep(delay*60)


#this code will open the youtube link
driver = webdriver.Firefox()

driver.get("https://www.youtube.com/results?search_query="+set_alarm_ringtone)
driver.find_element_by_id("video-title").click()



