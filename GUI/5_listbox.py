from tkinter import *

root = Tk()
root.title("LAC GuI")
root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

lstbox = Listbox(root, selectmode="extended", height=0) 
# single : 하나만 선택, extended : 복수선택가능
# heigt = 0 이면 리스트 크기만큼 적용
# 0, 1, 2 번 자리 혹은 맨 뒤에 삽입
lstbox.insert(0, "사과")
lstbox.insert(1, "딸기")
lstbox.insert(2, "수박")
lstbox.insert(END, "바나나")
lstbox.insert(END, "포도")
lstbox.pack()

def btncmd():
    # lstbox.delete(END)
    print("총", lstbox.size(), "개")
    # print(lstbox.get(0, 2))
    print("선택된 항목 :", lstbox.curselection()) # 인덱스로 반환


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()