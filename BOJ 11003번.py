# BOJ 11003번

import sys
input = sys.stdin.readline
from collections import deque

queue = deque()
answer = []
value , index = 0 , 1

n , l = map( int , input().split() )
num_list = list ( map( int , input().split() ) )

for current , number in enumerate( num_list ) :
    while queue and queue[-1][value] > number :
        queue.pop()
    queue.append( (number,current) )
    
    while queue and current - l + 1 > queue[0][index] :
        queue.popleft()

    answer.append( queue[0][value] )
    
print ( *answer)