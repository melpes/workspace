import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
from PIL import Image, ImageTk
from selenium import webdriver

root = Tk()
root.title("Item efficiency")
root.geometry("720x720+2000+100") # 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 값 변경 여부

##############################################

stat_data = {"전투 지속 시간":10, "공격력 / 주문력":0, "방어력 / 마법 저항력":0, "체력":0, "마나":0, \
    "공격 속도(%)":0, "스킬 가속":0, "물리 관통력 / 마법 관통력":0,\
    "방어구 관통력 / 마법 관통력(%)":0, "치명타 확률(%)":0, "생명력 흡수(%)":0,\
    "모든 피해 흡혈(%)":0, "회복 및 보호막 효과(%)":0, "피해 증폭(%)":0, "강인함":0, "둔화 저항":0,\
    "이동 속도":0, "이동 속도(%)":0}
stat_key = list(stat_data.keys())

before_stat = {"전투 지속 시간":10, "공격력 / 주문력":0, "방어력 / 마법 저항력":0, "체력":0, "마나":0, \
    "공격 속도(%)":0, "스킬 가속":0, "물리 관통력 / 마법 관통력":0,\
    "방어구 관통력 / 마법 관통력(%)":0, "치명타 확률(%)":0, "생명력 흡수(%)":0,\
    "모든 피해 흡혈(%)":0, "회복 및 보호막 효과(%)":0, "피해 증폭(%)":0, "강인함":0, "둔화 저항":0,\
    "이동 속도":0, "이동 속도(%)":0}
after_stat = {"전투 지속 시간":10, "공격력 / 주문력":0, "방어력 / 마법 저항력":0, "체력":0, "마나":0, \
    "공격 속도(%)":0, "스킬 가속":0, "물리 관통력 / 마법 관통력":0,\
    "방어구 관통력 / 마법 관통력(%)":0, "치명타 확률(%)":0, "생명력 흡수(%)":0,\
    "모든 피해 흡혈(%)":0, "회복 및 보호막 효과(%)":0, "피해 증폭(%)":0, "강인함":0, "둔화 저항":0,\
    "이동 속도":0, "이동 속도(%)":0}

##############################################

def get_info(combobox, entry):
    stat = combobox.get()
    try:
        value = int(entry.get())
    except ValueError:
        msgbox.showerror("에러", "정수로만 입력해 주십시오")
        return
    except Exception as err:
        msgbox.showerror("알 수 없는 에러", f"에러 코드 : {err}")
        return
    finally:
        entry.delete(0, END)
    return (stat, value)

def left_btn_selected():
    info = get_info(crr_cmbx, left_mn_etr)
    if info == None:
        return
    key, value = info

    before_stat[key] += value

    update()

def right_btn_selected():
    info = get_info(plus_cmbx, middle_mn_etr)
    if info == None:
        return
    key, value = info

    after_stat[key] += value

    update()

def reseting():
    for key in stat_key:
        before_stat[key] = 0
        after_stat[key] = 0
        stat_data[key] = 0

    update()

def basic_stat_select():
    global before_stat

    for key, value in stat_data.items():
        before_stat[key] = value
    
    stat_update()
    update()

def plus_stat_select():
    global after_stat

    for key, value in stat_data.items():
       after_stat[key] = value
    
    stat_update()
    update()

##############################################

def update():
    write_on_lstbx(before_stat, crrstat_lstbx)
    write_on_lstbx(after_stat, plusstat_lstbx)
    calculate()

def write_on_lstbx(diction, listbox):
    listbox.delete(0, END)

    for key, value in diction.items():
        if value == 0:
            continue
        else:
            index = stat_key.index(key)
        listbox.insert(index, f"[{key}] : {value}")

def calculate():
    before_hp_by_lifesteal = before_stat["전투 지속 시간"] * before_stat["공격력 / 주문력"] *\
         0.625 * (1 + before_stat["공격 속도(%)"] / 100) * before_stat["생명력 흡수(%)"] / 100
    after_hp_by_lifesteal = after_stat["전투 지속 시간"] * after_stat["공격력 / 주문력"] *\
         0.625 * (1 + after_stat["공격 속도(%)"] / 100) * after_stat["생명력 흡수(%)"] / 100

    before_hp_by_omnilifesteal = before_stat["전투 지속 시간"] * before_stat["공격력 / 주문력"] *\
         0.625 * (1 + before_stat["공격 속도(%)"] / 100) * before_stat["모든 피해 흡혈(%)"] / 100
    after_hp_by_omnilifesteal = after_stat["전투 지속 시간"] * after_stat["공격력 / 주문력"] *\
         0.625 * (1 + after_stat["공격 속도(%)"] / 100) * after_stat["모든 피해 흡혈(%)"] / 100
    
    try:
        basic_attack_dps = after_stat["공격력 / 주문력"] / before_stat["공격력 / 주문력"] *\
            (after_stat["공격 속도(%)"] + 100) / (before_stat["공격 속도(%)"] + 100) *\
            (100 + 0.75 * after_stat["치명타 확률(%)"]) / (100 + 0.75 * before_stat["치명타 확률(%)"]) \
            * 100 - 100
    except ZeroDivisionError:
        basic_attack_dps = (after_stat["공격 속도(%)"] + 100) / (before_stat["공격 속도(%)"] + 100) *\
            (100 + 0.75 * after_stat["치명타 확률(%)"]) / (100 + 0.75 * before_stat["치명타 확률(%)"]) \
            * 100 - 100
    effstat_lstbx.delete(1)
    effstat_lstbx.insert(1, f"기본 공격 평균 데미지 증가량 : {round(basic_attack_dps)}%")

    try:
        basic_tanking = (after_stat["방어력 / 마법 저항력"] + 100) / (before_stat["방어력 / 마법 저항력"] + 100) *\
            (after_stat["체력"] + after_hp_by_lifesteal + after_hp_by_omnilifesteal)\
            / (before_stat["체력"] + before_hp_by_lifesteal + before_hp_by_omnilifesteal) * 100 - 100
    except ZeroDivisionError:
        basic_tanking = (after_stat["방어력 / 마법 저항력"] + 100) / (before_stat["방어력 / 마법 저항력"] + 100) * 100 - 100
    effstat_lstbx.delete(0)
    effstat_lstbx.insert(0, f"생존 시간 증가량 : {round(basic_tanking)}%")

##############################################

