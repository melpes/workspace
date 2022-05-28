# 초기 셋업
import random, sys, copy, os, pygame
from pygame.locals import *

# 프로그램 윈도우의 너비, 높이 [픽셀]
FPS = 30
WINWIDTH = 800
WINHEIGHT = 600
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

# 각 타일의 너비, 높이 [픽셀]
TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 40 # 40 또는 45 정확하지 않음

CAM_MOVE_SPEED = 1 # [픽셀/초]

# 맵을 꾸미는 주변의 타일들의 비율
OUTSIDE_DECORATION_PCT = 20 # [%]

# 색 종류
BRIGHTBLUE  = (0, 170, 255)
WHITE       = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

# 자주 쓰는 문자열 상수화
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

def main() -> None:
    # 전역 변수와 상수 지정
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, \
    OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage
    
    # pygame 초기화와 전역변수 기본 셋업
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    # set_mode에서 반환한 surface 객체를 저장. update 호출 시 화면에 surface 객체를 그림
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    # 윈도우 제목
    pygame.display.set_caption("Star Pusher")
    # 기본 폰트와 크기 지정
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    # 모든 이미지 surface 객체를 저장하는 전역 dict
    IMAGESDICT = {
        "uncovered goal" : pygame.image.load("pygame_project/starpusher/RedSelector.png"),
        "covered goal" : pygame.image.load("pygame_project/starpusher/Selector.png"),
        "star" : pygame.image.load("pygame_project/starpusher/Star.png"),
        "corner" : pygame.image.load("pygame_project/starpusher/Wall_Block_Tall.png"),
        "wall" : pygame.image.load("pygame_project/starpusher/Wood_Block_Tall.png"),
        "inside floor" : pygame.image.load("pygame_project/starpusher/Plain_Block.png"),
        "outside floor" : pygame.image.load("pygame_project/starpusher/Grass_Block.png"),
        "title" : pygame.image.load("pygame_project/starpusher/star_title.png"),
        "solved" : pygame.image.load("pygame_project/starpusher/star_solved.png"),
        "princess" : pygame.image.load("pygame_project/starpusher/princess.png"),
        "boy" : pygame.image.load("pygame_project/starpusher/boy.png"),
        "catgirl" : pygame.image.load("pygame_project/starpusher/catgirl.png"),
        "horngirl" : pygame.image.load("pygame_project/starpusher/horngirl.png"),
        "pinkgirl" : pygame.image.load("pygame_project/starpusher/pinkgirl.png"),
        "rock" : pygame.image.load("pygame_project/starpusher/Rock.png"),
        "short tree" : pygame.image.load("pygame_project/starpusher/Tree_Short.png"),
        "tall tree" : pygame.image.load("pygame_project/starpusher/Tree_Tall.png"),
        "ugly tree" : pygame.image.load("pygame_project/starpusher/Tree_Ugly.png")
    }
    # 전역 dict. 레벨 파일의 문자들에 이미지를 대입하는 역할
    TILEMAPPING = {
        "x" : IMAGESDICT["corner"],
        "#" : IMAGESDICT["wall"],
        "o" : IMAGESDICT["inside floor"],
        " " : IMAGESDICT["outside floor"]
    }
    OUTSIDEDECOMAPPING = {
        "1" : IMAGESDICT["rock"],
        "2" : IMAGESDICT["short tree"],
        "3" : IMAGESDICT["tall tree"],
        "4" : IMAGESDICT["ugly tree"]
    }

    # 플레이어블 캐릭터 리스트
    PLAYERIMAGES = [
        IMAGESDICT["princess"],
        IMAGESDICT["boy"],
        IMAGESDICT["catgirl"],
        IMAGESDICT["horngirl"],
        IMAGESDICT["pinkgirl"]
    ]
    # 현재 플레이어의 캐릭터 이미지 인덱스
    currentImage = 0

    startScreen() # 플레이어가 키를 누를 때까지 타이틀 화면을 보여줌

    # 텍스트 파일에서 레벨을 읽어 온다.
    # 레벨 파일의 자세한 사항과 레벨 파일을 만드는 방법은 readLevelsFile()을 참고
    levels : list = readLevelsFile("pygame_project/starpusher/starPusherLevels.txt")
    currentLevelIndex = 0

    # 메인 게임 루프. 이 루프는 레벨 하나에 대해 수행한다. 즉 한번 반복될 때마다 레벨 하나를 시도.
    # 플레이어가 레벨을 완료하면 다음 레벨을 로드한다.
    while True:
        # 레벨을 수행하여 게임을 플레이한다.
        # 게임을 종료하면 runLevel은 다음 문자열 중 하나를 반환한다.
        # solved, next, back, reset
        result = runLevel(levels, currentLevelIndex)

        if result in ('solved', 'next'):
            # 다음 레벨로 이동
            currentLevelIndex += 1
            if currentLevelIndex >= len(levels):
                currentLevelIndex = 0
        elif result == "back":
            # 이전 레벨로 이동
            currentLevelIndex -= 1
            if currentLevelIndex < 0:
                currentLevelIndex = len(levels) - 1
        elif result == "reset":
            # 아무것도 하지 않으면 다시 루프문 처음으로 돌아가 레벨을 다시 불러온다.
            pass

