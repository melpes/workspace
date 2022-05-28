from tkinter import *

root = Tk()
root.title("LAC GuI")
root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

def create_new_file():
    print("새 파일 생성")

menu = Menu(root)

menu_file = Menu(menu, tearoff=8)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
# 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)

menu.add_cascade(label="Edit")

menu_lang = Menu(menu, tearoff=8)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Jave")
menu_lang.add_radiobutton(label="C#")
menu.add_cascade(label="Language", menu= menu_lang)

menu_view = Menu(menu,tearoff=8)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()