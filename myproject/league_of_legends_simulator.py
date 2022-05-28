# 스텟 = 본체 스탯(레벨) + 아이템, 룬 스텟, 스킬 스텟
# 캐릭터별 평타와 스킬 강화 정도, 골드 대비 성장률

# 선택 항목 : 챔프, 레벨, 스킬 레벨, 아이템, 룬, 기타 스택형 패시브 스택수
# 강화 전 항목, 강화 후 항목, 공격 대상 항목

import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Item efficiency")
root.geometry("720x720+2000+100") # 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 값 변경 여부

##############################################

class champion:
    basic_ad = 0
    growing_ad:0
    basic_hp:0
    growing_hp:0
    basic_as:0
    growing_as:0
    basic_def:0
    growing_def:0
    basic_mdef:0
    growing_mdef:0

zed = champion()
zed.basic_ad = 63
zed.growing_ad = 3.4
zed.basic_hp = 584
zed.growing_hp = 85
zed.basic_as = 0.651
zed.growing_as = 0.033
zed.basic_def = 32
zed.growing_def = 3.5
zed.basic_mdef = 32
zed.growing_mdef = 1.25

##############################################

class item:
    ad = 0
    ap = 0
    hp = 0
    defe = 0
    mdef = 0
    attack_speed = 0
    cd = 0
    bs = 0
    ombs = 0
    cr = 0
    crd = 0
    ad_pier = 0
    ad_pierP = 0
    ap_pier = 0
    ap_pierP = 0

    gold = 0

long_sword = item()
long_sword.ad = 10
long_sword.gold = 350

##############################################

champion_level = 1

skill_level = {
    'q':0,
    'w':0,
    'e':0,
    'r':0
}

