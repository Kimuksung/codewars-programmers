#BOJ 7562번

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dx , dy = [1,2,1,2,-2,-1,-1,-2] , [2,1,-2,-1,-1,-2,2,1]

def vfs ( visited , end_x , end_y ) :
    while q :
        x , y , move = q.popleft()
        if x == end_x and y == end_y :
            return move

        for i in range(8) :
            temp_x , temp_y = x+dx[i] , y+dy[i]
            if temp_x >= 0 and temp_x < length and temp_y >= 0 and temp_y < length :
                if not visited[temp_x][temp_y] :
                    visited[temp_x][temp_y] = True
                    q.append( (temp_x , temp_y , move+1 ) )

for _ in range( n ) :
    q = deque()
    length = int(input())
    visited = [ [False] * length for _ in range( length ) ]
    start_x , start_y = map( int, input().split() )
    end_x , end_y = map( int, input().split() )
    q.append( ( start_x , start_y , 0 ) )
    print ( vfs ( visited , end_x , end_y ) )
