from tkinter import *

root = Tk()
root.title("LAC GuI")
root.geometry("640x480+100+200") # 가로 x 세로 + x좌표 + y좌표

frm = Frame(root)
frm.pack()

scbar = Scrollbar(frm)
scbar.pack(side="right", fill="y")

lstbox = Listbox(frm, selectmode="extended", height=10, yscrollcommand=scbar.set)
for i in range(1, 32):
    lstbox.insert(END, str(i) + " 일")
lstbox.pack()

scbar.config(command=lstbox.yview)

root.mainloop()