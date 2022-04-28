#BOJ 6593번

from collections import deque
import sys
input = sys.stdin.readline

while True :
    l , r , c = map ( int , input().split() )
    if l == 0 and r == 0 and c == 0 :
        break
    maps = []
    visited = [[ [False] * c for _ in range ( r ) ] for _ in range ( l ) ]
    dx , dy , dz = [0,0,-1,1] , [1,-1,0,0] , [-1,1]

    for _ in range (l) :
        maps.append( [ list ( map ( str , input().rstrip() ) ) for _ in range ( r ) ] )
        input()

    def vfs ( start_z , start_y , start_x ) :
        q = deque()
        q.append( ( start_z , start_y , start_x , 0 ))
        visited[start_z][start_y][start_x] = True
        
        while q :
            z , y , x , move = q.popleft()
            if maps[z][y][x] == 'E' :
                return 'Escaped in {} minute(s).'.format( move )

            for i in range( 4 ) :
                temp_y , temp_x = y + dy[i] , x + dx[i]
                if temp_y >= 0 and temp_y < r and temp_x >= 0 and temp_x < c and maps[z][temp_y][temp_x] != '#' :
                    if not visited[z][temp_y][temp_x] :
                        visited[z][temp_y][temp_x] = True
                        q.append( ( z , temp_y , temp_x , move+1 ) )
                    
            for i in range ( 2 ) :
                temp_z = z + dz[i]
                if temp_z >= 0 and temp_z < l and maps[temp_z][y][x] != '#':   
                    if not visited[temp_z][y][x]  :
                        visited[temp_z][y][x] = True
                        q.append( ( temp_z,y,x,move+1 ) )

        return 'Trapped!'

    for z in range ( l ) :
        for y in range ( r ) :
            for x in range ( c ) :
                if maps[z][y][x] == 'S' :
                    print ( vfs( z , y , x ) )
