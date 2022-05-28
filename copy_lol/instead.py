# 초기 셋업
import sys, copy, pygame, os
from pygame.locals import *

FPS = 60
# 프로그램 윈도우의 너비, 높이 [픽셀]
WINWIDTH, WINHEIGHT = 800, 600
HALF_WINWIDTH, HALF_WINHEIGHT = int(WINWIDTH / 2), int(WINHEIGHT / 2)

# 각 타일의 너비, 높이 [픽셀]
TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 40

# 색 종류
BGCOLOR = (31, 30, 51)
TEXTCOLOR = (255, 255, 255)

# 자주 쓰는 문자열 상수화
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

def main() -> None:
    # 전역 변수와 상수 지정
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, BASICFONT, CHARACTERIMAGES

    # pygame 초기화와 전역변수 기본 셋업
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    # 윈도우 제목
    pygame.display.set_caption("copied_Lol")
    # 기본 폰트와 크기 지정
    BASICFONT = pygame.font.Font("freesansbold.ttf", 18)

    # 모든 기본 이미지 surface 객체를 저장하는 전역 dict
    IMAGESDICT = {
        "corner" : pygame.image.load("copy_lol/images/Wall_Block_Tall.png"),
        "wall" : pygame.image.load("copy_lol/images/Wood_Block_Tall.png"),
        "bright stone floor" : pygame.image.load("copy_lol/images/Plain_Block_Bright.png"),
        "dark stone floor" : pygame.image.load("copy_lol/images/Plain_Block_Dark.png"),
        "grass floor" : pygame.image.load("copy_lol/images/Grass_Block.png"),
        "princess" : pygame.image.load("copy_lol/images/princess.png"),
        "boy" : pygame.image.load("copy_lol/images/boy.png"),
        "catgirl" : pygame.image.load("copy_lol/images/catgirl.png"),
        "horngirl" : pygame.image.load("copy_lol/images/horngirl.png"),
        "pinkgirl" : pygame.image.load("copy_lol/images/pinkgirl.png"),
        "rock" : pygame.image.load("copy_lol/images/Rock.png"),
        "short tree" : pygame.image.load("copy_lol/images/Tree_Short.png"),
        "tall tree" : pygame.image.load("copy_lol/images/Tree_Tall.png"),
        "bush" : pygame.image.load("copy_lol/images/Bush.png")
    }
    # 전역 dict. 맵 파일의 문자들에 이미지를 대입하는 역할
    TILEMAPPING = {
        "#" : IMAGESDICT["wall"],
        "+" : IMAGESDICT["corner"],
        "o" : IMAGESDICT["bright stone floor"],
        "x" : IMAGESDICT["dark stone floor"],
        "w" : IMAGESDICT["grass floor"],
        "r" : IMAGESDICT["rock"],
        "t" : IMAGESDICT["short tree"],
        "T" : IMAGESDICT["tall tree"],
        "b" : IMAGESDICT["bush"]
    }
    # 캐릭터 리스트
    CHARACTERIMAGES = [
        IMAGESDICT["princess"],
        IMAGESDICT["boy"],
        IMAGESDICT["catgirl"],
        IMAGESDICT["horngirl"],
        IMAGESDICT["pinkgirl"]
    ]
    
    # 텍스트 파일에서 레벨을 읽어 온다.
    levels : list = read_levels_file("copy_lol/maps.txt")
    current_level_index = 0

    # 메인 게임 루프. 각 단계가 한 번의 루프이다.
    while True:
        result = run_level(levels, current_level_index)

def run_level(levels, current_level_index) -> str:
    levelObj = levels[current_level_index]
    mapObj = decorateMap(levelObj["mapObj"])
    gameStateObj = copy.deepcopy(levelObj["startState"])

    mapNeedsRedraw = True

    mapWidth = len(mapObj) * TILEWIDTH
    mapHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT

    # 메인 게임 루프
    mouse_pos = None
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            else:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 3:
                        mouse_pos = event.pos
                        print(event.pos)
                if event.type == KEYDOWN:
                    if event.key == K_s:
                        mouse_pos = None
        
        if mouse_pos:
            moved = makeMove(mapObj, gameStateObj, mouse_pos, 0.2, dt)
            if moved:
                mapNeedsRedraw = True

        DISPLAYSURF.fill(BGCOLOR)

        if mapNeedsRedraw:
            mapSurf = drawMap(mapObj, gameStateObj)
            mapNeedsRedraw = False

        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

        DISPLAYSURF.blit(mapSurf, mapSurfRect)

        pygame.display.update()
        dt = FPSCLOCK.tick(FPS)