def runLevel(levels, levelNum) -> str:
    global currentImage
    levelObj = levels[levelNum] # 선택한 레벨의 레벨 객체 저장
    mapObj = decorateMap(levelObj["mapObj"], levelObj["startState"]["player"]) # 맵 객체 저장
    # 플레이가 끝나면 처음 맵 상태로 되돌리기 위해 초기 상태 값을 저장(깊은 복사)
    # 깊은 복사를 하지 않고 대입하면 얕은 복사가 되어 주소를 복사하게 된다. 즉, 같은 대상을 두 대상이 공유하게 됨
    # 이 경우 한 대상에서 값을 변화시켜도 모든 대상에서 값이 변하게 된다.
    gameStateObj = copy.deepcopy(levelObj["startState"])

    # drawMap()을 호출하기 위해 True로 설정한다. 매 프레임마다 새로 그릴 필요가 없으므로 필요할 때만 호출하는것.
    mapNeedsRedraw = True
    # 현재 레벨을 표기
    levelSurf = BASICFONT.render("Level %s of %s" % (levelNum + 1, len(levels)), 1, TEXTCOLOR)
    # levelSurf 위치 설정
    levelRect = levelSurf.get_rect()
    levelRect.bottomleft = (20, WINHEIGHT - 35)
    # mapObj가 맵 객체인데 세로줄 하나를 묶은 것을 요소로 한 것으로 보인다.
    # 따라서 mapWidth = 맵 객체 요소 개수 * 한 타일 가로 길이
    # mapHeight = (맵 객체 첫 요소 속 요소 개수 - 1) * 한 타일 바닥 부분 세로 길이 + 한 타일 전체 세로 길이
    mapWidth = len(mapObj) * TILEWIDTH
    mapHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT
    MAX_CAM_X_PAN = abs(HALF_WINHEIGHT - int(mapHeight / 2))
    MAX_CAM_Y_PAN = abs(HALF_WINWIDTH - int(mapWidth / 2))

    levelIsComplete = False
    # 카메라가 얼마나 움직였는지 기록
    cameraOffsetX = 0
    cameraOffsetY = 0
    # 카메라를 움직이는 키를 계속 누르고 있는지 검사한다.
    cameraUp = False
    cameraDown = False
    cameraLeft = False
    cameraRight = False

    # 메인 게임 루프. 한 레벨을 플레이하는 동안 작동한다.
    while True:
        # 변수들 재설정
        playerMoveTo = None
        keyPressed = False

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                # 키 누름 체크
                keyPressed = True
                if event.key == K_LEFT:
                    playerMoveTo = LEFT
                elif event.key == K_RIGHT:
                    playerMoveTo = RIGHT
                elif event.key == K_UP:
                    playerMoveTo = UP
                elif event.key == K_DOWN:
                    playerMoveTo = DOWN
                
                # 카메라 무브 모드 설정
                elif event.key == K_a:
                    cameraLeft = True
                elif event.key == K_d:
                    cameraRight = True
                elif event.key == K_w:
                    cameraUp = True
                elif event.key == K_s:
                    cameraDown = True

                elif event.key == K_n:
                    return "next"
                elif event.key == K_b:
                    return "back"

                elif event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_BACKSPACE:
                    return "reset"
                elif event.key == K_p:
                    # 플레이어 이미지를 다음 이미지로 바꾼다.
                    currentImage += 1
                    if currentImage >= len(PLAYERIMAGES):
                        currentImage = 0
                    mapNeedsRedraw = True
            elif event.type == KEYUP:
                # 카메라 무브 모드 설정 해제
                if event.key == K_a:
                    cameraLeft = False
                elif event.key == K_d:
                    cameraRight = False
                elif event.key == K_w:
                    cameraUp = False
                elif event.key == K_s:
                    cameraDown = False
        
        if playerMoveTo != None and not levelIsComplete:
            # 플레이어가 방향키를 누름
            # 움직일 수 있는 상황인지 체크하고 가능하면 별도 같이 민다.
            moved = makeMove(mapObj, gameStateObj, playerMoveTo)
            if moved:
                # stepCounter를 증가시킨다.
                # 이동 횟수 제한을 위한 것
                gameStateObj["stepCounter"] += 1
                mapNeedsRedraw = True
            
            if isLevelFinished(levelObj, gameStateObj):
                # 레벨을 다 풀었으면 'Solved!' 이미지를 보여준다.
                levelIsComplete = True
                keyPressed = False
        
        DISPLAYSURF.fill(BGCOLOR)

        if mapNeedsRedraw:
            mapSurf = drawMap(mapObj, gameStateObj, levelObj["goals"])
            mapNeedsRedraw = False
        
        if cameraUp and cameraOffsetY < MAX_CAM_X_PAN:
            cameraOffsetY += CAM_MOVE_SPEED
        elif cameraDown and cameraOffsetY > -MAX_CAM_X_PAN:
            cameraOffsetY -= CAM_MOVE_SPEED
        if cameraLeft and cameraOffsetX < MAX_CAM_Y_PAN:
            cameraOffsetX += CAM_MOVE_SPEED
        elif cameraRight and cameraOffsetX > -MAX_CAM_Y_PAN:
            cameraOffsetX -= CAM_MOVE_SPEED

        # 카메라 오프셋에 맞게 mapSurf의 Rect 객체를 조정한다.
        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH + cameraOffsetX, HALF_WINHEIGHT + cameraOffsetY)

        # mapSurf를 displaysurf에 그린다.
        DISPLAYSURF.blit(mapSurf, mapSurfRect)

        DISPLAYSURF.blit(levelSurf, levelRect)
        stepSurf = BASICFONT.render("Steps %s" % (gameStateObj["stepCounter"]), 1, TEXTCOLOR)
        stepRect = stepSurf.get_rect()
        stepRect.bottomleft = (20, WINHEIGHT - 10)
        DISPLAYSURF.blit(stepSurf, stepRect)

        if levelIsComplete:
            # 레벨을 다 풀었으면 플레이어가 키를 누를 때까지
            # solved 이미지를 보여준다.
            solvedRect = IMAGESDICT["solved"].get_rect()
            solvedRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)
            DISPLAYSURF.blit(IMAGESDICT["solved"], solvedRect)

            if keyPressed:
                return "solved"

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isWall(mapObj, x, y) -> bool:
    # 맵상의 (x, y)위치가 벽이면 True를 반환, 아니면 False를 반환
    if x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return False
    elif mapObj[x][y] in ("#", "x"):
        return True
    return False

