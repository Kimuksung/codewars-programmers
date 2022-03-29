from collections import deque
import sys
input = sys.stdin.readline

def solution( ) :
    n , m = map( int , input().split() )
    edges = [[]*1 for _ in range( n+1 )]
    visited = [False] * (n+1)
    queue = deque()
    answer = 0

    for _ in range( m ) :
        start , end = map( int , input().split() )
        edges[start].append(end)
        edges[end].append(start)

    for index , edge in enumerate ( edges ) :
        if visited[index] :
            continue
        queue.append( index)
        visited[index] = True
        answer += 1

        while ( queue ) :
            temp = queue.popleft()
            for data in edges[temp] :
                if not visited[data] :
                    visited[data] = True
                    queue.append ( data )
    
    return answer-1

print ( solution() )



    

    