def read_levels_file(filename) -> list:
    assert os.path.exists(filename), f"Cannot find the level file : {filename}"

    with open(filename, "r") as mapFile:
        content = mapFile.readlines() + ["\n"]

    
    levels = []
    mapTextLines = []
    mapObj = []
    levelnum = 0

    # 각 줄 처리
    for line in content:
        line = line.rstrip("\n")

        if ";" in line: # ; 이후의 것은 무시
            line = line[:line.find(";")]

        if line != "": # 빈칸이 아니면 mapTextLines에 추가
            mapTextLines.append(line)
        
        # 빈칸이고 mapTextLines에 뭐라도 있으면 추가 종료하고 맵 처리 진행
        elif line == "" and len(mapTextLines) > 0:
            # 맵을 직사각형으로 만든다.
            maxWidth = max(map(len, mapTextLines))
            for i in range(len(mapTextLines)):
                mapTextLines[i] += " " * (maxWidth - len(mapTextLines[i]))

            # mapTextLines를 맵 객체로 변환
            for _ in range(maxWidth):
                mapObj.append([])
            for y in range(len(mapTextLines)):
                for x in range(maxWidth):
                    # assert mapTextLines[y][x] in TILEMAPPING,\
                    # f"Level {levelnum+1} in {filename} has a strange word : {mapTextLines[y][x]}"
                    mapObj[x].append(mapTextLines[y][x])

            # 맵 속에 있는 특정 문자들을 찾아 startState에 적용한다.
            startx, starty = None, None
            enemies = []
            
            for x in range(maxWidth):
                for y in range(len(mapObj[x])):
                    if mapObj[x][y] == "@":
                        startx, starty = (x + 0.5) * TILEWIDTH, (y - 1) * TILEFLOORHEIGHT + TILEHEIGHT

            # 레벨 디자인 유효성 검사
            assert startx != None and starty != None,\
            f"Level {levelnum+1} in {filename} is missing a \"@\" to mark the start point"


            # 레벨 객체 생성
            gameStateObj = {
                "player" : (startx, starty), 
                "enemies" : enemies
            }
            levelObj = {
                "mapObj" : mapObj,
                "startState" : gameStateObj
            }
            levels.append(levelObj)

            # 다음 맵을 위한 변수 초기화
            mapTextLines = []
            mapObj = []
            gameStateObj = {}
            levelnum += 1
    return levels

def decorateMap(mapObj) -> list:
    mapObjCopy = copy.deepcopy(mapObj)

    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[x])):
            if mapObjCopy[x][y] in ("@"): # 캐릭터 위치 표현들은 전부 포함시킬 것
                mapObjCopy[x][y] = "o"
    return mapObjCopy

def makeMove(mapObj, gameStateObj, dir_pos, speed, dt) -> bool:
    player_pos = pygame.Vector2(gameStateObj["player"])
    dir = pygame.Vector2(dir_pos)
    offset = dir - player_pos - pygame.Vector2(25, 100)
    if offset.length() <= 10:
        offset = (0, 0)
    else:
        offset.scale_to_length(speed)

    playerx, playery = player_pos
    xOff, yOff = offset

    to_x, to_y = xOff * dt, yOff * dt
    # print(to_x, to_y)

    if isWall(mapObj, playerx + to_x, playery + to_y):
        return False
    gameStateObj["player"] = (playerx + to_x, playery + to_y)
    return True

def isWall(mapObj, x, y) -> bool:
    x, y = int(x / TILEWIDTH), int(y / TILEFLOORHEIGHT)
    if x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return False
    elif mapObj[x][y] in ("#", "+", "r"):
        return True

def drawMap(mapObj, gameStateObj) -> pygame.Surface:
    mapSurfWidth = len(mapObj) * TILEWIDTH
    mapSurfHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill((BGCOLOR))

    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))

            baseTile = TILEMAPPING[mapObj[x][y]]
            mapSurf.blit(baseTile, spaceRect)

    playerRect = CHARACTERIMAGES[0].get_rect()
    playerRect.center = gameStateObj["player"]
    mapSurf.blit(CHARACTERIMAGES[0], playerRect)

    return mapSurf

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()