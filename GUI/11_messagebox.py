import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("LAC GuI")
root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

def info():
    msgbox.showinfo("알림", "예매 정상 완료")

def warn():
    msgbox.showwarning("경고", "해당 좌석 이미 매진")

def err():
    msgbox.showerror("에러", "결재 오류 발생")

def okcancel():
    msgbox.askokcancel("확인/취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    msgbox.askretrycancel("확인/취소", "일시적 오류 발생. 다시 시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장하시겠습니까?")
    print(response)
    if response == True:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=err, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예/아니오").pack()
Button(root, command=yesnocancel, text="예/아니오/취소").pack()


root.mainloop()