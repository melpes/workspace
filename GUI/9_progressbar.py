import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("LAC GuI")
root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# determinate : 채워가며 진행
# indeterminate : 바 왕복
# progressbar.start(10) # 속도 대입
# progressbar.pack()

# def btncmd():
#     progressbar.stop()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd():
    for i in range(100):
        time.sleep(0.01)
        p_var2.set(i) # 값 설정
        progressbar2.update() # 업데이트
        print(p_var2.get())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()