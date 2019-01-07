import tkinter  as tk
root=tk.Tk()
def set_Alarm():
    alarm=input("\n Enter your alarm ringtone:")
    return(alarm)
def ask_hr():
    hr=input("\n enter time in hour:")
    return(hr)
def ask_min():
    min=input("\n Enter min:")
    return (min)

def guiutility():
    root = tk.Tk()
    try:
        w1=tk.Label(root,text="An alarm clock",fg="red",bg="light green",font="Arial 12 bold")
        w1.pack()
        b1=tk.Button(root,text="hour",fg="blue",bg="red",command=ask_hr)
        b1.pack(side="left")
        b2=tk.Button(root,text="min",fg="blue",bg="red",command=ask_min)
        b2.pack(side="right")
    except:
        print(("button cant be priny")

# def alarm_utility():
#     b3=tk.Button(root,text="alarm",fg="blue",bg="red",command=set_Alarm)
#     b3.pack(side="bottom")
#root.mainloop