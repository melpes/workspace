import random
from roboid import * # 작은 로봇 조종하는 모듈

hamster = Hamster()
# denoise의 매개변수로 사용하기 위함이라면 denoise의 value와 이 value는 다르므로 필요 없다!
value = 0 

def denoise(value):
    if value < 10: 
        return 0
    return value

# 위 함수랑 같은 의미인데 한줄로. 굳이 외워서까지 쓸 필요는 없다. 
# 남들이 쓴 것을 이해만 할 수 있으면 됨
def denoise(value):
    return value if value >= 10 else 0


while True:
    print("R:", hamster.right_proximity(), "L", hamster.left_proximity())
    # 아래처럼 사용하면 원하는 위치에 정확하게 변수를 사용해서 값을 넣을 수 있다!
    # 정확한 원리는 문자열 시작 전에 f를 붙이고 문자열 내부에 {}로 감싸여 있는 항목은
    # 이를 문자열 자체가 아닌 변수나 함수로 인식함
    print(f"R : {hamster.right_proximity()} L : {hamster.left_proximity()}")

############################################################################################

    if hamster.left_proximity() > 50: 
        hamster.wheels(30, 30) 
        wait(1000)
        hamster.wheels(30, -30) 
        wait(805)
        hamster.wheels(30, 30)
        wait(1000)
    elif hamster.right_proximity() > 50: 
        if hamster.left_proximity() < 5: 
            hamster.wheels(30, 30) 
            wait(2000)
        else :
            hamster.wheels(30, 30) 
            wait(1000)
            hamster.wheels(-30, 30) 
            wait(805)
            hamster.wheels(30, 30)
            wait(1000)

############################################################################################
    # 계속 반복되는 함수가 아니고 반복되는 값이므로 치환해서 사용
    proxi = [hamster.left_proximity(), hamster.right_proximity()]
    speed = 30

    if proxi[0] > 50: 
        hamster.wheels(speed, speed) 
        wait(1000)
        hamster.wheels(speed, -speed) 
        wait(805)
        hamster.wheels(speed, speed)
        wait(1000)
    elif proxi[1] > 50: 
        if proxi[0] < 5: 
            hamster.wheels(speed, speed) 
            wait(2000)
        else :
            hamster.wheels(speed, speed) 
            wait(1000)
            hamster.wheels(-speed, speed) 
            wait(805)
            hamster.wheels(speed, speed)
            wait(1000)
        
    if proxi[0] > 50:
        hamster.wheels(speed, speed) 
        wait(1000)
        hamster.wheels(speed, -speed) 
        wait(805)
        hamster.wheels(speed, speed)
        wait(1000)
    elif proxi[1] < 50:
        
############################################################################################

    else:
        left_speed = denoise(60 - hamster.right_proximity())
        right_speed = denoise(60 - hamster.left_proximity())

        hamster.wheels(left_speed, right_speed)
        
        if left_speed <= 0 and right_speed <= 0 and hamster.left_proximity() < 1\
            and hamster.right_proximity() < 1:
            hamster.wheels(speed, -speed) 
            wait(1610)

############################################################################################

    else:
        left_speed = denoise(60 - proxi[1])
        right_speed = denoise(60 - proxi[0])

        hamster.wheels(left_speed, right_speed)
        
        if left_speed <= 0 and right_speed <= 0 and\
            proxi[0] < 1 and proxi[1] < 1:
            hamster.wheels(speed, -speed) 
            wait(1610)


    wait(20) 
