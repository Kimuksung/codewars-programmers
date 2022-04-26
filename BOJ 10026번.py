#BOJ 10026번

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [ ['t'] * n for _ in range ( n ) ] 
visited = [ [False] * n for _ in range ( n ) ] 
answer , answer_2 = 0 , 0

dx , dy = [0,0,1,-1] , [1,-1,0,0]

for x in range( n ) :
    for y , value in enumerate( input().rstrip() ) :
        maps[x][y] =value

def vfs ( start_x , start_y , color ) :
    q = deque()
    q.append( (start_x , start_y) )
    while q :
        start_x , start_y = q.popleft()
        for i in range( 4 ) :
            if start_x + dx[i] >= 0 and start_x + dx[i] < n and start_y + dy[i] >= 0 and start_y +dy[i] < n :
                temp_x = start_x + dx[i]
                temp_y = start_y + dy[i]
                if not visited[temp_x][temp_y] and color == maps[temp_x][temp_y] :
                    visited[temp_x][temp_y] = True
                    q.append( (temp_x,temp_y) )

for i in range ( n ) :
    for j in range( n ) :
        if not visited[i][j] :
            vfs( i , j , maps[i][j])
            answer += 1

for i in range( n ) :
    for j in range ( n ) :
        if maps[i][j] == 'G':
            maps[i][j] = 'R'

visited = [ [False] * n for _ in range ( n ) ] 

for i in range ( n ) :
    for j in range( n ) :
        if not visited[i][j] :
            vfs( i , j , maps[i][j])
            answer_2 += 1

print ( answer , answer_2 )