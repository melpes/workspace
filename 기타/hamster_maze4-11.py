import random
from roboid import *
import time

hamster = Hamster()

def denoise(value):
    if value < 10: 
        return 0
    return value



while True:
    proxi = [hamster.left_proximity(), hamster.right_proximity()]
    print(f"R : {proxi[0]} L : {proxi[1]}")

    if proxi[0] < 50

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
    
    else:
        left_speed = denoise(60 - hamster.right_proximity())
        right_speed = denoise(60 - hamster.left_proximity())

        hamster.wheels(left_speed, right_speed)
        
        if left_speed and right_speed <= 0 and hamster.left_proximity() and hamster.right_proximity() <1:
            hamster.wheels(30, -30) 
            wait(1610)

    wait(20) 
