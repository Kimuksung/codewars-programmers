from collections import deque
N , M = map( int , input().split() )
N , M = N + 2 , M + 2

Maps = [ [0] * M for _ in range ( N ) ]
Fire = [ [0] * M for _ in range ( N ) ]
Person = [ [0] * M for _ in range ( N ) ] # 지훈이가 필요하나?

dx , dy = [0,0,-1,1] , [1,-1,0,0]
que = deque ()

for i in range ( 1, N-1 ) :
    temp = input()
    for j in range ( 1, M-1 ) :
        if temp[j-1] == '#' :
            Maps[i][j] = 1
        elif temp[j-1] == 'J' :
            que.append( [i,j,'P'])
            Person[i][j] = 1
        elif temp[j-1] == 'F' : 
            que.append( [i,j,'F'])
            Fire[i][j] = 1
'''
for Map in Maps :
    print (Map)
print ( '---')
for t in Fire :
    print (t)
print ( '---')
for t in Person :
    print (t)
print ( '---')
'''
while ( que ) :
    x , y , status = que.popleft()
    #print ( x , y , status )
    if status == 'P' :
        if Fire[x][y] == 1 :
            continue
        for i in range( 4 ) :
            nx , ny = x + dx[i] , y + dy[i]
            if 0 <= nx < N and 0<= ny < M and Maps[nx][ny] == 0 :
                if Fire[nx][ny] == 0 and Person[nx][ny] == 0:
                    que.append( [nx , ny , 'P'] )
                    Person[nx][ny] = Person[x][y] + 1
                    if nx == 0 or ny == 0 or nx == N-1 or ny == M-1:
                        print ( Person[nx][ny] -1  )
                        exit(0)
    
    elif status == 'F' :
        for i in range ( 4 ) :
            nx , ny = x + dx[i] , y + dy[i]
            if 1 <= nx < N-1 and 0<= ny < M-1 and Maps[nx][ny] == 0 :      
                if Fire[nx][ny] == 0 :
                    que.append( [nx,ny,'F'])
                    Fire[nx][ny] = 1

print ( 'IMPOSSIBLE')