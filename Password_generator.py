from tkinter import *
from tkinter import messagebox
import random

import string

def genrate_password():
    try:
        length=int(entry_No_of_Word.get())
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        
        all = lower + upper + num + symbols

        
        temp = random.sample(all,length)

        
        password = "".join(temp)
   
        
        entry.delete(0, END)
        entry.insert(0,password)
    except:
        messagebox.showerror("Error!","Please Use Integer Values Only.")
        

win=Tk()

win.title("Password Genrator")
win.geometry("475x300")

No_of_Word=Label(win,text="Enter No. of Character in Password:")
No_of_Word.place(x=0,y=70)

entry_No_of_Word=Entry(win)
entry_No_of_Word.place(x=240,y=75)

gen_pass = Label(win, text = 'Generated Password')
gen_pass.place(x=0,y=100)

entry = Entry(win)
entry.place(x=240,y=105)

label_title=Label(win,text="Create Your Random Password",font=("Algerian", 20))
label_title.pack()

Create_button=Button(win,text="Create Password",command=genrate_password)
Create_button.place(x=174,y=140)

mainloop()