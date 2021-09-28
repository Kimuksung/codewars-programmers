def solution( data ):
    n = len(str(data))
    answer = 0
    for i in range(n):
        answer += int ( data[i] )
    
    return answer , data[0]

def order_weight(strng):
    # your code
    if strng == '' :
        return ''
    strng = strng.split(' ')
    return ' '.join ( sorted(strng , key = lambda x : solution(x) ) )

print ( order_weight( '2000 11 11 10003 22 123 1234000 44444444 9999' ))