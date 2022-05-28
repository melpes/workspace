def solution(n, lost, reserve):
    answer = 0
    check_lost = []
    check_reserve = []
    
    # 도난당한 사람 중 옷 빌린 사람들 체크용 배열.
    # 0이면 옷 없고 1이면 옷 빌림
    for _ in range(len(lost)):
        check_lost.append(0)
        
    # 여복 있는 사람 중 옷 빌려주거나 자신도 도난당했는지 체크용 배열
    # 0이면 여복 있고 1이면 여복 없음
    for _ in range(len(reserve)):
        check_reserve.append(0)
        
    
    # 도난 당하지 않은 학생들 수업 참가 표시
    answer += n - len(lost)

    #여벌 있는데 도난당한 인원 도난, 여복 표시 후 수업 참가 표시
    for L_index in range(len(lost)):
        if ( lost[L_index] in reserve):
            R_index = reserve.index(lost[L_index])
            
            check_lost[L_index] = 1
            check_reserve[R_index] = 1
            answer += 1

    # 도난당한 사람들 중 못 빌린 사람들 탐색
    for L_index in range(len(check_lost)):
        if check_lost[L_index] == 1:
            continue
        
        # 해당 사람 번호 앞뒤로 여벌 있고 표식 없는 사람 탐색 후 처리
        if (lost[L_index]+1 in reserve):
            R_index = reserve.index(lost[L_index]+1)
            
            if (check_reserve[R_index] == 1):
                continue

            check_lost[L_index] = 1
            check_reserve[R_index] = 1
            answer += 1
                
        elif (lost[L_index]-1 in reserve):
            R_index = reserve.index(lost[L_index]-1)
            
            if (check_reserve[R_index] == 1):
                continue
                
            check_lost[L_index] = 1
            check_reserve[R_index] = 1
            answer += 1
    
    
            
    return answer