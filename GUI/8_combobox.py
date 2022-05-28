import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("LAC GuI")
root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
# 읽기전용. 선택 창 변경 불가
combobox.current(1) # 1번째 선택 지정
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 및 버튼 클릭을 통한 값 설정

def btncmd():
    print(combobox.get())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()