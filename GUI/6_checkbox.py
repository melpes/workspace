from tkinter import *

root = Tk()
root.title("LAC GuI")
root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표


chkvar = IntVar() # chkvar에 인트형으로 값을 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# 체크 여부 variable에 할당된 변수에 저장
chkbox.select() # 시작시 체크되어있음
chkbox.deselect() # 시작시 해제되어있음
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())
    print(chkvar2.get())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()