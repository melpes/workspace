구성 파일들을 defeat_the_corona_demons 폴더 안에 넣어서 해당 폴더가 workspace 바로 하위 폴더로 있어야 합니다.

workspace에 바로 구성 파일을 흩어서 넣으면 경로 오류가 납니다

그런 경우 IMAGSDICT dict와 read_levels_fle 함수에 존재하는 모든 경로를 수정하면 작동합니다.
기본 값은 "defeat_the_corona_demons/images/파일명" 또는 "defeat_the_corona_demons/파일명" 으로 되어 있음



좌표 방식

map_obj 는 2차원 리스트로 map_obj[x][y]에 해당 블록의 정보가 문자 하나로 들어있다.
따라서 이때는 x, y가 블록단위이다.

이외의 모든 좌표쌍 x, y는 픽셀단위이다.

플레이어는 클래스 Player로 생성된 하나의 인스턴스이다.

level_obj["start_state"] 는 game_object이며
game_object["player"]에는 플레이어 시작 픽셀좌표가 튜플로 존재한다.
이는 플레이어 인스턴스를 만들때 생성자의 매개변수로 들어가며 Player 클래스가 상속받은 Character 클래스의
프로퍼티 self.__location 에 저장된다.이후로 game_object["player"]는 사용되지 않는다.

모든 플레이어 좌표 이동은 프로퍼티 self.__location에 저장되어 있으며
이는 Character 클래스의 추상 메소드 make_move를 상속받아 처리한다.
이 경우 self.__location의 좌표가 변한다.

또한 플레이어는 모든 몹에게 자신의 좌표를 제공해야 하므로
정적 변수 location을 만들어 make_move를 오버라이딩하여 super().make_move
이후 Player.location = self.__location을 추가하여 항상 자신의 좌표를 
정적 변수 location에 갱신한다.