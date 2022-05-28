from tkinter import *

root = Tk()
root.title("LAC GuI")
root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

lb1 = Label(root, text="안녕하세요") # Label
lb1.pack()

photo = PhotoImage(file="GUI/img.png")
lb2 = Label(root, image=photo)  # Label 속성 image : 이미지
lb2.pack()

def change():
    lb1.config(text="또 만나요")

    global photo2 # 함수 내부 선언된 변수이기 때문에 전역화를 안하면 가비지가 삭제해버림
    photo2 = PhotoImage(file="GUI/img2.png")
    lb2.config(image=photo2)

# Label 인스턴스에 대해 config() 안에 수정할 속성 대입

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()