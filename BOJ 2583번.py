# BOJ 2583번

import sys
input = sys.stdin.readline
from collections import deque

m , n , k = map(int , input().split() )
maps = [ [0] * m for _ in range( n ) ]
dx , dy = [0,0,-1,1] , [1,-1,0,0]
answer = 0
space_list = []

for _ in range ( k ) :
    start_x , start_y , end_x , end_y = map(int , input().rstrip().split() )
    for i in range( start_x , end_x ) :
        for j in range ( start_y , end_y ) :
            maps[i][j] = 1
    
def vfs ( x , y ) :
    maps[x][y] = 1
    max_value = 1
    q = deque()
    q.append( (x,y,1) )
    while q :
        temp_x , temp_y , move = q.popleft()
        for i in range ( 4 ) :
            x = temp_x + dx[i]
            y = temp_y + dy[i]
            if x>= 0 and x < n and y >=0 and y < m and not maps[x][y] :
                maps[x][y] = 1
                max_value += 1
                q.append( (x,y, move+1 ) )

    return max_value

for i in range ( m ) :
    for j in range ( n ) :
        if not maps[j][i] :
            space_list.append( vfs( j,i ) )
            answer += 1

space_list.sort()
print ( answer )
print ( *space_list )