# frame
if True:
    ##############################################

    left_frm = Frame(root)
    right_frm = Frame(root)
    top_frm = Frame(root)
    bottom_frm = Frame(root)

    top_frm.pack(side="top", fill="x", padx=20, pady=20)
    bottom_frm.pack(side="bottom", fill="x", padx=20, pady=20)
    left_frm.pack(side="left", fill="y", padx=20)
    right_frm.pack(side="right", fill="y", padx=20)

    reset = Button(root, text="초기화", command=reseting)
    reset.pack()

    ##############################################

    left_selecting_frm = Frame(left_frm)
    left_selecting_frm.pack(side="bottom")

    left_two_bts_frm = Frame(left_selecting_frm)
    left_two_bts_frm.pack(side="bottom")

    left_btn = Button(left_two_bts_frm, text="선택", command=left_btn_selected)
    left_btn.pack(side="left")
    basic_btn = Button(left_two_bts_frm, text="초기 상태 지정", command=basic_stat_select)
    basic_btn.pack(side="right")

    left_cmbx_frm = Frame(left_selecting_frm)
    left_cmbx_frm.pack(side="bottom")

    left_scrbar_frm = Frame(left_frm)
    left_scrbar_frm.pack(side="bottom", fill="x")

    left_scbar = Scrollbar(left_scrbar_frm)
    left_scbar.pack(side="right", fill="y")

    crrstat_lstbx = Listbox(left_scrbar_frm, yscrollcommand=left_scbar.set)
    crrstat_lstbx.pack(side="left", fill="both", expand=True)

    left_scbar.config(command=crrstat_lstbx.yview)

    crr_cmbx = ttk.Combobox(left_cmbx_frm, values=stat_key, width=25, state="readonly")
    crr_cmbx.set("공격력 / 주문력")
    crr_cmbx.pack(side="left")

    left_mn_etr = Entry(left_cmbx_frm, width=4)
    left_mn_etr.pack(side="right")

    ##############################################

    right_selecting_frm = Frame(right_frm)
    right_selecting_frm.pack(side="bottom")

    right_two_bts_frm = Frame(right_selecting_frm)
    right_two_bts_frm.pack(side="bottom")

    middle_btn = Button(right_two_bts_frm, text="선택", command=right_btn_selected)
    middle_btn.pack(side="left")
    plus_btn = Button(right_two_bts_frm, text="나중 상태 지정", command=plus_stat_select)
    plus_btn.pack(side="right")


    middle_cmbx_frm = Frame(right_selecting_frm)
    middle_cmbx_frm.pack(side="bottom")

    right_scrbar_frm = Frame(right_frm)
    right_scrbar_frm.pack(side="bottom", fill="x")

    right_scbar = Scrollbar(right_scrbar_frm)
    right_scbar.pack(side="right", fill="y")

    plusstat_lstbx = Listbox(right_scrbar_frm, yscrollcommand=right_scbar.set)
    plusstat_lstbx.pack(side="left", fill="both", expand=True)

    right_scbar.config(command=plusstat_lstbx.yview)

    plus_cmbx = ttk.Combobox(middle_cmbx_frm, values=stat_key, width=25, state="readonly")
    plus_cmbx.set("공격력 / 주문력")
    plus_cmbx.pack(side="left")

    middle_mn_etr = Entry(middle_cmbx_frm, width=4)
    middle_mn_etr.pack(side="right")

    ##############################################

    effstat_lstbx = Listbox(top_frm)
    effstat_lstbx.pack(fill="x")

    effstat_lstbx.insert(0, "생존 시간 증가량 : 0%")
    effstat_lstbx.insert(1, "기본 공격 평균 데미지 증가량 : 0%")
    effstat_lstbx.insert(2, "스킬 기반 평균 데미지 증가량 : 0%")

    ##############################################
    # bottom frame
    # lune frame

    rune_frm = LabelFrame(bottom_frm, text="룬", pady=10)
    rune_frm.pack(side="left")

    runetype_frm = Frame(rune_frm, padx=10)
    runetype_frm.grid(row=0, column=0)

