#BOJ 1003번

import sys
input = sys.stdin.readline

def pibonachi( number ) :
    if pibo_list[number] != -1 :
        return pibo_list[number]
    if number == 0 :
        return 0
    elif number == 1 :
        return 1

    pibo_list[number] = pibonachi(number-1) + pibonachi(number-2)
    return pibo_list[number]

k = int( input() )
for _ in range(k) :
    n = int(input())
    pibo_list = [0,1] + [-1] * 39

    pibonachi( n )
    if n == 0 :
        print(1 , 0)
    else:
        print( pibo_list[n-1] , pibo_list[n] )
