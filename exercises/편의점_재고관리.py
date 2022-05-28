class NotInItem(Exception):#구매 희망 대상이 재고 리스트에 없는 경우 예외처리
    pass
class Back(Exception):
    pass

class Manage: #구매 보충 관리 클래스
    def __init__(self, object, number):
        self.object = object
        self.number = number
    def buy(object, number):#구매 함수
        if not(object in object_dict):#물품이 리스트에 없을 때 예외처리
            raise NotInItem
        if number <= 0: #음수 구매를 막음
            raise ValueError
        if object_dict[object] >= number: #재고가 주문량 이상일때 구매처리
            print(f"{object}를 {number} 개 구매")
            object_dict[object] -= number
        else:
            if object_dict[object] != 0: #재고가 주문량보다 적고 0이 아닐 때 전량구매 처리
                over_item_order = input(f"{object}의 재고는 {object_dict[object]} 개"
                " 입니다.\n전부 구매하시겠습니까? (네/아니오)")
                if over_item_order == "네":
                    print(f"{object}를 {object_dict[object]} 개 구매")
                    object_dict[object] = 0
                elif over_item_order == "아니오":
                    print("구매를 취소합니다.")
                    raise Back
                else:
                    print("잘못된 값을 입력하였습니다. 구매가 취소됩니다.")
                    raise Back

            else: #재고가 0일 때
                print("해당 물품의 재고가 없습니다.")

    def supply(object, number):#보충 함수
        if number <= 0:
            raise ValueError #음수 보충을 막음
        if object in object_dict:#물품이 리스트에 존재 시 수량 증가
            print(f"{object}를 {number}개 보충")
            object_dict[object] += number
        else:#물품이 리스트에 존재하지 않을 시 새로 사전값 추가
            print(f"{object}를 {number}개 추가(신규)")
            object_dict[object] = number


object_dict = {} #재고 저장용 사전

#재고 초기값 등록 함수
def first_supply(object, number):
    print(f"{object}(은)는 {number} 개로 설정")
    object_dict[object] = number

#재고를 사전형식이 아닌 효율적으로 보여주기 위해 탭 정렬함. 상품 이름이 8자 이상인 경우 정렬 어긋남
def show_list(dict):
    for key in dict:
        if len(key) >= 4:
            print(f"{key}\t{dict[key]}")
        elif len(key) > 0:
            print(f"{key}\t\t{dict[key]}")

#재고 초기값 등록
first_supply("사이다", 10)
first_supply("김치", 4)
first_supply("닭꼬치", 3)
first_supply("우유", 6)
first_supply("하겐다즈", 12)



while True:
    print("")
    show_list(object_dict)
    menu = input("(구매/보충/종료)")
    if menu == "구매":
        while True:
            try:
                print("구매를 원치 않으시면 물품명에 \"취소\"를 입력해 주십시오.")
                object = input("구매 희망 물품명 : ")
                if object == "취소":
                    print("구매가 취소되었습니다.")
                    break
                number = int(input("구매 희망 개수 : "))
                Manage.buy(object, number)
                break
            except ValueError:
                print("올바른 값을 입력해 주십시오.")
            except NotInItem:
                print("해당 물품은 리스트에 존재하지 않습니다.")
            except Back:
                print("구매창으로 돌아갑니다.")
    elif menu == "보충":
        while True:
            try:
                print("보충을 원치 않으시면 물품명에 \"취소\"를 입력해 주십시오.")
                object = input("보충 요청 물품명 : ")
                if object == "취소":
                    print("보충이 취소되었습니다.")
                    break
                number = int(input("보충 요청 개수 : "))
                Manage.supply(object, number)
                break
            except ValueError:
                print("올바른 값을 입력해 주십시오.")                 
    elif menu == "종료":
        print("종료합니다.")
        break
    else:
        print("정확히 입력해 주십시오.")