def decorateMap(mapObj, startxy) -> list:
    # 주어진 맵 객체의 복사본을 만들어서 수정한다.
    # 수정 항목은 다음과 같다.
        # 코너의 벽은 코너 피스로 바꾼다.
        # 외부와 내부를 구분하는 타일을 배치한다.
        # 타일 외부에 나무/벽 장식 피스를 무작위로 배치한다.
    # 이후 수정된 맵 객체를 반환한다.
    
    startx, starty = startxy

    # 맵 객체를 복사한다.
    mapObjCopy = copy.deepcopy(mapObj)

    # 맵 데이터에서 벽이 아닌 부분을 제거한다.
    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):
            if mapObjCopy[x][y] in ("$", ".", "@", "+", "*"):
                mapObjCopy[x][y] = " "
    
    # 외부와 내부 타일을 구분하기 위해 floodFill 알고리즘을 사용한다.
    floodFill(mapObjCopy, startx, starty, " ", "o")

    # 서로 코너에 인접해 있는 벽을 코너 타일로 바꾼다.
    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):

            if mapObjCopy[x][y] == "#":
                if  (isWall(mapObjCopy, x, y-1) and isWall(mapObjCopy, x+1, y)) or \
                    (isWall(mapObjCopy, x+1, y) and isWall(mapObjCopy, x, y+1)) or \
                    (isWall(mapObjCopy, x, y+1) and isWall(mapObjCopy, x-1, y)) or \
                    (isWall(mapObjCopy, x-1, y) and isWall(mapObjCopy, x, y-1)):
                    mapObjCopy[x][y] = "x"

            elif mapObjCopy[x][y] == " " and random.randint(0, 99) < OUTSIDE_DECORATION_PCT:
                mapObjCopy[x][y] = random.choice(list(OUTSIDEDECOMAPPING.keys()))
    return mapObjCopy

