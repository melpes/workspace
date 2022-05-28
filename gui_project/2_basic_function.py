import tkinter.messagebox as msgbox
from tkinter import filedialog
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("LAC GUI")

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir="C:/") # 최초에 C:/경로를 보여줌
    for file in files:
        lst_file.insert(END, file)

def del_file():
    for index in reversed(lst_file.curselection()):
        lst_file.delete(index)

def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "":
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

def start():
    if lst_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요.")
        return
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요.")
        return

# 파일 프레임
file_frm = Frame(root)
file_frm.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frm, padx=5, pady=5, width=12, text='파일추가', command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frm, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
lst_frm = Frame(root)
lst_frm.pack(fill="both", padx=5, pady=5)

scbar = Scrollbar(lst_frm)
scbar.pack(side="right", fill="y")

lst_file = Listbox(lst_frm, selectmode="extended", height=15, yscrollcommand=scbar.set)
lst_file.pack(side="left", fill="both", expand=True)
scbar.config(command=lst_file.yview)

# 저장 경로 프레임
path_frm = LabelFrame(root, text="저장경로")
path_frm.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frm)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frm, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frm_option = LabelFrame(root, text="옵션")
frm_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 라벨
lbl_width = Label(frm_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frm_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 라벨
lbl_space = Label(frm_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frm_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 파일 포맷 옵션 라벨
lbl_format = Label(frm_option, text="형식", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frm_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 progress bar
frm_prgress = ttk.Labelframe(root, text="진행상황")
frm_prgress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
prgress_bar = ttk.Progressbar(frm_prgress, maximum=100, variable=p_var)
prgress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frm_run = Frame(root)
frm_run.pack(fill='x', padx=5, pady=5)

btn_close = Button(frm_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frm_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()