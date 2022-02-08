#idea1 = 1의 갯수를 세서 하나씩 올리면서 확인
from collections import Counter

def solution ( n ) :
    N = bin(n).count('1')
    for i in range ( n+1 , 2**20 ) :
        if bin(i).count('1') == N :
            return i

#idea2 = 3진법으로 N자리 수 일때 1의 갯수가 M개인 경우 ( N, M ) -> ( N+1 , M)
'''
from itertools import permutations
def zinbub ( num ) :
    answer = ''
    cnt = 0
    while ( num >= 1) :
        answer = str ( num % 2 ) + answer
        if num % 2  : 
            cnt += 1
        num //= 2
    return len(answer) , cnt

def data ( N , M , num ) :
    datas = ['0'] * (N - M ) + ['1'] * M
    return_data = []
    for check in set ( map ( ''.join , permutations ( datas , N ) )  ) :
        return_data.append ( int ( check , 2 ) )

    return_data = sorted ( return_data )

    return list ( filter ( lambda x : x > num , return_data ) )
    
def solution ( num ) :
    N , M = zinbub(num)
    
    check_data = data(N, M , num)
    if check_data :
        return min(check_data)
    check_data = ( data(N+1, M , num) )

    return min(check_data)
'''
11110100001001000000