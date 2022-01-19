from collections import deque
M , N  = map ( int , input().split() )
Maps = [ [0] * M for _ in range ( N ) ] 
dx , dy = [0 , 0 , 1, -1] , [1 , -1 , 0 , 0]
que = deque()
answer = 0
# Idea : 모든 시작점을 Queue에 넣는다.
#  방문한곳은 0보다 크거나 같다

for i in range ( N ) :
    data = list ( map ( int , input().split() ) )
    for j in range ( M ) :
        if data[j] == 1 : 
            Maps[i][j] = 1
            que.append( [i,j])
        elif data[j] == -1 :
            Maps[i][j] = -1

while ( que ) :
    x, y = que.popleft()
    for i in range(4) :
        nx , ny = x+dx[i] , y + dy[i]
        if ( nx < 0 or nx >= N or ny < 0 or ny >= M )    :
            continue
        if Maps[nx][ny] != 0  :
            continue
        que.append([nx,ny])
        Maps[nx][ny] = Maps[x][y] + 1

for i in Maps :
    for j in i :
        if j == 0 :
            print ( '-1')
            exit(0)

    answer = max(answer , max(i))
print ( answer -1  )


#print ('-1')  if 0 in sum(Maps, []) else print ( max(map( max , Maps ) ) - 1 )

