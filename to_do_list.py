

from tkinter import *
from tkinter import messagebox

win=Tk()


def add_task():
    a=entry.get()
    
    if a!='':
        def del_task():
            b.destroy()
            c.destroy()
            d.destroy()
        def edit():
            k=a
            entry.delete(0, END)
            entry.insert(0,k)

            return del_task()
        
        
         
    
        b=Label(win,text=a,font=("Algerian", 12))
        b.pack(anchor="w")
        b.configure(bg="#414d54",fg="#fffbfb")
        c=Button(win,text="Edit",command=edit)
        c.pack(anchor="c")
        c.configure(bg="#414d54",fg="#fffbfb")
        d=Button(win,text="delete", command=del_task)
        d.pack(anchor="c")
        d.configure(bg="#414d54",fg="#fffbfb")
        entry.delete(0, END)

    else :
        messagebox.showerror("Error","Please Enter Task ")
            
    
    
win.title("To Do List")
win.geometry("250x300")
win.configure(bg="#414d54")


label=Label(win,text="Enter Task:")
label.pack(anchor="w")
label.configure(bg="#414d54",fg='#fffbfb',font=("Algerian", 12))

entry=Entry(win)
entry.pack(anchor="w")
entry.configure(bg="#414d54",fg="#fffbfb")

Sumit_button=Button(win,text="Sumit",command=add_task,font=("Algerian", 10))
Sumit_button.place(x=140,y=20)
Sumit_button.configure(bg="#414d54",fg='#fffbfb')






win.mainloop()