def isBlocked(mapObj, gameStateObj, x, y) -> bool:
    # 맵의 (x, y) 위치가 벽이나 별로 막혀 있으면 True를 반환하고 아니면 False를 반환한다.

    if isWall(mapObj, x, y):
        return True
    
    elif x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return True
    
    elif (x, y) in gameStateObj["stars"]:
        return True
    
    return False

def makeMove(mapObj, gameStateObj, playerMoveTo) -> bool:
    # 주어진 맵과 게임 상태에서 플레이어가 해당 방향으로 움직일 수 있는지 검사
    # 움직일 수 있으면 위치를 바꾸고 별을 미는 경우라면 별의 위치도 바꾼다.
    # 만약 움직일 수 없다면 아무것도 하지 않는다.

    # 움직일 수 있다면 True를, 없다면 False를 반환한다.

    # 플레이어 좌표 체크
    playerx, playery = gameStateObj["player"]

    # 편의성
    stars = gameStateObj["stars"]

    # 각 위치로 움직이는 계산을 위해 xOffset, yOffset을 사용
    if playerMoveTo == UP:
        xOffset = 0
        yOffset = -1
    elif playerMoveTo == RIGHT:
        xOffset = 1
        yOffset = 0
    elif playerMoveTo == DOWN:
        xOffset = 0
        yOffset = 1
    elif playerMoveTo == LEFT:
        xOffset = -1
        yOffset = 0
    
    # 플레이어가 해당 방향으로 움직일 수 있는지 검사
    if isWall(mapObj, playerx + xOffset, playery + yOffset):
        return False
    else:
        if (playerx + xOffset, playery + yOffset) in stars:
            # 별이 있으면 밀 수 있는지 검사
            if not isBlocked(mapObj, gameStateObj, playerx + (xOffset*2), playery + (yOffset*2)):
                # 별을 움직인다.
                index = stars.index((playerx + xOffset, playery + yOffset))
                stars[index] = (stars[index][0] + xOffset, stars[index][1] + yOffset)
            else:
                return False
        # 플레이어를 움직인다.
        gameStateObj["player"] = (playerx + xOffset, playery + yOffset)
        return True

