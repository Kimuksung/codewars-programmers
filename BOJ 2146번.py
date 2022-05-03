#BOJ 2146번
from collections import deque
from copy import deepcopy
dx , dy = [0,0,-1,1] , [-1,1,0,0]
answer = []

n = int ( input() )

maps = [ list ( map ( int , input().split() ) ) for _ in range( n ) ]
maps_visited = [ [False] * n for _ in range ( n ) ]

def first_visit_init ( x , y ) :
    q = deque()  
    q.append( ( x,y ) )
    visited[x][y] = True
    maps_visited[x][y] = True
    while ( q ) :
        x , y = q.popleft()
        start_list.append( ( x,y) )
        for i in range ( 4 ) :
            nx , ny = x+dx[i] , y+dy[i]
            if 0<= nx < n and 0<= ny < n and maps[nx][ny] == 1 and not visited[nx][ny] :
                visited[nx][ny] = True
                maps_visited[nx][ny] = True
                q.append(( nx,ny ))    

def bfs( start_datas ) :
    q = deque()
    for start_data in start_datas :
        q.append( (start_data[0] , start_data[1] , 0) )

    while q :
        x , y , move = q.popleft()
        for i in range( 4 ) :
            nx , ny = x+dx[i] , y+dy[i]
            if 0<= nx < n and 0<= ny < n and not visited[nx][ny] :
                if not maps[nx][ny] :
                    visited[nx][ny] = True
                    q.append( (nx,ny,move+1) )
                else :
                    answer.append( move )
                    return
    return

for i in range ( n ) :
    for j in range ( n ) :
        if maps[i][j] and not maps_visited[i][j]:
            start_list = []
            visited = deepcopy(maps_visited)
            first_visit_init ( i , j )
            bfs( start_list )
            #print ( i , j , bfs( start_list ) , answer[-1])
            #print ( visited )

print ( min( answer ) )