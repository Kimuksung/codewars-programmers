#BOJ  5427번

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
answer = []

for _ in range ( n ) : 
    q = deque()
    w , h = map ( int , input().split() )
    maps = [ ['#'] * w for _ in range ( h ) ]
    visited = [ [False] * w for _ in range ( h ) ]
    dx , dy = [0,0,1,-1] , [1,-1,0,0]

    for i in range( h ) :
        for j , value in enumerate ( input().rstrip() )  :
            maps[i][j] = value
            if value == '@':
                q.append( ( i,j,0 ) )
                visited[i][j] = True
            elif value == '*' :
                q.appendleft( ( i,j,-1) )

    def vfs () :
        while q :
            x , y , move = q.popleft()
            if move != -1 : # 사람인 경우
                for i in range( 4 ) :
                    temp_x = x+dx[i]
                    temp_y = y+dy[i]
                    if temp_x >= 0 and temp_x < h and temp_y >= 0 and temp_y < w  :
                        if not visited[temp_x][temp_y] and maps[temp_x][temp_y] == '.' :
                            visited[temp_x][temp_y] = True
                            q.append( (temp_x , temp_y , move+1 ) )
                    else :
                        return move+1

            else : # 불인 경우
                for i in range( 4 ) :
                    temp_x = x+dx[i]
                    temp_y = y+dy[i]
                    if temp_x >= 0 and temp_x < h and temp_y >= 0 and temp_y < w and maps[temp_x][temp_y] not in ['#' , '*'] :
                        maps[temp_x][temp_y] = '*'
                        q.append( (temp_x,temp_y,move) )
        return 'IMPOSSIBLE'

    answer.append( vfs() )

print ( *answer )
