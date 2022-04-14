#BOJ 10845번

from collections import deque
import sys
input = sys.stdin.readline
n = int( input() )
command , value = 0 , 1
queue = deque()

for _ in range( n ) :
    data = list ( map( str , input().split() ) )
    if data[command] == 'push' :
        queue.append( data[value])

    if data[command] == 'pop' :
        if not queue :
            print('-1')
            continue
        print( queue.popleft() )

    if data[command] == 'size' :
        print(len(queue))

    if data[command] == 'empty' :
        if queue :
            print('0')
            continue
        print('1')

    if data[command] == 'front' :
        if queue :
            print ( queue[0] )
        else :
            print ( '-1' )

    if data[command] == 'back' :
        if queue :
            print(queue[-1])
        else :
            print ( '-1' )

