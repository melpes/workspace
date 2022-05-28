import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWidgets(QWidget):

    def __init__(self):

        # A스텟, 전투화면, B스텟 배치 박스
        super().__init__()
        self.formbox = QHBoxLayout()
        self.setLayout(self.formbox)

        # 캐릭터 생성
        self.character = [CharacterStat(100, 20, 20) for _ in range(2)]
        print(type(self.character[0]))

        # 공통 스텟 창
        self.stat = [QVBoxLayout(), QVBoxLayout()]
        # 전투 창
        self.battle = QVBoxLayout()
        sd = QLabel("가나다라마바사아자차카타파하")     # 임시
        self.battle.addWidget(sd)
        
        # 화면 크기 설정
        self.setGeometry(2400, 350, 500, 500)

        for i in range(2):
            self.lbb = QLabel("체력")
            self.lbb.setAlignment(Qt.AlignCenter)
            self.stat[i].addWidget(self.lbb)         # 체력 레이아웃 배치

        self.UIlasting()            
        
        
        self.attackbt = []
        for i in range(2):
            self.attackbt.append(QPushButton("공격"))
        self.healbt = []
        for i in range(2):
            self.healbt.append(QPushButton("힐"))
        self.grid = []
        for i in range(2):
            self.grid.append(QGridLayout())
            self.grid[i].addWidget(self.attackbt[i], 0, 0)
            self.grid[i].addWidget(self.healbt[i], 0, 1)
            self.stat[i].addLayout(self.grid[i])

        for i in range(2):
            if i == 0:
                self.attackbt[i].clicked.connect(lambda : self.attack(1, 20))
            if i == 1:
                self.attackbt[i].clicked.connect(lambda : self.attack(0, 20))
            if i == 0:
                self.healbt[i].clicked.connect(lambda : self.heal(0, 10))
            if i == 1:
                self.healbt[i].clicked.connect(lambda : self.heal(1, 10))
        for i in range(2):
            self.stat[i].addStretch(1)


        self.formbox.addLayout(self.stat[0])
        self.formbox.addLayout(self.battle)
        self.formbox.addLayout(self.stat[1])

    def UIlasting(self):
        self.hppbar = []
        for i in range(2):
            self.hppbar.append(QProgressBar())
            self.hppbar[i].setMinimum(0)
            self.stat[i].addWidget(self.hppbar[i])
            self.hppbar[i].setMaximum(self.character[i].maxhp + self.character[i].shield) # 실드 줄어들 때 갱신하는 시스템 부여 필요
            self.hppbar[i].setValue(self.character[i].crrhp + self.character[i].shield)    # 현재체력 비율 표시

        self.grid2 = []
        for i in range(2):
            self.grid2.append(QGridLayout())
        self.hppstat = []
        for i in range(2):
            self.hppstat.append(QLabel(f"{self.character[i].crrhp}(+{self.character[i].shield})/{self.character[i].maxhp}"))
        for i in range(2):
            self.grid2[i].addWidget(self.hppstat[i], 0, 0)
        for i in range(2):
            self.stat[i].addLayout(self.grid2[i])


    def attack(self, i, damage):
        if self.character[i].shield > damage:
            self.character[i].shield -= damage
        elif self.character[i].shield > 0:
            shieldwas = self.character[i].shield
            self.character[i].shield = 0
            self.character[i].crrhp -= damage - shieldwas
        elif self.character[i].shield == 0:
            self.character[i].crrhp -= damage
        self.hppbar[i].setMaximum(self.character[i].maxhp + self.character[i].shield) # 실드 줄어들 때 갱신하는 시스템 부여 필요
        self.hppbar[i].setValue(self.character[i].crrhp + self.character[i].shield)    # 현재체력 비율 표시
        print(i)
    
    def heal(self, i, heal):
        if self.character[i].crrhp < self.character[i].maxhp:
            if self.character[i].crrhp + heal < self.character[i].maxhp:
                self.character[i].crrhp += heal
            else:
                self.character[i].crrhp = self.character[i].maxhp
        self.hppbar[i].setMaximum(self.character[i].maxhp + self.character[i].shield) # 실드 줄어들 때 갱신하는 시스템 부여 필요
        self.hppbar[i].setValue(self.character[i].crrhp + self.character[i].shield)    # 현재체력 비율 표시
        print(i)

        

class CharacterStat:
    def __init__(self, maxhp, shield, speed):
        self.maxhp = maxhp
        self.shield = shield
        self.speed = speed
        self.crrhp = maxhp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWidgets()
    w.show()
    sys.exit(app.exec_())