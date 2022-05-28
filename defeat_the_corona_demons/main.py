# 모듈 임포트
import pygame, copy, sys, abc, os, math
from pygame.locals import *

# fps 상수값 설정
FPS = 60

# 프로그램 윈도우의 너비, 높이 [픽셀]
WINWIDTH, WINHEIGHT = 1400, 800

# 윈도우 너비, 높이의 절반
HALF_WINWIDTH, HALF_WINHEIGHT = int(WINWIDTH / 2), int(WINHEIGHT / 2)

# 맵을 구성하는 타일 각각의 너비, 높이, 바닥부분 높이 [픽셀]
TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 40

# 색 종류
BGCOLOR = (31, 30, 51)
TEXTCOLOR = (255, 255, 255)

# 자주 쓰는 문자열 상수화
Q = 'Q'
A = 'A'
S = 'S'

def main() -> None:
    
    # 전역 변수와 상수 지정
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, BASICFONT, SKILLFONT, CHARACTERIMAGES, bullet_list_player, bullet_list_mob, bullet_list_exploded, BLACK, WHITE

    # pygame 초기화
    pygame.init()
    
    # FPSCLOCK 설정
    FPSCLOCK = pygame.time.Clock()
    
    # 배경 surface 구현
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    
    # 윈도우 제목
    pygame.display.set_caption("Defeat The Corona Demons")
    
    # 기본 폰트와 크기 지정
    BASICFONT = pygame.font.Font("freesansbold.ttf", 18)
    SKILLFONT = pygame.font.Font("freesansbold.ttf", 40)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    

    # 모든 기본 이미지 surface 객체를 저장하는 전역 dict
    IMAGESDICT = {
        "wall" : pygame.image.load("defeat_the_corona_demons/images/wall.png"),
        "corner" : pygame.image.load("defeat_the_corona_demons/images/corner.png"),
        "floor" : pygame.image.load("defeat_the_corona_demons/images/floor.png"),
        "grass" : pygame.image.load("defeat_the_corona_demons/images/grass.png"),
        "rock" : pygame.image.load("defeat_the_corona_demons/images/rock.png"),
        "short tree" : pygame.image.load("defeat_the_corona_demons/images/short_tree.png"),
        "tall tree" : pygame.image.load("defeat_the_corona_demons/images/tall_tree.png"),
        "bush" : pygame.image.load("defeat_the_corona_demons/images/bush.png"),
        # 출처 https://pixabay.com/vectors/devil-satan-demon-horns-mask-evil-311310/
        "small golem" : pygame.image.load("defeat_the_corona_demons/images/small_golem.png"),
        # 출처 https://pixabay.com/vectors/demon-devil-face-halloween-head-1296505/
        "big golem" : pygame.image.load("defeat_the_corona_demons/images/big_golem.png"),
        # 출처 https://pixabay.com/vectors/skull-wings-horns-devil-death-5996957/
        "spirit" : pygame.image.load("defeat_the_corona_demons/images/spirit.png"),
        # 출처 https://www.crowdpic.net/photos/%EB%A7%88%EC%8A%A4%ED%81%AC%EB%A5%BC%EC%8D%A8%EC%A3%BC%EC%84%B8%EC%9A%94
        "player" : pygame.image.load("defeat_the_corona_demons/images/player.png"),
        "dummy" : pygame.image.load("defeat_the_corona_demons/images/dummy.png"),
        "damaged" : pygame.image.load("defeat_the_corona_demons/images/damaged.png"),
        # 출처 https://www.sciencetimes.co.kr/news/%EC%BD%94%EB%A1%9C%EB%82%9819-%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4%EB%8A%94-%EC%A7%84%ED%99%94%EC%9D%98-%EC%82%B0%EB%AC%BC/
        "bullet" : pygame.image.load("defeat_the_corona_demons/images/mob_bullet.png"),
        # 출처 https://key0.cc/ko/108880-%EC%8B%9C%EB%A6%B0%EC%A7%80-%ED%8E%91-%ED%88%AC%EB%AA%85-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%8B%9C%EB%A6%B0%EC%A7%80
        "bullet_player" : pygame.image.load("defeat_the_corona_demons/images/bullet.png"),
        "start screen" : pygame.image.load("defeat_the_corona_demons/images/start_screen.PNG")
    }
    
    # 맵 파일의 문자들에 대응되는 이미지 정보를 저장하는 전역 dict
    TILEMAPPING = {
        '#' : IMAGESDICT["wall"],
        '+' : IMAGESDICT['corner'],
        ' ' : IMAGESDICT["floor"],
        'w' : IMAGESDICT["grass"],
        'r' : IMAGESDICT["rock"],
        't' : IMAGESDICT["short tree"],
        'T' : IMAGESDICT["tall tree"],
        'b' : IMAGESDICT["bush"]
    }
    
    # 캐릭터 리스트(플레이어와 적 캐릭터)
    CHARACTERIMAGES = {
        "player" : IMAGESDICT["player"],
        "small golem" : IMAGESDICT["small golem"],
        "big golem" : IMAGESDICT["big golem"],
        "spirit" : IMAGESDICT["spirit"]
    }
    # 현재 사용되어 사라지지 않은 총알들 리스트
    bullet_list_mob = []
    bullet_list_player = []
    bullet_list_exploded = []

    # 플레이어가 아무 키를 누를 때까지 시작 화면을 보여준다.
    i = True
    while i:
        i = show_start_screen()

    # 텍스트 파일에서 레벨을 읽어 온다.
    map_file : str = "defeat_the_corona_demons/map.txt"
    levels : list = read_levels_file(map_file)

    current_level_index : int = 0

    # 메인 게임 루프. 스테이지를 종료할 때마다 반복된다.
    while True:
        
        # 스테이지 선택 화면을 불러온다.
        # 화면에는 전체 스테이지 개수와 진행 가능한 최고 스테이지가 표시되며
        # 맞는 스테이지 번호를 입력하면 해당 숫자를 반환하여 인덱스에 저장한다.

        # 스테이지를 마치면 클리어 여부와 재시작 등에 따라 int가 반환된다.
        # 실패 : 0, 클리어 : 1, 재시작 : 2, 이전 맵 : 3
        result = run_level(levels, current_level_index)

        # 스테이지 재시작 때마다 총알 초기화
        bullet_list_mob = []
        bullet_list_player = []
        bullet_list_exploded = []

        # result 에 따라 스테이지 인덱스 갱신
        if result == 0:
            print("실패")
        elif result == 1:
            print("클리어")
            current_level_index += 1
            if current_level_index >= len(levels):
                current_level_index = 0
        elif result == 2:
            print("재시작")
        elif result == 3:
            print("이전 맵")
            current_level_index -= 1
            if current_level_index < 0:
                current_level_index = len(levels) - 1
        elif result == 4:
            print("다음 맵")
            current_level_index += 1
            if current_level_index >= len(levels):
                current_level_index = 0
    
