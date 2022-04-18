# BOJ 18258번

import sys
input = sys.stdin.readline
from  collections import deque

n = int(input())
queue = deque()
answer = []
cmd , value = 0 , 1

for _ in range( n ) :
    command = list ( map( str , input().split() ) )
    if command[cmd] == 'push' :
        value = int ( command[value] )
        queue.append(value)

    if command[cmd] == 'pop' :
        if queue :
            answer.append( queue.popleft() )
        else :
            answer.append ( '-1' )

    if command[cmd] == 'size' :
        answer.append ( len(queue))

    if command[cmd] == 'empty' :
        if queue :
            answer.append ( '0' )
        else :
            answer.append ( '1' )

    if command[cmd] == 'front' :
        if queue :
            answer.append( queue[0] )
        else : 
            answer.append( '-1' )

    if command[cmd] == 'back' :
        if queue :
            answer.append( queue[-1] )
        else : 
            answer.append( '-1' )

print ( *answer )