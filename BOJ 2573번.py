#BOJ 2573번

from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

dx , dy = [0,0,-1,1] , [1,-1,0,0]
time = 1
answer = 0

# 1년이 지난 뒤 빙산
def after_one_year ( copy_maps ) :
    for i in range( 1 , n-1 ) :
        for j in range( 1, m-1 ) :
            cnt = 0
            if copy_maps[i][j] != 0 :
                for index in range( 4 ) :
                    temp_x , temp_y = i+dx[index] , j+dy[index]
                    if temp_x >= 0 and temp_x < n and temp_y >= 0 and temp_y < n and copy_maps[temp_x][temp_y] == 0 :
                        cnt += 1
            maps[i][j] = max ( 0 , maps[i][j] - cnt  )

# 빙산이 나누어졌는지 탐색
# 0으로 가득찬 경우 return 0
# 그외의 경우는 분산된 갯수
def dfs ( ) :
    visited = [ [False] * m for _ in range ( n ) ]
    stack = []
    cnt = 0
    for i in range ( 1 , n-1 ):
        for j in range( 1, m-1 ) :
            if maps[i][j] != 0 and not visited[i][j] :
                cnt += 1
                visited[i][j] = True
                stack.append( (i,j) )
                while stack :
                    x , y = stack.pop()
                    for index in range( 4 ) :
                        temp_x , temp_y = x+dx[index] , y+dy[index]
                        if temp_x >= 0 and temp_x < n and temp_y >= 0 and temp_y < m and maps[temp_x][temp_y] != 0 and not visited[temp_x][temp_y]:
                            visited[temp_x][temp_y] = True
                            stack.append( ( temp_x,temp_y ) )
                                  
    return cnt
'''
def bfs( ):
    visited = [ [False] * m for _ in range ( n ) ]
    q = deque()
    cnt = 0
    for i in range( 1, n-1 ) :
        for j in range( 1, m-1) :
            if maps[i][j] != 0 and not visited[i][j] :
                cnt += 1
                q.append( (i,j) )
                visited[i][j] = True
                while q :
                    x , y = q.popleft()
                    for index in range(4) :
                        nx , ny = x + dx[index] , y + dy[index]
                        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

    if cnt == 0 :
        return 0
    return cnt
'''

n , m = map ( int , input().split() )
maps = [ list( map( int , input().split() ) ) for _ in range ( n ) ]

while True :
    after_one_year ( deepcopy( maps ) ) #한 시간 후
    temp = dfs() # 빙산이 나누어졌는지 여부 

    if temp == 0 : #빙산이 다 녹은 경우
        answer = 0
        break

    if temp >= 2 : #빙산 덩어리가 나누어진 경우
        answer = time
        break
    time += 1

print ( answer )