# 시작 화면 그리기
def show_start_screen() -> bool:
    image = IMAGESDICT["start screen"]
    image_rect = image.get_rect()
    image_rect.topleft = 0, 0
    
    DISPLAYSURF.fill(BGCOLOR)

    DISPLAYSURF.blit(image, image_rect)

    pygame.display.update()
    
    # 임의의 버튼을 누르면 False를 반환
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            return False

    return True
    

# 스테이지 플레이
def run_level(levels : list, current_level_index : int) -> int:
    global map_width_global, map_height_global
    # 선택한 스테이지의 레벨 불러오기
    level_obj : dict = levels[current_level_index]
    
    # 스테이지의 맵 정보를 가공하여 맵 요소 이외의 것을 제거
    map_obj : list = processing_map(level_obj["map_obj"])

    map_width_global, map_height_global = len(map_obj) * TILEWIDTH, (len(map_obj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT

    # 스테이지 정보를 훼손하지 않고 여러 변동 정보(플레이어 위치 등)를
    # 다루기 위해 deepcopy
    game_state_obj = copy.deepcopy(level_obj["start_state"])

    # 몬스터 인스턴스 생성
    player = Player(game_state_obj["player"])
    mobs = []
    for mob in game_state_obj["mobs"]:
        if mob[0] == "g":
            mobs.append(SmallGolem(mob[1]))
        elif mob[0] == "G":
            mobs.append(BigGolem(mob[1]))
        elif mob[0] == "s":
            mobs.append(Spirit(mob[1]))

    # 마우스 좌표 변수
    mouse_pos : tuple = None
    mouse_bt3 : bool = False

    # while문 최초로 마우스가 입력되기 전에 ploc 사용하기 위한 정의
    ploc = game_state_obj["player"]
    # while문 틱 전에 dt 사용하기 위한 정의
    dt : float = 1 / FPS
    # a버튼이 눌렸는지 검사하는 변수
    key_a = False

    # 메인 게임 루프
    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == QUIT:
                # 종료 함수
                terminate()
            else:
                # 키 입력에 대한 대응 설정
                if event.type == MOUSEBUTTONDOWN:
                    # 우클릭이 눌리면 체크
                    if event.button == 3:
                        mouse_bt3 = True
                        mouse_pos = event.pos
                if event.type == MOUSEMOTION:
                    # 화면 상 마우스 위치 체크
                    if mouse_bt3:
                        mouse_pos = event.pos
                if event.type == MOUSEBUTTONUP:
                    # 우클릭을 떼었는지 체크
                    if event.button == 3:
                        mouse_bt3 = False
                if event.type == KEYDOWN:
                    # q스킬 사용
                    if event.key == K_q:
                        player.a_skill()
                    # a버튼 눌렸는지 검사
                    if event.key == K_a:
                        key_a = True
                    # s버튼 누르면 플레이어 정지
                    if event.key == K_s:
                        mouse_pos = None
                    # esc를 누르면 해당 스테이지 재시작
                    if event.key == K_ESCAPE:
                        return 2
                    # 왼쪽 방향키를 누르면 이전 스테이지로
                    if event.key == K_LEFT:
                        return 3
                    # 오른쪽 방향키를 누르면 다음 스테이지로
                    if event.key == K_RIGHT:
                        return 4
                if event.type == KEYUP:
                    # a버튼 떼었는지 검사
                    if event.key == K_a:
                        key_a = False

        # a버튼이 눌리면 플레이어 기본 공격
        if key_a:
            player.basic_attack(mouse_location)

        # 플레이어 평타 대기시간 측정
        player.tick(dt)

        # 이벤트에서 측정한 마우스 좌표는 화면 상 좌표이므로 이를 맵 상 좌표로 변환해야 함.
        # 맵 상 좌표로 변환하는 계산
        mouse_location = tuple(\
              pygame.Vector2(player.location)\
            + pygame.Vector2(pygame.mouse.get_pos())\
            - pygame.Vector2(HALF_WINWIDTH, HALF_WINHEIGHT))
    
        # 유닛의 damaged 초기화(하지 않으면 피격 이펙트가 꺼지지 않음)
        player.damaged = False
        for mob in mobs:
            mob.damaged = False

        # 마우스 좌표가 입력되면 대응하는 맵의 좌표로 변환한 뒤 플레이어를 이동
        if mouse_pos:
            # 플레이어를 이동시켜보고 이동할 수 있다면 이동
            dir_pos = tuple(pygame.Vector2(ploc) + pygame.Vector2(mouse_pos) - pygame.Vector2(HALF_WINWIDTH, HALF_WINHEIGHT))
            player.make_move(map_obj, dir_pos, dt)
            if mouse_bt3:
                # mouse_bt3 == False인 경우 ploc의 갱신이 중단되어 마지막 터치 지점에 가서 멈추게 된다.
                ploc = Player.location

        # 몹 이동
        for i in range(len(mobs)):
            # 몹이 생성되고 죽는 과정에서 인덱스 오류를 방지하기 위한 try 문
            try:
                mobs[i].make_move(map_obj, dt, player)
                if mobs[i].hp == 0:
                    del mobs[i]
            except:
                pass

        # 총알 이동
        for i in range(len(bullet_list_mob)):
            try:
                if bullet_list_mob[i].live:
                    bullet_list_mob[i].move(dt)
                else:
                    del bullet_list_mob[i]
            except:
                pass
        for i in range(len(bullet_list_player)):
            try:
                if bullet_list_player[i].live:
                    bullet_list_player[i].move(dt)
                else:
                    del bullet_list_player[i]
            except:
                pass
        for i in range(len(bullet_list_exploded)):
            try:
                if bullet_list_exploded[i].live:
                    bullet_list_exploded[i].move(dt)
                else:
                    del bullet_list_exploded[i]
            except:
                pass
        
        # 플레이어가 죽으면 실패
        if not player.is_alive:
            return 0
        # 몹이 전부 죽으면 클리어
        if not mobs:
            return 1

        # 배경색 칠하기
        DISPLAYSURF.fill(BGCOLOR)

        # draw_map으로 그릴 surface를 받는다.
        map_surf : pygame.Surface = draw_map(map_obj, player, mobs)
        map_surf_rect : pygame.Rect = map_surf.get_rect()

        # 스킬 켜졌는지 표기 (map_surf 바깥에 그려야 해서 따로 분리)
        if player._is_q_on:
            q_text = SKILLFONT.render("Q", True, WHITE)
        else: 
            q_text = SKILLFONT.render("Q", True, (100, 100, 100))
        q_text_rect = q_text.get_rect()
        q_text_rect.center = HALF_WINWIDTH - 100, WINHEIGHT - 100

        # 맵 가로, 세로 길이 [픽셀] (map_surf 위치 계산용)
        map_width, map_height = len(map_obj) * TILEWIDTH / 2, ((len(map_obj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT) / 2
        map_center = tuple(pygame.Vector2(map_width, map_height) + pygame.Vector2(HALF_WINWIDTH, HALF_WINHEIGHT) - pygame.Vector2(Player.location))
        map_surf_rect.center = map_center
        DISPLAYSURF.blit(map_surf, map_surf_rect)

        # 스킬 표시를 가장 위에 표시
        DISPLAYSURF.blit(q_text, q_text_rect)
        
        # 현재 맵 번호 표시
        map_num = SKILLFONT.render(f"{current_level_index+1} STAGE", True, WHITE)
        map_num_rect = map_num.get_rect()
        map_num_rect.center = 100, 100
        DISPLAYSURF.blit(map_num, map_num_rect)

        pygame.display.update()
        dt : float = FPSCLOCK.tick(FPS)
        print(FPSCLOCK.get_fps()) # 실시간으로 현재 프레임 상태 측정

# read_levels_file과 run_level 함수 기본적인 방식은 python과 pygame으로 게임만들기의 Star Pusher 부분을 참고
# 링크 http://www.yes24.com/Product/Goods/13709740
# 구글에 star pusher 라 검색해도 비슷한 내용이 나옴
def read_levels_file(mapfile) -> list:
    # 파일이 없을 경우 예외 발생
    assert os.path.exists(mapfile), f"Cannot find the level file : {mapfile}"

    # 파일을 열어 내용을 content에 저장
    with open(mapfile, 'rt', encoding='UTF8') as map_file:
        content = map_file.readlines() + ["\n"]

    levels = []
    map_text_lines = []
    map_obj = []
    level_num = 0

    # content의 각 줄에 대해 처리
    for line in content:
        line = line.rstrip("\n")

        if ";" in line: # ;이후의 것은 무시
            line = line[:line.find(";")]
        
        if line != "": # 빈칸이 아니면 map_text_lines에 추가
            map_text_lines.append(line)

        # map_text_lines에 내용이 있으면서 빈칸이 나오면 맵 가공
        elif len(map_text_lines) > 0:
            # 직사각형이 되게 맵 빈칸을 채운다.
            max_width = max(map(len, map_text_lines))
            for i in range(len(map_text_lines)):
                map_text_lines[i] += " " * (max_width - len(map_text_lines[i]))

            # map_text_lines를 맵 객체로 변환
            # 맵 객체는 (x, y) 좌표의 블록이 map_obj[x][y]에 존재하도록 처리 
            for _ in range(max_width):
                map_obj.append([])
            for y in range(len(map_text_lines)):
                for x in range(max_width):
                    # assert mapTextLines[y][x] in TILEMAPPING,\
                    # f"Level {levelnum+1} in {filename} has a strange word : {mapTextLines[y][x]}"
                    map_obj[x].append(map_text_lines[y][x])

            # 맵 속에 있는 특정 문자들을 찾아 start_state에 저장한다.
            # 해당 문자들은 플레이어와 몹의 시작 위치를 나타낸다.
            player_pos = None
            mobname_nobpos = []

            for x in range(max_width):
                for y in range(len(map_obj[x])):
                    if map_obj[x][y] == "@":
                        player_pos = (x + 0.5) * TILEWIDTH, (y - 1) * TILEFLOORHEIGHT + TILEHEIGHT
                    if map_obj[x][y] in ["g", "G", "s"]:
                        mobname_nobpos.append((map_obj[x][y], ((x + 0.5) * TILEWIDTH, (y - 1) * TILEFLOORHEIGHT + TILEHEIGHT)))


            # 레벨 디자인 유효성 검사
            assert player_pos != None, \
            f"Level {level_num + 1} in {mapfile} is missing a \"@\" to mark the start point"

            assert mobname_nobpos != None, \
            f"Level {level_num + 1} in {mapfile} is missing \"g\" or \"G\" or \"s\" to mark the mobs"

            # 레벨 객체 생성
            game_state_obj = {
                "player" : player_pos,
                "mobs" : mobname_nobpos
            }
            level_obj = {
                "map_obj" : map_obj,
                "start_state" : game_state_obj
            }
            levels.append(level_obj)

            # 다음 맵을 위한 변수 초기화
            map_text_lines = []
            map_obj = []
            game_state_obj = {}
            level_num += 1

    return levels

# 유닛의 위치 정보를 기록하고 해당 위치를 일반 블럭으로 바꿈
def processing_map(map_obj : list) -> list:
    map_obj_copy = copy.deepcopy(map_obj)

    for x in range(len(map_obj_copy)):
        for y in range(len(map_obj_copy[x])):
            if map_obj_copy[x][y] in ['@', 'g', 'G', 's']:
                map_obj_copy[x][y] = ' '
    return map_obj_copy

# 해당 좌표가 벽인지 확인해줌
def is_wall(map_obj, xpos, ypos) -> bool:
    # x, y 좌표를 각각 블록 한 칸의 가로, 세로 길이로 나누고 반올림하면
    # 해당 좌표에 존재하는 블록의 map_obj 상 좌표가 된다.
    x, y = int(xpos / TILEWIDTH), int(ypos / TILEFLOORHEIGHT)
    # 만약 해당 좌표가 맵 바깥이면 False
    if x < 0 or x >= len(map_obj) or y < 0 or y >= len(map_obj[x]):
        return False
    # 만약 해당 좌표에 wall corner, rock이 있으면 True
    elif map_obj[x][y] in ['#', '+', 'r']:
        return True

# 총알 클래스
class Bullet:
    # 총알 생성 위치와 발사 방향을 매개변수로 받는다.
    def __init__(self, pos, dir_pos) -> None:
        self.bulletspeed = 0.2  # 총알의 이동 속도
        self.live = True        # False가 되면 총알 인스턴스를 삭제한다.

        # dir_pos가 None으로 대입되는 경우가 있어 그런 경우 아래쪽 방향으로 고정시킨다.
        # 아닌 경우 생성 위치에 대해 이동 방향의 위치벡터를 구한다.
        try: 
            self.offset = pygame.Vector2(dir_pos[0], dir_pos[1]) -  pygame.Vector2(pos[0], pos[1])
        except:
            self.offset = pygame.Vector2(0, 1)
            
        # 위치벡터의 길이를 총알의 속도로 한다.
        self.offset.scale_to_length(self.bulletspeed)
        self.location = pos + self.offset * 5 # 5는 보정값

    # 매 프레임 총알을 이동시킴
    def move(self, dt):
        # 프레임이 떨어질 경우를 대비해 위치벡터에 dt 곱하기
        self.location += self.offset[0] * dt, self.offset[1] * dt

        # 총알이 맵 바깥으로 이동하면 삭제시키기
        if self.location[0] < 0 or self.location[0] > map_width_global:
            self.live = False
        elif self.location[1] < 0 or self.location[1] > map_height_global:
            self.live = False

    # 바이러스 총알 그리기
    def blit(self, surface : pygame.Surface) -> None:
        bullet = IMAGESDICT["bullet"]
        bullet_rect = bullet.get_rect()
        bullet_rect.center = self.location
        surface.blit(bullet, bullet_rect)

    # 백신 총알 그리기    
    def blit_player(self, surface : pygame.Surface) -> None:
        bullet = IMAGESDICT["bullet_player"]
        bullet_rect = bullet.get_rect()
        bullet_rect.center = self.location
        surface.blit(bullet, bullet_rect)

# 모든 유닛의 부모 클래스
# 유닛의 대부분의 기능이 담겨 있다.
class Character(metaclass = abc.ABCMeta):
    pos_tolerance : int or float = 10
    def __init__(self, pos : tuple) -> None:
        # Character 클래스는 추상 클래스로 인스턴스를 만들 수 없다.
        # 모든 유닛들이 상속받아 사용한다.
        # 형식을 표기하고 극단값으로 정의한 프로퍼티들은 상속받은 클래스에서 재정의해야 한다.
        self._hp : int = 1e10               # 체력. 0 이하가 되면 사망하여 인스턴스가 삭제된다.
        self._attack_damage : int = 0       # 기본공격 데미지
        self._attack_speed : float = 1e-2   # 초당 기본공격 횟수
        self._attack_range : int = 0        # 기본공격 사거리
        self._is_alive = True               # 살아있는지 확인하는 변수
        self._character_image : pygame.image = IMAGESDICT["dummy"] # 해당 캐릭터의 이미지
        self._location : tuple = pos        # 해당 인스턴스의 위치
        self._moving_speed : float = 0      # 이동 속도
        self._damaged : bool = False        # 피격당했는지 확인하는 변수. 피격 이펙트를 띄우기 위함이다.
        self._tick : float = 0              # 공격 간 딜레이를 체크하는 변수

    # 체력 getter
    @property
    def hp(self):
        return self._hp
    
    # 체력 setter
    # 0 이하가 대입되면 0으로 고정하고 _is_alive에 False를 대입한다.
    @hp.setter
    def hp(self, hp):
        if hp <= 0:
            self._hp = 0
            self._is_alive = False
            print(type(self), "가 사망하였습니다.")
        else:
            self._hp = hp

    # _is_alive getter
    @property
    def is_alive(self):
        return self._is_alive

    # 피격 여부 getter
    @property
    def damaged(self):
        return self._damaged

    # 피격 여부 setter
    @damaged.setter
    def damaged(self, damaged : bool):
        self._damaged = damaged

    # 위치 getter
    @property
    def location(self):
        return self._location

    # 프레임마다 캐릭터 움직임 처리.
    # 추상 메소드로 하위 클래스에서 오버라이딩 필수
    # 몹 클래스에서는 오버라이딩하여 플레이어 추적하는 기능을 추가할 것.
    @abc.abstractmethod
    def make_move(self, map_obj : list, dir_pos : tuple, dt : float) -> None:
        pos = pygame.Vector2(self._location)
        dir = pygame.Vector2(dir_pos)
        offset = dir - pos

        # Character.pos_tolerance : offset의 크기가 일정 수준 이하일때 0으로 취급하지 않으면 목표 좌표에 도착하고
        # 진동하는 모습을 보인다. 따라서 이를 완화하기 위해 추가했다.
        if offset.length() <= Character.pos_tolerance:
            offset = (0, 0)
        # 프레임 변화에도 일정한 속도를 유지하기 위해 속도에 dt(프레임 사이의 시간 차이)를 곱한다.
        # pygame의 경우 맵의 크기가 커질수록 프레임이 떨어지기 때문에 맵 간 이동속도 차이가 날 수 있어 이런 조치를 했다.
        else:
            offset.scale_to_length(self._moving_speed * dt)

        # 이동할 좌표가 벽에 해당하는지 확인
        if is_wall(map_obj, pos[0] + offset[0], pos[1] + offset[1]):
            return

        # 위 조건을 모두 만족하면 자신의 위치를 변경한다.
        self._location = tuple(pos + offset)
    
    # 기본 공격 메소드
    @abc.abstractmethod
    # 현재 프레임의 dt를 받아 tick에 더한 뒤 반환한다.
    # 이후 반환한 tick을 다음 프레임에 다시 받아 dt를 더한다.
    # 이 과정이 반복되다가 충분한 시간이 지날 경우 기본 공격 인스턴스를 생성한다.
    def basic_attack(self, dir, tick, dt) -> float:
        self._tick = tick
        self._tick += dt
        if self._tick >= 1e3 / self._attack_speed:
            self._tick = 0
            bullet_list_mob.append(Bullet(self._location, dir))
        return self._tick

    # 피격 이펙트 그리기
    def blit_damaged(self, surface, rect):
        surface.blit(IMAGESDICT["damaged"], rect)

    # 스킬 메서드
    @abc.abstractmethod
    def a_skill(self, surface, theta, skill_range, skill_dtspeed):
        pass

    # 캐릭터 그리기
    def blit_character(self, surface : pygame.Surface) -> None:
        character_image_rect = self._character_image.get_rect()
        character_image_rect.center = self._location
        surface.blit(self._character_image, character_image_rect)

    # 체력 표시하기
    def blit_hp(self, surface : pygame.Surface) -> None:
        hp_text = BASICFONT.render(f"{self._hp}", True, BLACK)
        hp_text_rect = hp_text.get_rect()
        hp_text_rect.center = (self._location[0], self._location[1] - 40)
        surface.blit(hp_text, hp_text_rect)

# 플레이어 클래스
class Player(Character):
    # 플레이어는 하나만 존재하며 그 위치는 모든 몹에게 공개되어야 하므로
    # 정적 변수로 location을 만들어 매 순간 인스턴스의 위치 값을 동기화하도록 했다. 
    location : tuple = (0, 0) 
    def __init__(self, pos) -> None:
        super().__init__(pos)
        self._hp = 500
        self._attack_damage = 60
        self._attack_speed = 2.5
        self._attack_range = 200
        self._character_image = CHARACTERIMAGES["player"]
        self._moving_speed = 0.1
        self._is_q_on = False
        # 매개변수로 플레이어를 주지 않아도 플레이어의 위치를 알도록 정적 변수에 동기화. 
        Player.location = self._location

    # 공격 딜레이를 측정하는 tick 변수를 매 프레임마다 프레임 간의 시간 차이만큼 늘린다.
    def tick(self, dt):
        self._tick += dt

    # 기본 공격은 1초에 self._attack_speed의 값만큼 이루어지므로
    # self._tick으로 공격이 가능한지 시간을 측정한다.
    def basic_attack(self, dir) -> float:
        # 기본공격간 딜레이는 1/초당 공격횟수 이고 틱의 단위는 ms이므로 1000을 곱한다. 
        if self._tick >= 1e3 / self._attack_speed:
            self._tick = 0
            bullet_list_player.append(Bullet(self._location, dir)) # 탄 발사

    # 플레이어가 공격 키를 눌렀을때 반응
    def a_click(self):
        self.ready_to_attack = True
    
    # 상위 클래스 Character의 이동 함수를 그대로 쓰되 오버라이딩해서 플레이어 위치를 정적 변수에 연동
    def make_move(self, map_obj: list, dir_pos: tuple, dt: float) -> tuple:
        super().make_move(map_obj, dir_pos, dt)
        Player.location = self._location

    # Q 스킬
    # 발동하면 공격 속도가 느려지는 대신 데미지가 증가하고
    # 다시 누르면 해제된다.
    def a_skill(self) -> None:
        if self._is_q_on:
            self._attack_speed /= 0.5
            self._attack_damage /= 3
            self._is_q_on = False
        else:
            self._attack_speed *= 0.5
            self._attack_damage *= 3
            self._is_q_on = True

# 적 클래스. 세 종류 몬스터 클래스의 상위 클래스다.
# 매 프레임마다 자동으로 플레이어에게 다가간다.
class Enemy(Character):
    def __init__(self, pos) -> None:
        super().__init__(pos)

    def basic_attack(self, dir, tick, dt) -> float:
        return super().basic_attack(dir, tick, dt)
    
    # 플레이어에게 다가가는 AI 설정
    def make_move(self, map_obj : list, dt : float, player) -> None:
        
        dir_pos = Player.location
        pos = pygame.Vector2(self._location)
        dir = pygame.Vector2(dir_pos)
        offset = dir - pos # 해당 몹 위치를 기준으로 플레이어 위치벡터

        # Character.pos_tolerance : offset의 크기가 일정 수준 이하일때 0으로 취급하지 않으면 목표 좌표에 도착하고
        # 진동하는 모습을 보인다. 따라서 이를 완화하기 위해 추가했다.
        if offset.length() <= Character.pos_tolerance:
            offset = (0, 0)
        # 몬스터의 경우 사거리 내에 플레이어가 존재하면 더 이상 이동하지 않고 공격한다.
        elif offset.length() <= self._attack_range:
            offset = (0, 0)
            self._tick = self.basic_attack(player.location, self._tick, dt)
        # 프레임 변화에도 일정한 속도를 유지하기 위해 속도에 dt(프레임 사이의 시간 차이)를 곱한다.
        # pygame의 경우 맵의 크기가 커질수록 프레임이 떨어지기 때문에 맵 간 이동속도 차이가 날 수 있어 이런 조치를 했다.
        else:
            offset.scale_to_length(self._moving_speed * dt)

        # 이동할 좌표가 벽에 해당하는지 확인
        if is_wall(map_obj, pos[0] + offset[0], pos[1] + offset[1]):
            return

        # 위 조건을 모두 만족하면 자신의 위치를 변경한다.
        self._location = tuple(pos + offset)
        return

# 근접에서 바이러스를 쏘아낸다.
class SmallGolem(Enemy):
    def __init__(self, pos) -> None:
        super().__init__(pos)
        self._hp = 500
        self._attack_damage = 100
        self._attack_speed = 1.5
        self._attack_range = 50
        self._moving_speed = 0.12
        self._character_image : pygame.image = CHARACTERIMAGES["small golem"]

    def a_skill(self):
        pass

# 근접에서 바이러스를 쏘아낸다.
# SmallGolem과 스펙이 다르다
class BigGolem(Enemy):
    def __init__(self, pos) -> None:
        super().__init__(pos)
        self._hp = 1000
        self._attack_damage = 150
        self._attack_speed = 2.0
        self._attack_range = 75
        self._moving_speed = 0.09
        self._character_image : pygame.image = CHARACTERIMAGES["big golem"]

    def a_skill(self):
        pass

# 원거리에서 바이러스를 쏘아낸다.
class Spirit(Enemy):
    def __init__(self, pos) -> None:
        super().__init__(pos)
        self._hp = 700
        self._attack_damage = 50
        self._attack_speed = 3
        self._attack_range = 500
        self._moving_speed = 0.15
        self._character_image : pygame.image = CHARACTERIMAGES["spirit"]

    def a_skill(self):
        pass

# 게임이 진행되는 surface를 받아서 필요한 요소들 그리기.
# surface의 경우 매개변수로 받아 수정하면 함수 외부에 영향을 미치므로 반환값은 없음
def draw_map(map_obj, player : Player, mobs : list) -> None:
    map_surf_width = len(map_obj) * TILEWIDTH
    map_surf_height = (len(map_obj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT
    map_surf = pygame.Surface((map_surf_width, map_surf_height)) # 맵 픽셀 크기만큼 만들기
    map_surf.fill((BGCOLOR))

    # 맵 구조물들 그리기
    for x in range(len(map_obj)):
        for y in range(len(map_obj[x])):
            space_rect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            base_tile = TILEMAPPING[map_obj[x][y]]
            map_surf.blit(base_tile, space_rect)

    # 플레이어와 몹 그리기
    player.blit_character(map_surf)

    for mob in mobs:
        mob.blit_character(map_surf)

    # 유닛 위에 그려질 수 있도록 부시와 나무들 다시 그리기
    for x in range(len(map_obj)):
        for y in range(len(map_obj[x])):
            if map_obj[x][y] in ['t', 'T', 'b']:
                space_rect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
                base_tile = TILEMAPPING[map_obj[x][y]]
                map_surf.blit(base_tile, space_rect)
    
    # 총알 그리기 및 피격 판정 적용시키기
    # 플레이어의 탄환
    for bullet in bullet_list_player:
        if bullet.live:
            bullet.blit_player(map_surf) # 총알 그리기
            for mob in mobs:
                # 총알과 몹 사이의 거리 측정
                d = math.sqrt((bullet.location[0] - mob.location[0])**2 + (bullet.location[1] - mob.location[1])**2)
                if player._is_q_on: # Q 스킬이 켜져 있을때 피격시 탄환 폭발
                    if d <= 50:
                        bullet.live = False
                        for i in range(30):
                            bullet_list_exploded.append(Bullet(bullet.location, (bullet.location[0] + math.cos(i*math.pi/15), bullet.location[1] + math.sin(i*math.pi/15))))
                elif d <= 25: # q 스킬이 꺼져 있을떄 피격시 데미지
                    mob.damaged = True
                    mob.hp -= int(player._attack_damage)
                    bullet.live = False
    # 몬스터의 탄환
    for bullet in bullet_list_mob:
        if bullet.live:
            bullet.blit(map_surf)
            d = math.sqrt((bullet.location[0] - player.location[0])**2 + (bullet.location[1] - player.location[1])**2)
            if d <= 25:
                player.damaged = True
                player.hp -= 50
                bullet.live = False
    # q스킬에 의해 폭발한 탄환
    # 플레이어의 탄환과 구분한 이유는 구분하지 않을 시 무한하게 탄환이 증식하기 때문
    for bullet in bullet_list_exploded:
        if bullet.live:
            bullet.blit_player(map_surf)
            for mob in mobs:
                d = math.sqrt((bullet.location[0] - mob.location[0])**2 + (bullet.location[1] - mob.location[1])**2)
                if d <= 25:
                    mob.damaged = True
                    mob.hp -= int(player._attack_damage / 10)
                    bullet.live = False


    # 유닛 피격 이펙트 그리기
    rect = IMAGESDICT["damaged"].get_rect()
    if player.damaged:
        rect.center = Player.location
        player.blit_damaged(map_surf, rect)
    
    for mob in mobs:
        if mob.damaged:
            rect.center = mob.location
            mob.blit_damaged(map_surf, rect)

    # 유닛 위에 체력 숫자로 표기
    player.blit_hp(map_surf)
    for mob in mobs:
        mob.blit_hp(map_surf)

    return map_surf

# 종료 함수
def terminate():
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()