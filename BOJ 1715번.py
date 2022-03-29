import heapq
import sys
input = sys.stdin.readline

def solution ( n ) :
    temp = []
    answer = 0

    [heapq.heappush ( temp , int(input() ) ) for _ in range ( n ) ]
        
    # 예외 처리
    if n == 1 :
        return 0

    while len(temp) > 1 :
        first , second = heapq.heappop( temp ) , heapq.heappop( temp )
        change_value = first + second
        heapq.heappush ( temp , change_value )
        answer += change_value
    
    return answer

n = int ( input() )
print ( solution ( n ) )
