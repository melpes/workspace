import pygame
class CharacterBase:

    def __init__(self, health, shield, fatigue, movementspeed, blessing):
        self.maxhealth = health
        self.currenthealth = self.maxhealth
        self.shield = shield
        self.fatigue = fatigue
        self.movementspeed = movementspeed
        self.blessing = blessing
        self.accumulated_damage = 0
        self.hemorrhage_time = 60 - self.blessing * 5

        self.hemorrhage_counting = 0

    def increasing_maxhealth(self, additional_health):
        self.maxhealth += additional_health

    def increasing_currenthealth(self, additional_health):
        self.currenthealth += additional_health

    def increasing_shield(self, additional_shield):
        self.shield += additional_shield

    def increasing_movementspeed(self, additional_movementspeed):
        self.shield += additional_movementspeed

    def increasing_blessing_level(self):
        self.blessing += 1
        if self.blessing >= 5:
            print(f"[경고] : 가호가 {self.blessing} 레벨 입니다.")
    def increasing_fatigue(self, fatigue):
            self.fatigue += fatigue
            if fatigue >= 100:
                print(f"[경고] : 피로도가 {self.fatigue}% 입니다.")

    def get_damaged(self, damage):
        self.shield_damage = ( self.shield / self.currenthealth ) * damage
        self.increasing_shield(-self.shield_damage)
        if self.shield_damage <= damage:
            self.increasing_currenthealth(self.shield_damage - damage)
            self.accumulated_damage += damage - self.shield_damage
            self.hemorrhage_counting = 0
            return damage - self.shield_damage
        else:
            return 0

    # 피로도 증가. 이동시 틱마다 dt 곱해서 불러낼 것
    def fatigue_management(self, coefficient1, coefficient2): # 계수1은 이속비례 증가계수, 계수2는 누적데미지 비례 증가계수
        for _ in range(round(self.movementspeed / self.maxhealth * coefficient1)): # 이속 0일때 기본피로증가 0
            self.increasing_fatigue(self.accumulated_damage / self.maxhealth * coefficient2)
        print(self.fatigue)

    # 출혈데미지. 
    def hemorrhage(self, damage, dt):
        # for _ in range(round((60 - self.blessing * 5) / dt * 1000)):
        #     pygame.time.Clock().tick(goal_fps)
        #     hemorrhage_damage = damage * (1 + (self.fatigue ** 2) / 5000 )
        #     self.increasing_currenthealth(hemorrhage_damage / round((60 / dt * 1000)))
        # print(self.currenthealth)
        hemorrhage_total_damage = damage * (1 + (self.fatigue ** 2) / 5000 )
        self.increasing_currenthealth(-hemorrhage_total_damage / (60 / (dt / 1000)))
        self.hemorrhage_counting += 1