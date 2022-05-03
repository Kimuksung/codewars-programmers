#BOJ 11559번

dx , dy = [0,0,-1,1] , [1,-1,0,0]

maps = [ list ( map ( str , input() ) ) for _ in range( 12 ) ]
answer = 0

def bomb ( x,y ) :
    check_data = maps[x][y]
    q = []
    q.append( (x,y) )
    visited[x][y] = True
    temp_xy_list = [(x,y)]

    while q :
        x , y = q.pop()
        for i in range( 4 ) :
            nx , ny = x+dx[i] , y+dy[i]
            if 0<= nx < 12 and 0<= ny < 6 and maps[nx][ny] == check_data and not visited[nx][ny] :
                visited[nx][ny] = True
                q.append( ( nx,ny ) )
                temp_xy_list.append( (nx,ny) )

    if len( temp_xy_list ) >= 4 :
        for temp in temp_xy_list :
            temp_x , temp_y = temp
            maps[temp_x][temp_y] = '.'
        return 1
    return 0

while True :  
    visited = [ [False] * 6 for _ in range(12) ]
    check = 0
    for i in range( 11 , -1 , -1) :
        for j in range ( 6 ) :
            if maps[i][j] != '.' and  not visited[i][j] :
                check += bomb(i,j)      
    
    if check == 0 :
        break
    
    answer += 1

    for j in range ( 6 ) :
        temp_list = []
        for i in range( 11 , -1 , -1) :
            if maps[i][j] != '.' :
                temp_list.append( maps[i][j] )
        temp_list +=['.'] * ( 12 - len(temp_list) )
        for index , temp in enumerate ( temp_list[::-1] ) :
            maps[index][j] = temp
    
print ( answer )