##############################################
# images
def image_resize(size, link):
    image = Image.open(link)
    image = image.resize(size, Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    return image

if True:
    # main rune

    basic_image = PhotoImage(file="gui_project/item_simulation/approach_velocity.png")

    precision = image_resize((20, 20), "gui_project/item_simulation/precision.png")
    domination = image_resize((20, 20), "gui_project/item_simulation/domination.png")
    sorcery = image_resize((20, 20), "gui_project/item_simulation/sorcery.png")
    resolve = image_resize((20, 20), "gui_project/item_simulation/resolve.png")
    inspiration = image_resize((20, 20), "gui_project/item_simulation/inspiration.png")
    
    ##############################################
    # precision

    press_the_attack = image_resize((20, 20), "gui_project/item_simulation/press_the_attack.png")
    lethal_tempo = image_resize((20, 20), "gui_project/item_simulation/lethal_tempo.png")
    fleet_footwork = image_resize((20, 20), "gui_project/item_simulation/fleet_footwork.png")
    conqueror = image_resize((20, 20), "gui_project/item_simulation/conqueror.png")

    overheal = image_resize((20, 20), "gui_project/item_simulation/overheal.png")
    triumph = image_resize((20, 20), "gui_project/item_simulation/triumph.png")
    presence_of_mind = image_resize((20, 20), "gui_project/item_simulation/presence_of_mind.png")

    legend_alacrity = image_resize((20, 20), "gui_project/item_simulation/legend_alacrity.png")
    legend_tenacity = image_resize((20, 20), "gui_project/item_simulation/legend_tenacity.png")
    legend_bloodline = image_resize((20, 20), "gui_project/item_simulation/legend_bloodline.png")

    coup_de_grace = image_resize((20, 20), "gui_project/item_simulation/coup_de_grace.png")
    cut_down = image_resize((20, 20), "gui_project/item_simulation/cut_down.png")
    last_stand = image_resize((20, 20), "gui_project/item_simulation/last_stand.png")

    press_the_attack3 = image_resize((30, 30), "gui_project/item_simulation/press_the_attack.png")
    lethal_tempo3 = image_resize((30, 30), "gui_project/item_simulation/lethal_tempo.png")
    fleet_footwork3 = image_resize((30, 30), "gui_project/item_simulation/fleet_footwork.png")
    conqueror3 = image_resize((30, 30), "gui_project/item_simulation/conqueror.png")

    overheal3 = image_resize((30, 30), "gui_project/item_simulation/overheal.png")
    triumph3 = image_resize((30, 30), "gui_project/item_simulation/triumph.png")
    presence_of_mind3 = image_resize((30, 30), "gui_project/item_simulation/presence_of_mind.png")

    legend_alacrity3 = image_resize((30, 30), "gui_project/item_simulation/legend_alacrity.png")
    legend_tenacity3 = image_resize((30, 30), "gui_project/item_simulation/legend_tenacity.png")
    legend_bloodline3 = image_resize((30, 30), "gui_project/item_simulation/legend_bloodline.png")

    coup_de_grace3 = image_resize((30, 30), "gui_project/item_simulation/coup_de_grace.png")
    cut_down3 = image_resize((30, 30), "gui_project/item_simulation/cut_down.png")
    last_stand3 = image_resize((30, 30), "gui_project/item_simulation/last_stand.png")

    ##############################################
    # domination

    electrocute = image_resize((20, 20), "gui_project/item_simulation/electrocute.png")
    dark_harvest = image_resize((20, 20), "gui_project/item_simulation/dark_harvest.png")
    predator = image_resize((20, 20), "gui_project/item_simulation/predator.png")
    hail_of_blades = image_resize((20, 20), "gui_project/item_simulation/hail_of_blades.png")

    cheap_shot = image_resize((20, 20), "gui_project/item_simulation/cheap_shot.png")
    taste_of_blood = image_resize((20, 20), "gui_project/item_simulation/taste_of_blood.png")
    sudden_impact = image_resize((20, 20), "gui_project/item_simulation/sudden_impact.png")

    zombie_ward = image_resize((20, 20), "gui_project/item_simulation/zombie_ward.png")
    ghost_poro = image_resize((20, 20), "gui_project/item_simulation/ghost_poro.png")
    eyeball_collection = image_resize((20, 20), "gui_project/item_simulation/eyeball_collection.png")

    ravenous_hunter = image_resize((20, 20), "gui_project/item_simulation/ravenous_hunter.png")
    relentless_hunter = image_resize((20, 20), "gui_project/item_simulation/relentless_hunter.png")
    ingenious_hunter = image_resize((20, 20), "gui_project/item_simulation/ingenious_hunter.png")
    ultimate_hunter = image_resize((20, 20), "gui_project/item_simulation/ultimate_hunter.png")

    electrocute3 = image_resize((30, 30), "gui_project/item_simulation/electrocute.png")
    dark_harvest3 = image_resize((30, 30), "gui_project/item_simulation/dark_harvest.png")
    predator3 = image_resize((30, 30), "gui_project/item_simulation/predator.png")
    hail_of_blades3 = image_resize((30, 30), "gui_project/item_simulation/hail_of_blades.png")

    cheap_shot3 = image_resize((30, 30), "gui_project/item_simulation/cheap_shot.png")
    taste_of_blood3 = image_resize((30, 30), "gui_project/item_simulation/taste_of_blood.png")
    sudden_impact3 = image_resize((30, 30), "gui_project/item_simulation/sudden_impact.png")

    zombie_ward3 = image_resize((30, 30), "gui_project/item_simulation/zombie_ward.png")
    ghost_poro3 = image_resize((30, 30), "gui_project/item_simulation/ghost_poro.png")
    eyeball_collection3 = image_resize((30, 30), "gui_project/item_simulation/eyeball_collection.png")

    ravenous_hunter3 = image_resize((30, 30), "gui_project/item_simulation/ravenous_hunter.png")
    relentless_hunter3 = image_resize((30, 30), "gui_project/item_simulation/relentless_hunter.png")
    ingenious_hunter3 = image_resize((30, 30), "gui_project/item_simulation/ingenious_hunter.png")
    ultimate_hunter3 = image_resize((30, 30), "gui_project/item_simulation/ultimate_hunter.png")

    ##############################################
    # sorcery

    summon_aery = image_resize((20, 20), "gui_project/item_simulation/summon_aery.png")
    arcane_comet = image_resize((20, 20), "gui_project/item_simulation/arcane_comet.png")
    phase_rush = image_resize((20, 20), "gui_project/item_simulation/phase_rush.png")

    nullifying_orb = image_resize((20, 20), "gui_project/item_simulation/nullifying_orb.png")
    manaflow_band = image_resize((20, 20), "gui_project/item_simulation/manaflow_band.png")
    nimbus_cloak = image_resize((20, 20), "gui_project/item_simulation/nimbus_cloak.png")

    transcendence = image_resize((20, 20), "gui_project/item_simulation/transcendence.png")
    celerity = image_resize((20, 20), "gui_project/item_simulation/celerity.png")
    absolute_focus = image_resize((20, 20), "gui_project/item_simulation/absolute_focus.png")

    scorch = image_resize((20, 20), "gui_project/item_simulation/scorch.png")
    waterwalking = image_resize((20, 20), "gui_project/item_simulation/waterwalking.png")
    gathering_storm = image_resize((20, 20), "gui_project/item_simulation/gathering_storm.png")

    summon_aery3 = image_resize((30, 30), "gui_project/item_simulation/summon_aery.png")
    arcane_comet3 = image_resize((30, 30), "gui_project/item_simulation/arcane_comet.png")
    phase_rush3 = image_resize((30, 30), "gui_project/item_simulation/phase_rush.png")

    nullifying_orb3 = image_resize((30, 30), "gui_project/item_simulation/nullifying_orb.png")
    manaflow_band3 = image_resize((30, 30), "gui_project/item_simulation/manaflow_band.png")
    nimbus_cloak3 = image_resize((30, 30), "gui_project/item_simulation/nimbus_cloak.png")

    transcendence3 = image_resize((30, 30), "gui_project/item_simulation/transcendence.png")
    celerity3 = image_resize((30, 30), "gui_project/item_simulation/celerity.png")
    absolute_focus3 = image_resize((30, 30), "gui_project/item_simulation/absolute_focus.png")

    scorch3 = image_resize((30, 30), "gui_project/item_simulation/scorch.png")
    waterwalking3 = image_resize((30, 30), "gui_project/item_simulation/waterwalking.png")
    gathering_storm3 = image_resize((30, 30), "gui_project/item_simulation/gathering_storm.png")

    ##############################################
    # resolve

    grasp_of_the_undying = image_resize((20, 20), "gui_project/item_simulation/grasp_of_the_undying.png")
    aftershock = image_resize((20, 20), "gui_project/item_simulation/aftershock.png")
    guardian = image_resize((20, 20), "gui_project/item_simulation/guardian.png")

    demolish = image_resize((20, 20), "gui_project/item_simulation/demolish.png")
    font_of_life = image_resize((20, 20), "gui_project/item_simulation/font_of_life.png")
    shield_bash = image_resize((20, 20), "gui_project/item_simulation/shield_bash.png")

    conditioning = image_resize((20, 20), "gui_project/item_simulation/conditioning.png")
    second_wind = image_resize((20, 20), "gui_project/item_simulation/second_wind.png")
    bond_plating = image_resize((20, 20), "gui_project/item_simulation/bond_plating.png")

    overgrowth = image_resize((20, 20), "gui_project/item_simulation/overgrowth.png")
    revitalize = image_resize((20, 20), "gui_project/item_simulation/revitalize.png")
    unflinching = image_resize((20, 20), "gui_project/item_simulation/unflinching.png")

    grasp_of_the_undying3 = image_resize((30, 30), "gui_project/item_simulation/grasp_of_the_undying.png")
    aftershock3 = image_resize((30, 30), "gui_project/item_simulation/aftershock.png")
    guardian3 = image_resize((30, 30), "gui_project/item_simulation/guardian.png")

    demolish3 = image_resize((30, 30), "gui_project/item_simulation/demolish.png")
    font_of_life3 = image_resize((30, 30), "gui_project/item_simulation/font_of_life.png")
    shield_bash3 = image_resize((30, 30), "gui_project/item_simulation/shield_bash.png")

    conditioning3 = image_resize((30, 30), "gui_project/item_simulation/conditioning.png")
    second_wind3 = image_resize((30, 30), "gui_project/item_simulation/second_wind.png")
    bond_plating3 = image_resize((30, 30), "gui_project/item_simulation/bond_plating.png")

    overgrowth3 = image_resize((30, 30), "gui_project/item_simulation/overgrowth.png")
    revitalize3 = image_resize((30, 30), "gui_project/item_simulation/revitalize.png")
    unflinching3 = image_resize((30, 30), "gui_project/item_simulation/unflinching.png")

    ##############################################
    # inspiration

    glacial_augment = image_resize((20, 20), "gui_project/item_simulation/glacial_augment.png")
    unsealed_spellbook = image_resize((20, 20), "gui_project/item_simulation/unsealed_spellbook.png")
    prototype_omnistone = image_resize((20, 20), "gui_project/item_simulation/prototype_omnistone.png")

    hextech_flashtraption = image_resize((20, 20), "gui_project/item_simulation/hextech_flashtraption.png")
    magical_footwear = image_resize((20, 20), "gui_project/item_simulation/magical_footwear.png")
    perfect_timing = image_resize((20, 20), "gui_project/item_simulation/perfect_timing.png")

    future_market = image_resize((20, 20), "gui_project/item_simulation/future's_market.png")
    minion_dematerializer = image_resize((20, 20), "gui_project/item_simulation/minion_dematerializer.png")
    biscuit_delivery = image_resize((20, 20), "gui_project/item_simulation/biscuit_delivery.png")

    cosmic_insight = image_resize((20, 20), "gui_project/item_simulation/cosmic_insight.png")
    approach_velocity = image_resize((20, 20), "gui_project/item_simulation/approach_velocity.png")
    time_warp_tonic = image_resize((20, 20), "gui_project/item_simulation/time_warp_tonic.png")

    glacial_augment3 = image_resize((30, 30), "gui_project/item_simulation/glacial_augment.png")
    unsealed_spellbook3 = image_resize((30, 30), "gui_project/item_simulation/unsealed_spellbook.png")
    prototype_omnistone3 = image_resize((30, 30), "gui_project/item_simulation/prototype_omnistone.png")

    hextech_flashtraption3 = image_resize((30, 30), "gui_project/item_simulation/hextech_flashtraption.png")
    magical_footwear3 = image_resize((30, 30), "gui_project/item_simulation/magical_footwear.png")
    perfect_timing3 = image_resize((30, 30), "gui_project/item_simulation/perfect_timing.png")

    future_market3 = image_resize((30, 30), "gui_project/item_simulation/future's_market.png")
    minion_dematerializer3 = image_resize((30, 30), "gui_project/item_simulation/minion_dematerializer.png")
    biscuit_delivery3 = image_resize((30, 30), "gui_project/item_simulation/biscuit_delivery.png")

    cosmic_insight3 = image_resize((30, 30), "gui_project/item_simulation/cosmic_insight.png")
    approach_velocity3 = image_resize((30, 30), "gui_project/item_simulation/approach_velocity.png")
    time_warp_tonic3 = image_resize((30, 30), "gui_project/item_simulation/time_warp_tonic.png")

    ##############################################

    upside = image_resize((20, 20), "gui_project/item_simulation/upside.png")
    downside = image_resize((20, 20), "gui_project/item_simulation/downside.jpg")

##############################################

main_rune_type = None
sub_rune_type = None

level = 1
q_level = 1
w_level = 1
e_level = 1
r_level = 1
current_champion = None
is_long_range = False
is_selected = {"00":False,"01":False,"02":False,"03":False}

def stat_update(rune_code = None):
    global stat_data
    global is_selected
    global is_long_range

    if current_champion == "zedd":
        is_long_range = False

        for key in stat_key:
            stat_data[key] = 0

        stat_data["전투 지속 시간"] = 10
        stat_data["체력"] = 584 + 85 * (level - 1)
        stat_data["공격력 / 주문력"] = 63 + 3.4 * (level - 1)
        stat_data["공격 속도(%)"] = 3.3 * (level - 1)
        stat_data["방어력 / 마법 저항력"] = 32 + (3.5 + 1.25) / 2 * (level - 1)
        stat_data["이동 속도"] = 345

    # browser = webdriver.Chrome() # 괄호 속엔 위치
    # print(current_champion + ":")
    # browser.get(f"https://namu.wiki/w/{current_champion}")
    # try:
    #     browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/article/div[3]/div[2]\
    #     /div/div/div[11]/div[2]/table/tbody/tr[2]/td[2]/div/span").text
    # except:
    #     browser.get(f"https://namu.wiki/w/{current_champion}(리그%20오브%20레전드)")

    # hp = browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/article/div[3]/div[2]\
    #     /div/div/div[11]/div[2]/table/tbody/tr[2]/td[2]/div/span").text
    # ad = browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/article/div[3]/div[2]\
    #     /div/div/div[11]/div[2]/table/tbody/tr[4]/td[2]/div/span").text
    # asspd = browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/article/div[3]/div[2]\
    #     /div/div/div[11]/div[2]/table/tbody/tr[5]/td[2]/div/span").text
    # df = browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/article/div[3]/div[2]\
    #     /div/div/div[11]/div[2]/table/tbody/tr[6]/td[2]/div/span").text
    # md = browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/article/div[3]/div[2]\
    #     /div/div/div[11]/div[2]/table/tbody/tr[7]/td[2]/div/span").text
    # rangest = browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/article/div[3]/div[2]\
    #     /div/div/div[11]/div[2]/table/tbody/tr[8]/td[2]/div/span").text
    # basic_hp = float(hp.split("(")[0])
    # grow_hp = float(hp.split("+")[-1].split(")")[0])

    # basic_ad = float(ad.split("(")[0])
    # grow_ad = float(ad.split("+")[-1].split(")")[0])

    # grow_as = float(asspd.split("+")[-1].split(")")[0])

    # basic_df = float(df.split("(")[0])
    # grow_df = float(df.split("+")[-1].split(")")[0])

    # basic_md = float(md.split("(")[0])
    # grow_md = float(md.split("+")[-1].split(")")[0])

    # range = int(float(rangest))

    # stat_data["전투 지속 시간"] = 10
    # stat_data["체력"] = basic_hp + grow_hp * (level - 1)
    # stat_data["공격력 / 주문력"] = basic_ad + grow_ad * (level - 1)
    # stat_data["공격 속도(%)"] = grow_as * (level - 1)
    # stat_data["방어력 / 마법 저항력"] = basic_df + basic_md + (grow_df + grow_md) / 2 * (level - 1)
    # is_long_range = False if range <= 300 else True


    for key, value in is_selected.items():
        if value:
            if key == "03":
                stat_data["공격력 / 주문력"] += (3 / 17 * (level - 1) + 2) * 12
                stat_data["모든 피해 흡혈(%)"] += 6 if is_long_range else 9

    if rune_code == None:
        return

    if main_rune_type == "precision":
        if rune_code == "03":
            if is_selected[rune_code] == False:
                is_selected[rune_code] = True

                stat_update()

                runepage_03.config(image=conqueror3)                    
            elif is_selected[rune_code] == True:
                is_selected[rune_code] = False

                stat_update()

                runepage_03.config(image=conqueror)
##############################################
# main rune function
def select_precision():
    global main_rune_type
    main_rune_type = "precision"

    runepage_00.config(image=press_the_attack)
    runepage_01.config(image=lethal_tempo)
    runepage_02.config(image=fleet_footwork)
    runepage_03.config(image=conqueror)
    runepage_03.grid(row=0, column=3)

    runepage_10.config(image=overheal)
    runepage_11.config(image=triumph)
    runepage_12.config(image=presence_of_mind)

    runepage_20.config(image=legend_alacrity)
    runepage_21.config(image=legend_tenacity)
    runepage_22.config(image=legend_bloodline)

    runepage_30.config(image=coup_de_grace)
    runepage_31.config(image=cut_down)
    runepage_32.config(image=last_stand)
    runepage_33.grid_forget()

    runepage_precision_sub.grid_forget()
    runepage_domination_sub.grid(row=0, column=1)
    runepage_sorcery_sub.grid(row=0, column=2)
    runepage_resolve_sub.grid(row=0, column=3)
    runepage_inspiration_sub.grid(row=0, column=4)
    
    runepage_40.config(image=basic_image)
    runepage_41.config(image=basic_image)
    runepage_42.config(image=basic_image)

    runepage_50.config(image=basic_image)
    runepage_51.config(image=basic_image)
    runepage_52.config(image=basic_image)

    runepage_60.config(image=basic_image)
    runepage_61.config(image=basic_image)
    runepage_62.config(image=basic_image)
    runepage_63.grid_forget()

def select_domination():
    global main_rune_type
    main_rune_type = "domination"

    runepage_00.config(image=electrocute)
    runepage_01.config(image=dark_harvest)
    runepage_02.config(image=predator)
    runepage_03.config(image=hail_of_blades)
    runepage_03.grid(row=0, column=3)

    runepage_10.config(image=cheap_shot)
    runepage_11.config(image=taste_of_blood)
    runepage_12.config(image=sudden_impact)

    runepage_20.config(image=zombie_ward)
    runepage_21.config(image=ghost_poro)
    runepage_22.config(image=eyeball_collection)

    runepage_30.config(image=ravenous_hunter)
    runepage_31.config(image=relentless_hunter)
    runepage_32.config(image=ingenious_hunter)
    runepage_33.config(image=ultimate_hunter)
    runepage_33.grid(row=0, column=3)

    runepage_precision_sub.grid(row=0, column=0)
    runepage_domination_sub.grid_forget()
    runepage_sorcery_sub.grid(row=0, column=2)
    runepage_resolve_sub.grid(row=0, column=3)
    runepage_inspiration_sub.grid(row=0, column=4)

    runepage_40.config(image=basic_image)
    runepage_41.config(image=basic_image)
    runepage_42.config(image=basic_image)

    runepage_50.config(image=basic_image)
    runepage_51.config(image=basic_image)
    runepage_52.config(image=basic_image)

    runepage_60.config(image=basic_image)
    runepage_61.config(image=basic_image)
    runepage_62.config(image=basic_image)
    runepage_63.grid_forget()

def select_sorcery():
    global main_rune_type
    main_rune_type = "sorcery"
    
    runepage_00.config(image=summon_aery)
    runepage_01.config(image=arcane_comet)
    runepage_02.config(image=phase_rush)
    runepage_03.grid_forget()

    runepage_10.config(image=nullifying_orb)
    runepage_11.config(image=manaflow_band)
    runepage_12.config(image=nimbus_cloak)

    runepage_20.config(image=transcendence)
    runepage_21.config(image=celerity)
    runepage_22.config(image=absolute_focus)

    runepage_30.config(image=scorch)
    runepage_31.config(image=waterwalking)
    runepage_32.config(image=gathering_storm)
    runepage_33.grid_forget()

    runepage_precision_sub.grid(row=0, column=0)
    runepage_domination_sub.grid(row=0, column=1)
    runepage_sorcery_sub.grid_forget()
    runepage_resolve_sub.grid(row=0, column=3)
    runepage_inspiration_sub.grid(row=0, column=4)

    runepage_40.config(image=basic_image)
    runepage_41.config(image=basic_image)
    runepage_42.config(image=basic_image)

    runepage_50.config(image=basic_image)
    runepage_51.config(image=basic_image)
    runepage_52.config(image=basic_image)

    runepage_60.config(image=basic_image)
    runepage_61.config(image=basic_image)
    runepage_62.config(image=basic_image)
    runepage_63.grid_forget()

def select_resolve():
    global main_rune_type
    main_rune_type = "resolve"
    
    runepage_00.config(image=grasp_of_the_undying)
    runepage_01.config(image=aftershock)
    runepage_02.config(image=guardian)
    runepage_03.grid_forget()

    runepage_10.config(image=demolish)
    runepage_11.config(image=font_of_life)
    runepage_12.config(image=shield_bash)

    runepage_20.config(image=conditioning)
    runepage_21.config(image=second_wind)
    runepage_22.config(image=bond_plating)

    runepage_30.config(image=overgrowth)
    runepage_31.config(image=revitalize)
    runepage_32.config(image=unflinching)
    runepage_33.grid_forget()

    runepage_precision_sub.grid(row=0, column=0)
    runepage_domination_sub.grid(row=0, column=1)
    runepage_sorcery_sub.grid(row=0, column=2)
    runepage_resolve_sub.grid_forget()
    runepage_inspiration_sub.grid(row=0, column=4)

    runepage_40.config(image=basic_image)
    runepage_41.config(image=basic_image)
    runepage_42.config(image=basic_image)

    runepage_50.config(image=basic_image)
    runepage_51.config(image=basic_image)
    runepage_52.config(image=basic_image)

    runepage_60.config(image=basic_image)
    runepage_61.config(image=basic_image)
    runepage_62.config(image=basic_image)
    runepage_63.grid_forget()

def select_inspiration():
    global main_rune_type
    main_rune_type = "inspiration"
    
    runepage_00.config(image=glacial_augment)
    runepage_01.config(image=unsealed_spellbook)
    runepage_02.config(image=prototype_omnistone)
    runepage_03.grid_forget()

    runepage_10.config(image=hextech_flashtraption)
    runepage_11.config(image=magical_footwear)
    runepage_12.config(image=perfect_timing)

    runepage_20.config(image=future_market)
    runepage_21.config(image=minion_dematerializer)
    runepage_22.config(image=biscuit_delivery)

    runepage_30.config(image=cosmic_insight)
    runepage_31.config(image=approach_velocity)
    runepage_32.config(image=time_warp_tonic)
    runepage_33.grid_forget()

    runepage_precision_sub.grid(row=0, column=0)
    runepage_domination_sub.grid(row=0, column=1)
    runepage_sorcery_sub.grid(row=0, column=2)
    runepage_resolve_sub.grid(row=0, column=3)
    runepage_inspiration_sub.grid_forget()

    runepage_40.config(image=basic_image)
    runepage_41.config(image=basic_image)
    runepage_42.config(image=basic_image)

    runepage_50.config(image=basic_image)
    runepage_51.config(image=basic_image)
    runepage_52.config(image=basic_image)

    runepage_60.config(image=basic_image)
    runepage_61.config(image=basic_image)
    runepage_62.config(image=basic_image)
    runepage_63.grid_forget()

def select_precision_sub():
    global sub_rune_type
    sub_rune_type = "precision"
    
    runepage_40.config(image=overheal)
    runepage_41.config(image=triumph)
    runepage_42.config(image=presence_of_mind)

    runepage_50.config(image=legend_alacrity)
    runepage_51.config(image=legend_tenacity)
    runepage_52.config(image=legend_bloodline)

    runepage_60.config(image=coup_de_grace)
    runepage_61.config(image=cut_down)
    runepage_62.config(image=last_stand)
    runepage_63.grid_forget()

def select_domination_sub():
    global sub_rune_type
    sub_rune_type = "domination"
    
    runepage_40.config(image=cheap_shot)
    runepage_41.config(image=taste_of_blood)
    runepage_42.config(image=sudden_impact)

    runepage_50.config(image=zombie_ward)
    runepage_51.config(image=ghost_poro)
    runepage_52.config(image=eyeball_collection)

    runepage_60.config(image=ravenous_hunter)
    runepage_61.config(image=relentless_hunter)
    runepage_62.config(image=ingenious_hunter)
    runepage_63.config(image=ultimate_hunter)
    runepage_63.grid(row=0, column=3)

def select_sorcery_sub():
    global sub_rune_type
    sub_rune_type = "sorcery"
    
    runepage_40.config(image=nullifying_orb)
    runepage_41.config(image=manaflow_band)
    runepage_42.config(image=nimbus_cloak)

    runepage_50.config(image=transcendence)
    runepage_51.config(image=celerity)
    runepage_52.config(image=absolute_focus)

    runepage_60.config(image=scorch)
    runepage_61.config(image=waterwalking)
    runepage_62.config(image=gathering_storm)
    runepage_63.grid_forget()

def select_resolve_sub():
    global sub_rune_type
    sub_rune_type = "resolve"
    
    runepage_40.config(image=demolish)
    runepage_41.config(image=font_of_life)
    runepage_42.config(image=shield_bash)

    runepage_50.config(image=conditioning)
    runepage_51.config(image=second_wind)
    runepage_52.config(image=bond_plating)

    runepage_60.config(image=overgrowth)
    runepage_61.config(image=revitalize)
    runepage_62.config(image=unflinching)
    runepage_63.grid_forget()

def select_inspiration_sub():
    global sub_rune_type
    sub_rune_type = "inspiration"
    
    runepage_40.config(image=hextech_flashtraption)
    runepage_41.config(image=magical_footwear)
    runepage_42.config(image=perfect_timing)

    runepage_50.config(image=future_market)
    runepage_51.config(image=minion_dematerializer)
    runepage_52.config(image=biscuit_delivery)

    runepage_60.config(image=cosmic_insight)
    runepage_61.config(image=approach_velocity)
    runepage_62.config(image=time_warp_tonic)
    runepage_63.grid_forget()

##############################################
# rune function
def command_03():
    stat_update(rune_code="03")

##############################################
# rune frame
if True:
    ##############################################

    runepage_precision = Button(runetype_frm, width=20, height=20, image=precision, command=select_precision)
    runepage_domination = Button(runetype_frm, width=20, height=20, image=domination, command=select_domination)
    runepage_sorcery = Button(runetype_frm, width=20, height=20, image=sorcery, command=select_sorcery)
    runepage_resolve = Button(runetype_frm, width=20, height=20, image=resolve, command=select_resolve)
    runepage_inspiration = Button(runetype_frm, width=20, height=20, image=inspiration, command=select_inspiration)

    runepage_precision.grid(row=0, column=0)
    runepage_domination.grid(row=0, column=1)
    runepage_sorcery.grid(row=0, column=2)
    runepage_resolve.grid(row=0, column=3)
    runepage_inspiration.grid(row=0, column=4)

    runemain0_frm = Frame(rune_frm)
    runemain0_frm.grid(row=1, column=0)

    runepage_00 = Button(runemain0_frm, width=20, height=20, image=basic_image)
    runepage_01 = Button(runemain0_frm, width=20, height=20, image=basic_image)
    runepage_02 = Button(runemain0_frm, width=20, height=20, image=basic_image)
    runepage_03 = Button(runemain0_frm, width=20, height=20, image=basic_image, command=command_03)

    runepage_00.grid(row=0, column=0)
    runepage_01.grid(row=0, column=1)
    runepage_02.grid(row=0, column=2)
    runepage_03.grid(row=0, column=3)

    runemain1_frm = Frame(rune_frm)
    runemain1_frm.grid(row=2, column=0)

    runepage_10 = Button(runemain1_frm, width=20, height=20, image=basic_image)
    runepage_11 = Button(runemain1_frm, width=20, height=20, image=basic_image)
    runepage_12 = Button(runemain1_frm, width=20, height=20, image=basic_image)

    runepage_10.grid(row=0, column=0)
    runepage_11.grid(row=0, column=1)
    runepage_12.grid(row=0, column=2)

    runemain2_frm = Frame(rune_frm)
    runemain2_frm.grid(row=3, column=0)

    runepage_20 = Button(runemain2_frm, width=20, height=20, image=basic_image)
    runepage_21 = Button(runemain2_frm, width=20, height=20, image=basic_image)
    runepage_22 = Button(runemain2_frm, width=20, height=20, image=basic_image)

    runepage_20.grid(row=0, column=0)
    runepage_21.grid(row=0, column=1)
    runepage_22.grid(row=0, column=2)

    runemain3_frm = Frame(rune_frm)
    runemain3_frm.grid(row=4, column=0)

    runepage_30 = Button(runemain3_frm,width=20, height=20, image=basic_image)
    runepage_31 = Button(runemain3_frm,width=20, height=20, image=basic_image)
    runepage_32 = Button(runemain3_frm,width=20, height=20, image=basic_image)
    runepage_33 = Button(runemain3_frm,width=20, height=20, image=basic_image)

    runepage_30.grid(row=0, column=0)
    runepage_31.grid(row=0, column=1)
    runepage_32.grid(row=0, column=2)
    runepage_33.grid(row=0, column=3)

    runetype_sub_frm = Frame(rune_frm, padx=10)
    runetype_sub_frm.grid(row=0, column=1)

    runepage_precision_sub = Button(runetype_sub_frm,width=20, height=20, image=precision, command=select_precision_sub)
    runepage_domination_sub = Button(runetype_sub_frm,width=20, height=20, image=domination, command=select_domination_sub)
    runepage_sorcery_sub = Button(runetype_sub_frm,width=20, height=20, image=sorcery, command=select_sorcery_sub)
    runepage_resolve_sub = Button(runetype_sub_frm,width=20, height=20, image=resolve, command=select_resolve_sub)
    runepage_inspiration_sub = Button(runetype_sub_frm,width=20, height=20, image=inspiration, command=select_inspiration_sub)

    runepage_precision_sub.grid(row=0, column=0)
    runepage_domination_sub.grid(row=0, column=1)
    runepage_sorcery_sub.grid(row=0, column=2)
    runepage_resolve_sub.grid(row=0, column=3)
    runepage_inspiration_sub.grid(row=0, column=4)

    runemain4_frm = Frame(rune_frm)
    runemain4_frm.grid(row=1, column=1)

    runepage_40 = Button(runemain4_frm,width=20, height=20, image=basic_image)
    runepage_41 = Button(runemain4_frm,width=20, height=20, image=basic_image)
    runepage_42 = Button(runemain4_frm,width=20, height=20, image=basic_image)

    runepage_40.grid(row=0, column=0)
    runepage_41.grid(row=0, column=1)
    runepage_42.grid(row=0, column=2)

    runemain5_frm = Frame(rune_frm)
    runemain5_frm.grid(row=2, column=1)

    runepage_50 = Button(runemain5_frm,width=20, height=20, image=basic_image)
    runepage_51 = Button(runemain5_frm,width=20, height=20, image=basic_image)
    runepage_52 = Button(runemain5_frm,width=20, height=20, image=basic_image)

    runepage_50.grid(row=0, column=0)
    runepage_51.grid(row=0, column=1)
    runepage_52.grid(row=0, column=2)

    runemain6_frm = Frame(rune_frm)
    runemain6_frm.grid(row=3, column=1)

    runepage_60 = Button(runemain6_frm,width=20, height=20, image=basic_image)
    runepage_61 = Button(runemain6_frm,width=20, height=20, image=basic_image)
    runepage_62 = Button(runemain6_frm,width=20, height=20, image=basic_image)
    runepage_63 = Button(runemain6_frm,width=20, height=20, image=basic_image)

    runepage_60.grid(row=0, column=0)
    runepage_61.grid(row=0, column=1)
    runepage_62.grid(row=0, column=2)
    runepage_63.grid(row=0, column=3)

select_precision()
select_domination_sub()

##############################################
# item frame
if True:
    item_frm = LabelFrame(bottom_frm, text="아이템", padx=10, pady=10)
    item_frm.pack(side="right")

    item_0 = Button(item_frm,width=20, height=20, image=basic_image)
    item_0.grid(row=0, column=0, sticky=N+E+W+S)

    item_1 = Button(item_frm,width=20, height=20, image=basic_image)
    item_1.grid(row=0, column=1, sticky=N+E+W+S)

    item_2 = Button(item_frm,width=20, height=20, image=basic_image)
    item_2.grid(row=0, column=2, sticky=N+E+W+S)

    item_3 = Button(item_frm,width=20, height=20, image=basic_image)
    item_3.grid(row=1, column=0, sticky=N+E+W+S)

    item_4 = Button(item_frm,width=20, height=20, image=basic_image)
    item_4.grid(row=1, column=1, sticky=N+E+W+S)

    item_5 = Button(item_frm,width=20, height=20, image=basic_image)
    item_5.grid(row=1, column=2, sticky=N+E+W+S)

    ##############################################

##############################################
# 챔피언을 바꾸거나 레벨을 바꿀 때는 룬을 초기화하고 바꿀 것
# 가능하면 룬을 초기화하고 챔피언 또는 레벨을 바꾸고 다시 룬을 적용시킬 것
# 룬을 켰을때 얻은 스탯과 룬을 껐을때 얻은 스탯이 다른 경우에 대비

# champion image
if True:
    no_champion = image_resize((20, 20), "gui_project/item_simulation/champion/no_champion.png")
    no_champion3 = image_resize((30, 30), "gui_project/item_simulation/champion/no_champion.png")

    zedd = image_resize((20, 20), "gui_project/item_simulation/champion/zedd.png")
    zedd3 = image_resize((30, 30), "gui_project/item_simulation/champion/zedd.png")

##############################################
# champion function (stat_data)
def select_champion():
    root_sub_champion = Toplevel(root)
    root_sub_champion.title("select champion")

    def click_no_champion():
        global current_champion

        champion_character.config(image=no_champion)
        current_champion = NONE
        
        reseting()

        root_sub_champion.destroy()

    def click_zedd():
        global current_champion

        champion_character.config(image=zedd)
        current_champion = "zedd"
        
        stat_update()
        root_sub_champion.destroy()
        

    cp_00 = Button(root_sub_champion,width=30, height=30, image=no_champion3, command=click_no_champion)
    cp_00.grid(row=0, column=0)
    
    cp_01 = Button(root_sub_champion,width=30, height=30, image=zedd3, command=click_zedd)
    cp_01.grid(row=0, column=1)

    # def clck():
    #     global current_champion
    #     current_champion = etr.get().split(" ")[0]
    #     root_sub_champion.destroy()

    # etr = Entry(root_sub_champion)
    # etr.pack(side="left")

    # bt = Button(root_sub_champion, text="확인", command=clck)
    # bt.pack(side="right")


def level_down():
    global level

    level = max(min(18, level - 1), 1)
    level_lb.config(text=f"Lv. {level}")

    stat_update()

def level_up():
    global level

    level = max(min(18, level + 1), 1)
    level_lb.config(text=f"Lv. {level}")

    stat_update()

def q_level_down():
    global q_level

    q_level = max(min(6, q_level - 1), 1)
    champion_q_lb.config(text=f"Q : {q_level}")

def q_level_up():
    global q_level

    q_level = max(min(6, q_level + 1), 1)
    champion_q_lb.config(text=f"Q : {q_level}")
    
def w_level_down():
    global w_level
    w_level = max(min(6, w_level - 1), 1)
    champion_w_lb.config(text=f"W : {w_level}")

def w_level_up():
    global w_level
    w_level = max(min(6, w_level + 1), 1)
    champion_w_lb.config(text=f"W : {w_level}")

def e_level_down():
    global e_level
    e_level = max(min(6, e_level - 1), 1)
    champion_e_lb.config(text=f"E : {e_level}")

def e_level_up():
    global e_level
    e_level = max(min(6, e_level + 1), 1)
    champion_e_lb.config(text=f"E : {e_level}")

def r_level_down():
    global r_level
    r_level = max(min(6, r_level - 1), 1)
    champion_r_lb.config(text=f"R : {r_level}")

def r_level_up():
    global r_level
    r_level = max(min(3, r_level + 1), 1)
    champion_r_lb.config(text=f"R : {r_level}")

def reset_all_levels():
    global level
    global q_level
    global w_level
    global e_level
    global r_level

    level = 1
    q_level = 1
    w_level = 1
    e_level = 1
    r_level = 1

    level_lb.config(text=f"Lv. {level}")
    champion_q_lb.config(text=f"Q : {q_level}")
    champion_w_lb.config(text=f"W : {w_level}")
    champion_e_lb.config(text=f"E : {e_level}")
    champion_r_lb.config(text=f"R : {r_level}")

    stat_update()

##############################################
# champion frame
if True:
    champion_frm = LabelFrame(bottom_frm, text="챔피언", padx=10)
    champion_frm.pack(side="right", padx=30)

    champion_level = Frame(champion_frm)
    champion_level.grid(row=0, column=0)

    champion_character = Button(champion_level,width=20, height=20, image=basic_image, command=select_champion)
    champion_character.grid(row=0, column=0)

    champion_name_lb = Label(champion_level, text="챔피언")
    champion_name_lb.grid(row=1, column=0)

    level_bt_frm = Frame(champion_level, padx=10, pady=10, relief="solid", bd=1)
    level_bt_frm.grid(row=0, column=1)

    level_down_bt = Button(level_bt_frm, width=20, height=20, image=downside, command=level_down)
    level_lb = Label(level_bt_frm, text=f"Lv. {level}")
    level_up_bt = Button(level_bt_frm, width=20, height=20, image=upside, command=level_up)

    level_down_bt.grid(row=0, column=0)
    level_lb.grid(row=0, column=1)
    level_up_bt.grid(row=0, column=2)

    champion_skill = Frame(champion_frm)
    champion_skill.grid(row=1, column=0)

    champion_q_frm = Frame(champion_skill)
    champion_q_frm.grid(row=0, column=0)

    q_level_bt_frm = Frame(champion_q_frm)
    q_level_bt_frm.pack(side="top", pady=10)

    q_level_down_bt = Button(q_level_bt_frm, width=7, height=7, image=downside, command=q_level_down)
    q_level_down_bt.pack(side="left")

    q_level_up_bt = Button(q_level_bt_frm, width=7, height=7, image=upside, command=q_level_up)
    q_level_up_bt.pack(side="right")

    champion_q_bt = Button(champion_q_frm,width=20, height=20, image=basic_image)
    champion_q_bt.pack(side="top")

    champion_q_lb = Label(champion_q_frm, text=f"Q : {q_level}")
    champion_q_lb.pack(side="bottom")

    champion_w_frm = Frame(champion_skill)
    champion_w_frm.grid(row=0, column=1)

    w_level_bt_frm = Frame(champion_w_frm)
    w_level_bt_frm.pack(side="top", pady=10)

    w_level_down_bt = Button(w_level_bt_frm, width=7, height=7, image=downside, command=w_level_down)
    w_level_down_bt.pack(side="left")

    w_level_up_bt = Button(w_level_bt_frm, width=7, height=7, image=upside, command=w_level_up)
    w_level_up_bt.pack(side="right")

    champion_w_bt = Button(champion_w_frm,width=20, height=20, image=basic_image)
    champion_w_bt.pack(side="top")

    champion_w_lb = Label(champion_w_frm, text=f"W : {w_level}")
    champion_w_lb.pack(side="bottom")

    champion_e_frm = Frame(champion_skill)
    champion_e_frm.grid(row=0, column=2)

    e_level_bt_frm = Frame(champion_e_frm)
    e_level_bt_frm.pack(side="top", pady=10)

    e_level_down_bt = Button(e_level_bt_frm, width=7, height=7, image=downside, command=e_level_down)
    e_level_down_bt.pack(side="left")

    e_level_up_bt = Button(e_level_bt_frm, width=7, height=7, image=upside, command=e_level_up)
    e_level_up_bt.pack(side="right")

    champion_e_bt = Button(champion_e_frm,width=20, height=20, image=basic_image)
    champion_e_bt.pack(side="top")

    champion_e_lb = Label(champion_e_frm, text=f"E : {e_level}")
    champion_e_lb.pack(side="bottom")

    champion_r_frm = Frame(champion_skill)
    champion_r_frm.grid(row=0, column=3)

    r_level_bt_frm = Frame(champion_r_frm)
    r_level_bt_frm.pack(side="top", pady=10)

    r_level_down_bt = Button(r_level_bt_frm, width=7, height=7, image=downside, command=r_level_down)
    r_level_down_bt.pack(side="left")

    r_level_up_bt = Button(r_level_bt_frm, width=7, height=7, image=upside, command=r_level_up)
    r_level_up_bt.pack(side="right")

    champion_r_bt = Button(champion_r_frm,width=20, height=20, image=basic_image)
    champion_r_bt.pack(side="top")

    champion_r_lb = Label(champion_r_frm, text=f"R : {r_level}")
    champion_r_lb.pack(side="bottom")

##############################################

root.mainloop()