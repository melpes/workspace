from os import stat
from tkinter import *
from tkinter.ttk import Progressbar
from typing import Sized

class Stat_btn:
    def __init__(self, number, G_per_stat, name, nm_kr):
        self.btn = Button(topfrm, width=5, height=2)
        self.btn.grid(row=0, column=number, padx=5, pady=5, ipady=5)
        self.lb = Label(topfrm, text=f"{G_per_stat}G/{name}")
        self.nm = Label(topfrm, text=nm_kr)
        self.lb.grid(row=1, column=number, padx=5, pady=2, ipadx=3)
        self.nm.grid(row=2, column=number, padx=5, pady=2, ipadx=3)

root = Tk()
root.title("League of Legends Item Efficiency")
root.geometry("600x480+600+200") # 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 값 변경 여부

###########################################

topfrm = LabelFrame(root, text="기준 아이템")
topfrm.pack(side="top", fill="x", padx=10, pady=5, ipady=5)

ad = Stat_btn(0, 35, "ad", "공격력")
ap = Stat_btn(1, 21.75, "ap", "주문력")
deff = Stat_btn(2, 20, "def", "방어력")
magic_resis = Stat_btn(3, 25, "mr", "마법저항력")
hp = Stat_btn(4, 2.67, "hp", "체력")
mp = Stat_btn(5, 1.4, "mp", "마나")
# 공간 없으니 안 바뀌는 절대스탯이랑 몇개는 기타 설정에서 확인할 수 있게 하고 
# 물관같이 이상한 놈들만 기재하는걸로

###########################################

mdlfrm = Frame(root)
mdlfrm.pack(side="top", fill="x")

leftfrm = LabelFrame(mdlfrm, text="스탯")
leftfrm.pack(side="left", fill="y", padx=10)

lftlstbx = Listbox(leftfrm)
lftlstbx.pack(side="top", padx=10, pady=10)

rightfrm = LabelFrame(mdlfrm, text="골드 가치")
rightfrm.pack(side="right", fill="y", padx=10)

rtlstbx = Listbox(rightfrm)
rtlstbx.pack(side="top", padx=10, pady=10)

item_btn = Button(mdlfrm, width=9, height=4)
item_btn.pack(side="top", pady=10)

item_lb = Label(mdlfrm, text="???".center(15), background="#ffffff", relief="solid", bd=1)
item_lb.pack(side="top")

###########################################

bottomfrm = Frame(root)
bottomfrm.pack(side="top", fill="both", padx=10, pady=10)

# bottomleftfrm = Frame(bottomfrm)
# bottomleftfrm.pack(side="left")

txt = Text(bottomfrm, width=58, height=5)
txt.pack(side="left")

final_frm = Frame(bottomfrm)
final_frm.pack(side="right", expand=True)
final_lb1 = Label(final_frm, text="추가능력 가격")
final_lb2 = Label(final_frm, text="[500]")
final_lb1.pack(side="top")
final_lb2.pack(side="top")


lftlstbx.insert(0, " 공격력 30")
lftlstbx.insert(1, " 물관 10")

rtlstbx.insert(0, " 1050")
rtlstbx.insert(1, " ??")
for i in range(2, 9):
    rtlstbx.insert(i, "")
rtlstbx.insert(9, " 스탯 총 가치 :1100")

root.mainloop()