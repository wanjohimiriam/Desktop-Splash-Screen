from tkinter import ttk
from tkinter.ttk import Progressbar

from tkinter import *

w= Tk()

#geometry

w.geometry("427x250+100+50")

# width_of_window=427
# height_of_window = 250
#
# screen_width= w.winfo_screenwidth()
# screen_height=w.winfo_height()
#
# x_coordinate= (screen_width/2)-(width_of_window/2)
# y_coordinate= (screen_height/2)-(height_of_window/2)

#w.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window, x_coordinate, y_coordinate))
#w.overrideredirect(1)

s=ttk.Style()
s.theme_use("clam")
s.configure("red.Horizontal.TProgressbar", foreground='red', background="#4f4f4f")
progress= Progressbar(w, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode="determinate")

def main_window():
    q=Tk()
    q.geometry('427x250')
    li= Label(w, text="ADD TEXT HERE", fg='dark grey')
    l=('Calibri (Body)',24, 'bold')
    li.config(font=l)
    li.place(x=80, y=100)
    q.mainloop()

def bar():
    l4= Label(w, text="Loading...", fg="white", bg='#249794')
    lst4=('Calibri (Body)', 10)
    l4.configure(font=lst4)
    l4.place(x=0, y=210)

    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    w.destroy()
    main_window()

    progress.place(x=-10, y=235)

    # #frame
    Frame(w, width=427, height=241, bg="#249794").place(x=0, y=0)
    b1=Button(w, width=10, height=1, text='Get Started', command=bar, border=0, fg='249794')
    b1.place(x=170, y=200)

    #labels
    l1= Label(w, text="SPLASH", fg='white', bg='#249794')
    lst1=("Calibri (Body)", 18, 'Bold')
    l1.configure(font=lst1)
    l1.place(x=50, y=80)

    l2 = Label(w, text="SCREEN", fg='white', bg='#249794')
    lst2 = ("Calibri (Body)", 18)
    l2.configure(font=lst2)
    l2.place(x=155, y=82)

    l3 = Label(w, text="PROGRAMMED", fg='white', bg='#249794')
    lst3 = ("Calibri (Body)", 13)
    l3.configure(font=lst3)
    l3.place(x=50, y=110)



w.mainloop()