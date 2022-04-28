#BOJ 2468번

from collections import deque

n = int( input() )
maps = [ [0] * n for _ in range ( n ) ]
dx , dy = [0,0,-1,1] , [1,-1,0,0]

answer = 0
for i in range ( n ) :
    for j , value in enumerate( input().split() ) :
        maps[i][j] = int ( value )

def vfs ( number ) :
    visited = [ [False] * n for _ in range ( n ) ]
    q = deque()
    cnt = 0
    for i in range ( n ) :
        for j in range ( n ) :
            if maps[i][j] <= number :
                visited[i][j] = True
            elif maps[i][j] > number and not visited[i][j] :
                q.append( (i,j) )
                visited[i][j] = True
                cnt += 1
                while q :
                    x , y = q.popleft()
                    for move in range ( 4 ) :
                        temp_x , temp_y = x + dx[move] , y + dy[move]
                        if temp_x >= 0 and temp_x < n and temp_y >= 0 and temp_y < n and not visited[temp_x][temp_y] and maps[temp_x][temp_y] > number :
                            q.append( (temp_x,temp_y) )
                            visited[temp_x][temp_y] = True

    return cnt 

for i in range ( 0 , 101 ) :
    answer = max ( vfs(i) , answer )

print ( answer )