from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Calculator")
win.geometry("185x180")

field_text = ''


def field_txt(variable):
    global field_text
    field_text = field_text + str(variable)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)


def calculate():
    try:
        global field_text
        result = str(eval(field_text))
        field.delete("1.0", "end")
        field.insert("1.0", result)
    except:
        messagebox.showinfo("Error!", "Something went wrong")


def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")


field = Text(win, height=2, width=21)
field.grid(row=1, column=1, columnspan=4)
C1 = Button(win, text="1", command=lambda: field_txt(1), width=5)
C1.grid(row=2, column=1)
C2 = Button(win, text="2", command=lambda: field_txt(2), width=5)
C2.grid(row=2, column=2)
C3 = Button(win, text="3", command=lambda: field_txt(3), width=5)
C3.grid(row=2, column=3)
C4 = Button(win, text="4", command=lambda: field_txt(4), width=5)
C4.grid(row=3, column=1)
C5 = Button(win, text="5", command=lambda: field_txt(5), width=5)
C5.grid(row=3, column=2)
C6 = Button(win, text="6", command=lambda: field_txt(6), width=5)
C6.grid(row=3, column=3)
C7 = Button(win, text="7", command=lambda: field_txt(7), width=5)
C7.grid(row=4, column=1)
C8 = Button(win, text="8", command=lambda: field_txt(8), width=5)
C8.grid(row=4, column=2)
C9 = Button(win, text="9", command=lambda: field_txt(9), width=5)
C9.grid(row=4, column=3)
C0 = Button(win, text="0", command=lambda: field_txt(0), width=5)
C0.grid(row=5, column=2)
Ca = Button(win, text="+", command=lambda: field_txt('+'), width=5)
Ca.grid(row=2, column=4)
Cs = Button(win, text="-", command=lambda: field_txt('-'), width=5)
Cs.grid(row=3, column=4)
Cm = Button(win, text="*", command=lambda: field_txt('*'), width=5)  # Fixed the empty text
Cm.grid(row=4, column=4)
Cd = Button(win, text="/", command=lambda: field_txt('/'), width=5)
Cd.grid(row=5, column=4)
Cdec = Button(win, text=".", command=lambda: field_txt('.'), width=5)
Cdec.grid(row=6, column=1)
Cbr1 = Button(win, text="(", command=lambda: field_txt('('), width=5)
Cbr1.grid(row=6, column=2)
Cbr2 = Button(win, text=")", command=lambda: field_txt(')'), width=5)
Cbr2.grid(row=6, column=3)
Croot = Button(win, text="pow", command=lambda: field_txt('**'), width=5)
Croot.grid(row=6, column=4)

Ccl = Button(win, text="clear", width=5, command=clear)
Ccl.grid(row=5, column=1)
Ceq = Button(win, text="=", width=5, command=calculate)
Ceq.grid(row=5, column=3)

win.mainloop()
