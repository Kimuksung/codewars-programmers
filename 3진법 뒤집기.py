
def solution(n):
    answer = 0
    
    #3진법
    three_zinbub = ''
    while n >= 3 :
        three_zinbub = ( str( int (n % 3 ) ) ) + three_zinbub
        n = n / 3
    three_zinbub = ( str( int (n % 3 ) ) ) + three_zinbub

    # 문자열 -> 진법 int 형
    # int(three_zinbub, 3)

    #거꾸로
    for index , value in enumerate ( three_zinbub ) :
        answer += 3**(index) * int(value)

        
    return answer

print ( solution(45) ) 