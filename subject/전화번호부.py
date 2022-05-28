data = {}

while True:
    print(f"""\
=======================

현재 데이터 개수: {len(data)}개

1. 전화번호 추가

2. 전화번호 검색

3. 전화번호 삭제

4. 전화번호 전체출력

5. 종료

=======================""")

    while True:
        try:
            ip = int(input("선택 >> "))
            break
        except:
            print("올바른 숫자를 입력하세요")


    if ip == 1:
        name = input("이름 입력 : ")
        number = input("번호 입력 : ")
        data[name] = number

    if ip == 2:
        search_name = input("검색할 이름 입력 : ")
        if search_name in data.keys():
            print(f"""
---------------------

이름 : {search_name}

번호 : {data[search_name]}

---------------------""")
        else:
            print("검색 결과가 없습니다.")
        input("엔터를 누르면 시작 화면으로 돌아갑니다.")
    
    if ip == 3:
        delete_name = input("삭제할 이름 입력 : ")
        if delete_name in data.keys():
            del data[delete_name]
            print("삭제했습니다.")
        else:
            print("해당 이름이 존재하지 않습니다.")
        input("엔터를 누르면 시작 화면으로 돌아갑니다.")
    
    if ip == 4:
        print("---------------------")
        for index, value in data.items():
            print(f"""\

이름 : {index}

번호 : {value}

---------------------\
""")
        input("엔터를 누르면 시작 화면으로 돌아갑니다.")
    if ip == 5:
        print("종료합니다.")
        break