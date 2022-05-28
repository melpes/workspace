from tkinter import *

def check():
    print(value1)
    print(value1.get())

ROOT = Tk()

value1 = IntVar()

Checkbutton(ROOT, text="abracadabra", variable=value1,command=check).pack()

ROOT.mainloop()