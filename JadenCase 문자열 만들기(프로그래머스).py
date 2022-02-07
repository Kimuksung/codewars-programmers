def solution(datas):
    answer = ''
    cnt = 0
    for data in datas :
        #print(data)
        if cnt == 0 and data.isalpha() :
            answer += data.upper()
            cnt += 1
            continue
        if data == ' ' :
            cnt = 0
            answer += ' '
            continue
        cnt += 1
        answer += data.lower()
        
    return answer