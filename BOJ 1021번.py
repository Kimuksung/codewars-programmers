# BOJ 1021번

import sys
from collections import deque
input = sys.stdin.readline

n , m = map( int , input().split() )
number_deque = deque( [i for i in range(1,n+1)] )
targets = deque( map(int, input().split()) )
answer = 0

for target in targets :
    index = number_deque.index( target )
    temp = len(number_deque) - index
    if index < temp :
        answer += index
        for _ in range(index) : #move_left
            number_deque.append( number_deque.popleft() ) 
        
    else :
        answer += temp
        for _ in range( temp ) : #move_right
            number_deque.appendleft( number_deque.pop() )

    number_deque.popleft()

print ( answer )
