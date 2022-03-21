import heapq
import sys
input = sys.stdin.readline

n = int(input())

for _ in range ( n ) :
    min_heap = []
    max_heap = []
    m = int(input())
    visited = [False] * m
    
    for i in range ( m ) :
        command , value = map ( str , input().split() )
        value = int ( value )
        if command == 'I':        
            heapq.heappush( min_heap , ( value , i ) )
            heapq.heappush( max_heap , ( - value , i ) )
            visited[i] = True

        elif command == 'D' and value == 1:
            while max_heap and not visited[max_heap[0][1]] :
                heapq.heappop ( max_heap )
            if max_heap :
                visited[max_heap[0][1]] = False
                heapq.heappop ( max_heap )
        else :         
            while min_heap and not visited[min_heap[0][1]]: 
                heapq.heappop ( min_heap )
            if min_heap :
                visited[max_heap[0][1]] = False
                heapq.heappop ( min_heap )
        #print ( max_heap , max_heap[0][1] , visited[max_heap[0][1]] )
    while max_heap and not visited[max_heap[0][1]] :
        heapq.heappop ( max_heap )

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop ( min_heap )
            
    #print ( 'min_heap : ' , min_heap )
    #print ( 'max_heap : ' , max_heap )
    #print ( visited )
    if not min_heap or not max_heap :
        print ( 'EMPTY' )
    else :
        print ( -1 * max_heap[0][0] , min_heap[0][0] )
