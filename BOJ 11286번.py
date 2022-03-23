import sys
import heapq
input = sys.stdin.readline

n = int ( input () )
heap = []
answer = []
for _ in range ( n ) :
    temp = int( input() )
    if not temp == 0 :
        heapq.heappush ( heap , [- abs(1/temp),temp ] )
    
    else :
        if heap :
            answer.append ( heapq.heappop( heap )[1] )
        else : 
            answer.append ( 0 )

[ print( i ) for i in answer ]
    

