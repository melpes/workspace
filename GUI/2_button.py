from tkinter import *

root = Tk()
root.title("LAC GuI")
root.geometry("640x480+100+200") # 가로 x 세로 + x좌표 + y좌표

button1 = Button(root, text="버튼1") # Button(위치, text="텍스트")
button1.pack() # 버튼 호출. 실제 반영

button2 = Button(root, padx=5, pady=10, text="버튼2")
button2.pack()
button3 = Button(root, padx=10, pady=5, text="버튼3")
button3.pack()
button4 = Button(root, width=10, height=3, text="버튼4")
button4.pack()

# 버튼 속성 : [padx, pady] 여백, [width, height] 크기

button5 = Button(root, fg="red", bg="yellow", text="버튼5")
button5.pack()

# fg : 글자 색상, bg : 배경 색상

photo = PhotoImage(file="GUI/img.png")
button6 = Button(root, image=photo)
button6.pack()

# PhotoImage로 이미지 불러오기, image 속성으로 이미지 설정 가능

def btncmd():
    print("클릭됨")

button7 = Button(root, text="동작", command=btncmd)
button7.pack()

# command : 버튼 클릭(떼는 시점) 시 함수 동작



root.mainloop()