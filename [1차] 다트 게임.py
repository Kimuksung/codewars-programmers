def solution(dartResult):
    answer = 0
    temp = [0,0,0,0]
    cnt = 0
    for data in dartResult :
        print(cnt)
        if data.isdigit():
            temp[cnt+1] = int ( data )
            cnt +=1
        elif data == 'D':
            temp[cnt] = temp[cnt] * temp[cnt]
        elif data == 'T':
            temp[cnt] = temp[cnt] * temp[cnt] * temp[cnt]
        elif data == '*':
            if cnt >= 1:
                temp[cnt-1] = temp[cnt-1]*2
            temp[cnt] = temp[cnt]*2
        elif data == '#':
            temp[cnt] = -1*temp[cnt]
    
    print(temp)
    return answer

solution('1D2S#10S')

#stack으로 푸는거 같음...