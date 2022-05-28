from sys import exec_prefix
from tkinter import *

root = Tk()
root.title("How To Fight Well!")
root.geometry("700x480+2000+100") # 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 값 변경 여부

def search():
    keyword = search_etr.get()
    possiblity = []

    empty = [pos for pos, char in enumerate(keyword) if char == " "]
    if len(empty) == 1:
        title = keyword.replace(" ", "=")
        with open("myproject/how_to_fight/" + title + ".txt", "r", encoding="utf8") as file:
            txtbx.insert(1.0, file.read())
    elif len(empty) >= 2:
        a = keyword.split(" ")
        for i in range(len(a)):
            possiblity.append("")
            for j in range(len(a)):
                possiblity[i] += a[j] + " " if i != j else a[j] + "="
            possiblity[i] = possiblity[i][:-1]
        for i in range(len(a)):
            try:
                with open("myproject/how_to_fight/" + possiblity[i] + ".txt", "r", encoding="utf8") as file:
                    txtbx.insert(1.0, file.read())
                break
            except:
                continue

##############################################

top_frm = Frame(root, pady=30)
top_frm.pack(side="top")

search_etr = Entry(top_frm, width=30)
search_etr.pack(side="left")

bt = Button(top_frm, text="검색", command=search)
bt.pack(side="right")

txtbx_frm = Frame(root)
txtbx_frm.pack(side="bottom", fill="both", padx=20, pady=20)

scbar = Scrollbar(txtbx_frm)
scbar.pack(side="right", fill="y")

txtbx = Text(txtbx_frm, yscrollcommand=scbar.set)
txtbx.pack(side="left", fill="both")

scbar.config(command=txtbx.yview)

root.mainloop()