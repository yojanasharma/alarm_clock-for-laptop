import time
import gui

from selenium import webdriver
print("dontkno")
d=time.localtime()
hour1=d.tm_hour
min1=d.tm_min
try:
    gui.guiutility()
    print("ÿou were her")
except:
    print("fdg")
gui.guiutility()
in_hr=int(gui.ask_hr())
in_min=int(gui.ask_min())
if hour1 > in_hr:
    print("ït will ring tomorrow")
else:
    gui.alarm_utility()
    set_alarm_ringtone = gui.set_Alarm()
    delay =(in_hr-hour1)*60
    delay2=in_min-min1
    delay=delay + delay2
print("your alarm will ring in "+str(delay) +"min")
time.sleep(delay*60)


#this code will open the youtube link
driver = webdriver.Firefox()

driver.get("https://www.youtube.com/results?search_query="+set_alarm_ringtone)
driver.find_element_by_id("video-title").click()
