from tkinter import *

root = Tk()
root.title("LAC GuI")
root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요") # 미리보기 설정

e = Entry(root, width=30) # Entry에서는 엔터 불가(한 줄)
e.pack()
e.insert(0, "한 줄만 입력")

def btncmd():
    print(txt.get("1.0", END)) # 라인 1 0번째 column 위치부터 끝까지
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()