def startScreen() -> None:
    # 플레이어가 키를 누를 때까지 시작 화면을 보여준다.
    # 반환값이 없다.(None)

    # 타이틀 이미지의 위치
    titleRect = IMAGESDICT["title"].get_rect()
    topCoord = 50
    titleRect.top = topCoord
    titleRect.centerx = HALF_WINWIDTH
    topCoord += titleRect.height

    # 여러 줄을 render하기 위해 리스트 사용
    instructionText = [
        "Push the stars over the marks.",
        "Arrow keys to move, WASD for camera control, P to change character.",
        "Backspace to reset level, Esc to quit",
        "N for next level, B to go back a level"
    ]

    # 전체 윈도우에 바탕색을 칠한다.
    DISPLAYSURF.fill(BGCOLOR)

    # 윈도우에 타이틀 이미지를 그린다.
    DISPLAYSURF.blit(IMAGESDICT["title"], titleRect)

    # 텍스트 위치를 잡아서 그린다.
    for i in range(len(instructionText)):
        instSurf = BASICFONT.render(instructionText[i], True, TEXTCOLOR)
        instRect = instSurf.get_rect()
        topCoord += 10
        instRect.top = topCoord
        instRect.centerx = HALF_WINWIDTH
        topCoord += instRect.height
        DISPLAYSURF.blit(instSurf, instRect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

        pygame.display.update()
        FPSCLOCK.tick()

def readLevelsFile(filename) -> list:
    assert os.path.exists(filename), "Cannot find the level file: %s" % (filename)

    with open(filename, "r") as mapFile:
        content = mapFile.readlines() + ["\r\n"]
    
    levels = [] # 레벨 객체를 담는 리스트
    levelNum = 0
    mapTextLines = [] # 레벨 하나의 맵을 구성하는 텍스트 라인들
    mapObj = [] # mapTextLines의 데이터로 만든 맵 객체
    
    for lineNum in range(len(content)):
        # 레벨 파일의 각 줄에 대해 처리한다.
        line = content[lineNum].rstrip("\r\n")

        if ";" in line:
            line = line[:line.find(";")]
        
        if line != "":
            # 맵 부분
            mapTextLines.append(line)

        elif line == "" and len(mapTextLines) > 0:
            # 레벨 끝
            # 맵에서 가장 긴 가로 열을 찾는다.
            maxWidth = max(list(map(len, mapTextLines)))
            # 맵을 직사각형으로 만든다.
            for i in range(len(mapTextLines)):
                mapTextLines[i] += " " * (maxWidth - len(mapTextLines[i]))
            
            # mapTextLines를 맵 객체로 변환한다.
            for x in range(maxWidth): # 책에는 len(mapTextLines[0])로 되어 있었음 오류시 참고
                mapObj.append([])
            for y in range(len(mapTextLines)):
                for x in range(maxWidth):
                    mapObj[x].append(mapTextLines[y][x])
            # 맵에서 공간에 대해 루프문을 돌면서 시작할 때
            # 게임 상태에 대해 정하기 위해 @, ., $ 문자들을 찾아낸다.
            startx, starty = None, None
            goals = [] # 각 스타 마커의 위치
            stars = [] # 각 별의 시작 위치
            for x in range(maxWidth):
                for y in range(len(mapObj[x])):
                    if mapObj[x][y] in ("@", "+"):
                        # @ : 플레이어, + : 플레이어 + 스타 마커
                        startx, starty = x, y
                    if mapObj[x][y] in (".", "+", "*"):
                        # . : 스타 마커, * : 별 + 스타 마커
                        goals.append((x, y))
                    if mapObj[x][y] in ("$", "*"):
                        # $ : 별
                        stars.append((x, y))
            
            # 기본 레벨 디자인 유효성 검사
            assert startx != None and starty != None, \
            "Level %s (around line %s) in %s is missing a \"@\" or \"+\" to mark the start point." \
            % (levelNum + 1, lineNum, filename)
            
            assert len(goals) > 0, \
            "Level %s (around line %s) in %s must have at least one goal." \
            % (levelNum + 1, lineNum, filename)

            assert len(stars) >= len(goals), \
            "Level %s (around %s) in %s is impossible to solve. It has %s goals but only %s stars." \
            % (levelNum + 1, lineNum, filename, len(goals), len(stars))

            # 레벨 객체를 생성하고 게임 상태 객체를 시작하기
            gameStateObj = {
                "player" : (startx, starty),
                "stepCounter" : 0,
                "stars" : stars
            }
            levelObj = {
                "width" : maxWidth,
                "height" : len(mapObj),
                "mapObj" : mapObj,
                "goals" : goals,
                "startState" : gameStateObj
            }

            levels.append(levelObj)

            # 다음 맵을 위해 변수 재설정
            mapTextLines = []
            mapObj = []
            gameStateObj = {}
            levelNum += 1
    return levels

def floodFill(mapObj, x, y, oldCharacter, newCharacter):
    # 맵 객체상 (x, y) 위치에 있는 oldCharacter를 newCharacter로 바꾸고 
    # 똑같은 동작을 재귀적으로 4방향에 대해 실시한다.

    if mapObj[x][y] == oldCharacter:
        mapObj[x][y] = newCharacter
    
    if x < len(mapObj) - 1 and mapObj[x+1][y] == oldCharacter:
        floodFill(mapObj, x+1, y, oldCharacter, newCharacter)
    if x > 0 and mapObj[x-1][y] == oldCharacter:
        floodFill(mapObj, x-1, y, oldCharacter, newCharacter)
    if y < len(mapObj[x]) - 1 and mapObj[x][y+1] == oldCharacter:
        floodFill(mapObj, x, y+1, oldCharacter, newCharacter)
    if y > 0 and mapObj[x][y-1] == oldCharacter:
        floodFill(mapObj, x, y-1, oldCharacter, newCharacter)

def drawMap(mapObj, gameStateObj, goals) -> pygame.Surface:
    # 플레이어와 별을 포함한 맵을 surface에 그린다.
    # 이 함수는 루프문이 아니며 따라서 update를 호출하지 않는다.
    
    # 구석의 level과 steps 텍스트로 그리지 않는다는 건 소리야

    # 이 함수의 리턴을 받을 mapSurf는 Surface 객체이며 타일을 그린다.
    # 전체 맵을 하나의 surface로 받아 위치 조정을 쉽게 한다.
    mapSurfWidth = len(mapObj) * TILEWIDTH
    mapSurfHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill((BGCOLOR))

    # 타일 스프라이트를 그린다.
    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            
            if mapObj[x][y] in TILEMAPPING:
                baseTile = TILEMAPPING[mapObj[x][y]]
            elif mapObj[x][y] in OUTSIDEDECOMAPPING:
                baseTile = TILEMAPPING[" "]
            
            mapSurf.blit(baseTile, spaceRect)
            if mapObj[x][y] in OUTSIDEDECOMAPPING:
                mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)
            elif (x, y) in gameStateObj["stars"]:
                if (x, y) in goals:
                    mapSurf.blit(IMAGESDICT["covered goal"], spaceRect)
                mapSurf.blit(IMAGESDICT["star"], spaceRect)
            elif (x, y) in goals:
                mapSurf.blit(IMAGESDICT["uncovered goal"], spaceRect)

            # 플레이어를 그린다.
            if (x, y) == gameStateObj["player"]:
                # 주의 : currentImage는 Playerimage 상수의 인덱스 키를 가지고 있다.
                mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)
    return mapSurf

def isLevelFinished(levelObj, gameStateObj) -> bool:
    # 모든 스타 마커 위에 별이 있으면 True를 반환한다.
    for goal in levelObj["goals"]:
        if goal not in gameStateObj["stars"]:
            # 별이 없는 스타 마커가 있으면
            return False
    return True

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()