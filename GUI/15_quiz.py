import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

frm = Frame(root)
frm.pack(fill="both", expand=True)

scbar = Scrollbar(frm)
scbar.pack(side="right", fill="y")

txt = Text(frm, yscrollcommand=scbar.set)
txt.pack(side="left", fill="both", expand=True)

scbar.config(command=txt.yview)

def open_new_file():
    if os.path.isfile("GUI/mynote.txt") == False:
        print("파일 없음")
        return
    with open("GUI/mynote.txt", "r", encoding="utf8") as note:
        txt.delete("1.0", END)
        txt.insert(END, note.read())

def save_file():
    with open("GUI/mynote.txt", "w", encoding="utf8") as note:
        note.write(txt.get("1.0", END))

def exit_programe():
    root.quit()

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_new_file)

menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=exit_programe)

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)
root.mainloop()