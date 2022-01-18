from collections import deque
N , M = map ( int , list ( input().split() ) )
Maps = [ [0] * M for _ in range ( N ) ]
Visited = [ [0] * M for _ in range ( N ) ]
Visited[0][0] = 1
dx = [ 0 , 0 , 1 , -1 ]
dy = [ 1 , -1 , 0 , 0]

for i in range ( N ) :
    data = input()  
    for j in range ( M ) :
        Maps[i][j] = int ( data[j] )

que = deque()
que.append([0,0])
while ( que ) :
    x , y = que.popleft()
    for i in range ( 4 ) :
        nx , ny = x + dx[i] , y + dy[i]
        if nx == N and ny == M : 
            break
        if ( 0<= nx < N ) and 0 <= ny < M and Maps[nx][ny] :
            if Visited[nx][ny] == 0 :
                que.append( [nx,ny] )
                Visited[nx][ny] = Visited[x][y] + 1

print ( Visited[N-1][M-1] )
