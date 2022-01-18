from collections import deque

#Declare
N , M = map ( int , list ( input().split() ) )
Maps = [ [0] * M for _ in range(N) ]
Visited = [ [0] * M for _ in range(N) ]
answer = []

m_x = [ 0 , 0 , 1 , -1 ]
m_y = [ 1 , -1 , 0 , 0]

#Map 설정
for i in range( N ) :
    data = list ( map ( int , list ( input().split() ) ) )
    for j in range( M ) :
        Maps[i][j] = data[j]

#VFS
que = deque()
for i in range( N ) :
    for j in range( M ) :
        if Maps[i][j] == 1 and not Visited[i][j] :
            Visited[i][j] = 1
            depth = 1
            que.append( [i,j] )
            while ( que ) :
                x,y = que.popleft()
                for move_i in range(4) :
                    nx , ny = x + m_x[move_i] , y + m_y[move_i]
                    if ( 0<= nx < N ) and ( 0 <= ny < M ) :
                        if Maps[nx][ny] == 1 and Visited[nx][ny] == 0 : 
                            depth += 1
                            Visited[nx][ny] = 1
                            que.append( [nx , ny] )
            answer.append(depth)

print ( len(answer) )
print ( max(answer) if answer else 0)
