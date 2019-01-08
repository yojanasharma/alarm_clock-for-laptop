import tkinter as tk
from tkinter import *
import  time
from selenium import webdriver
from tkinter import messagebox
global in_hr,in_min,in_alarm,delay
def calc_delay(hr,min):
    local_time=time.localtime()
    hr1=local_time.tm_hour
    min1=local_time.tm_min
    delay=hr-hr1
    if delay<0:
        print("sorry")
    else:
        delay2=min-min1
        delay=delay+delay2
        delay=delay*60
    return (delay)

def alarm(set_alarm):
    driver=webdriver.Firefox()
    driver.get("https://www.youtube.com/results?search_query="+set_alarm)
    driver.find_element_by_id("video-title").click()


def message1():
   print("called")

   in_hr = int(ehr.get())
   print(in_hr)
   in_min =int(em.get())
   print(in_min)
   in_alarm=ea.get()
   print(in_alarm)
   am_pm = var_char.get()
   print(am_pm)
   if am_pm==1:
       in_hr=in_hr
   else:
       in_hr=in_hr+12
       delay1=calc_delay(in_hr,in_min)
   message=messagebox.showinfo("alarm set","Your alarm will ring in "+ str(delay1)+"sec")
   time.sleep(delay1)
   alarm(in_alarm)

root=tk.Tk()
root.geometry("500x500")
b1=tk.Label(text="hour",bg="red",fg="green").grid(row=1,column=1)
b2=tk.Label(text="min",bg="red",fg="green").grid(row=2,column=1)
b3=tk.Label(text="alarm",bg="red",fg="green").grid(row=3,column=1)
b4=tk.Button(root,text="ok",bd=5,fg="purple",command=message1).grid(row=6,column=1)
ehr=tk.Entry(root,bd=5)
ehr.grid(row=1,column=2)
em=tk.Entry(root,bd=5)
em.grid(row=2,column=2)
ea=tk.Entry(root,bd=5)
ea.grid(row=3,column=2)
var_char=IntVar()
rd1=tk.Radiobutton(root,text="am",bd=5,variable=var_char,value=1).grid(row=4,column=1)
rd2=tk.Radiobutton(root,text="pm",bd=5,variable=var_char,value=2).grid(row=4,column=2)
txt=tk.Text(root,width=25,height=25,bd=5).grid(row=7,columnspan=4)
root.mainloop()

