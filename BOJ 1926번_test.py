from collections import deque

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
        if Maps[i][j] == 1 and not Visited[i][j]:
            Visited[i][j] = 1
            depth = 1
            que.append( [i,j] )
            while ( que ) :
                x,y = que.popleft()
                for move_i in range(4) :
                    if ( 0<= x + m_x[move_i] < N ) and ( 0 <= y + m_y[move_i] < M ) :
                        if Maps[x + m_x[move_i]][y + m_y[move_i]] == 1 and Visited[x + m_x[move_i]][y + m_y[move_i]] == 0 : 
                            depth += 1
                            Visited[x + m_x[move_i]][y + m_y[move_i]] = 1
                            que.append( [x + m_x[move_i] , y + m_y[move_i] ])
            answer.append(depth)

print ( len(answer) )
print ( max(answer) if answer else 0)
