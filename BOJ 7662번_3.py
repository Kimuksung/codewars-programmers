import sys
input = sys.stdin.readline
import heapq


m = int ( input() )

for _ in range ( m ) :
    n = int(input())
    visitied = [False]*1_000_001
    min_heap = []
    max_heap = []

    for i in range( n ) :
        command , value = map( str , input().split() )
        value = int ( value )

        if command =='I':
            heapq.heappush( min_heap , (value , i ))
            heapq.heappush( max_heap , (-value , i ))
            visitied[i] = True

        elif value == 1:
            while max_heap and not visitied[max_heap[0][1]] :
                heapq.heappop( max_heap )
            if max_heap :
                visitied[max_heap[0][1]] = False
                heapq.heappop ( max_heap )

        else :
            while min_heap and not visitied[min_heap[0][1]] :
                heapq.heappop ( min_heap )

            if min_heap :
                visitied[min_heap[0][1]] = False
                heapq.heappop ( min_heap )

    while max_heap and not visitied[max_heap[0][1]] :
        heapq.heappop( max_heap )

    while min_heap and not visitied[min_heap[0][1]] :
        heapq.heappop( min_heap )

    if not min_heap or not max_heap :
        print ( 'EMPTY' )
    else :
        print ( -1 * max_heap[0][0] , min_heap[0][0] )