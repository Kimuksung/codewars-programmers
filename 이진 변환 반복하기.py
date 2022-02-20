def binary_change( s ) :
    zero_cnt = 0
    one_cnt = 0
    for i in s :
        if i == '0' :
            zero_cnt += 1
        else :
            one_cnt += 1
            
    return bin ( one_cnt )[2:] , zero_cnt

def solution(s):
    answer = 0
    zero_cnt = 0
    
    while ( s != '1' ) :
        s , cnt = binary_change ( s )
        zero_cnt += cnt
        answer += 1
        
    return [answer , zero_cnt ]