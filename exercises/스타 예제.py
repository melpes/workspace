from random import *
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name} 유닛이 생성되었습니다.")

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. 현재 속도 {self.speed}")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 피해를 받았습니다.")
        self.hp -= damage
        if self.hp > 0:
            print(f"현재 체력은 {self.hp} 입니다.")
        else:
            print("파괴되었습니다.")

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적에게 {self.damage} 피해를 입혔습니다.")

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{self.name} : {location} 방향으로 비행합니다. 현재 속도 {self.flying_speed}")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, flying_speed, damage):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다.")
        else:
            print(f"{self.name} : 체력이 부족합니다.")

class Tank(AttackUnit):
    seize_developed = False
    if seize_developed == True:
        print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.seize_mode = True
        else:
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.damage /= 2
            self.seize_mode = False

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 5, 20)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print(f"{self.name} : 클로킹 모드 해제합니다.")
            self.clocked = False
        else:
            print(f"{self.name} : 클로킹 모드 진입합니다.")
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

game_start()
num_of_marine = int(input("생성할 마린의 수 :")) + 1
num_of_tank = int(input("생성할 탱크의 수 :")) + 1
num_of_wraith = int(input("생성할 레이스의 수 :")) + 1

attack_units = []
for i in range(1,num_of_marine):
    attack_units.append(Marine())

for i in range(1,num_of_tank):
    attack_units.append(Tank())

for i in range(1,num_of_wraith):
    attack_units.append(Wraith())

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,50))

game_over()