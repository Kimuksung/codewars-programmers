def solution(s):
    answer = True
    s = s.lower()
    p_num , y_num = 0 , 0
    
    for value in s :
        if value == 'p' :
            p_num += 1
        elif  value == 'y':
            y_num += 1
           
    return True if p_num == y_num else False