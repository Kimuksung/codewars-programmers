#BOJ 2667번

from collections import deque
import sys
input = sys.stdin.readline

n = int ( input() )
maps = [ [0] * n for _ in range ( n ) ]
answer = []
dx , dy = [0,0,-1,1] , [1,-1,0,0]
q = deque()

def vfs ( start_x , start_y ) :
    q.append( (start_x , start_y ) )
    maps[start_x][start_y] = 0
    temp_move = 0
    while q :
        x , y = q.popleft()
        temp_move += 1
        for i in range( 4 ) :
            temp_x , temp_y = x + dx[i] , y+dy[i]
            if temp_x >= 0 and temp_x < n and temp_y >= 0 and temp_y < n and maps[temp_x][temp_y]:
                maps[temp_x][temp_y] = 0
                q.append( (temp_x , temp_y ) )
                
    answer.append( temp_move )

for i in range ( n ) :
    for j , data in enumerate ( input().rstrip() ) :
        if int ( data ) :
            maps[i][j] = 1

for i in range ( n ) :
    for j in range ( n ) :
        if maps[i][j] :
            vfs( i , j ) 

answer.sort()
print ( len(answer) ,  *answer )