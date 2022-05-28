from pygame import Vector3

class CoordSysError(Exception):
    pass

def transform3(i:Vector3, coorsys:tuple, default:Vector3 = Vector3(0, 0, 0)) -> Vector3:
    f = []
    for a in range(3):
        f.append(Vector3.normalize(coorsys[a]))

    if f[0] != Vector3.cross(f[2], f[1]):
        raise CoordSysError

    screen : Vector3 = Vector3()
    for a in range(3):
        screen[a] = i.x * f[a].x + i.y * f[a].y + i.z * f[a].z
    if default:
        screen += default
    
    return screen

def transform2(i:Vector3, coorsys:tuple, default:Vector3 = Vector3(0, 0, 0)) -> Vector3:
    f = []
    i = Vector3(i)
    for a in range(3):
        f.append(Vector3.normalize(coorsys[a]))

    if f[0] != Vector3.cross(f[2], f[1]):
        raise CoordSysError

    screen : Vector3 = Vector3()
    for a in range(3):
        screen[a] = i.x * f[a].x + i.y * f[a].y + i.z * f[a].z
    if default:
        screen += default
    
    return screen[0], screen[1]