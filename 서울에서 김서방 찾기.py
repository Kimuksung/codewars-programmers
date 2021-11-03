def solution(seoul):
    n = 0
    
    for data in seoul :
        if data == 'Kim' :
            break
        n += 1
        
    answer = '김서방은 ' + str(n) + '에 있다' 
    
    return answer