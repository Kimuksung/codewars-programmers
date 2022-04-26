# BOJ 7569번
import sys
input = sys.stdin.readline
from collections import deque

n , m , height = map ( int , input().split() )
q = deque()
tomatos = [ [[-1] * n for _ in range(m) ] for _ in range(height) ]
answer = 0
dx , dy , dh = [0,0,1,-1] , [1,-1,0,0] , [1,-1]

def vfs ( ) :
    global answer
    while q :
        temp_h , temp_y , temp_x , temp_days = q.popleft()
        for i in range(4) : # 상하좌우
            if temp_y + dy[i] >= 0 and temp_y + dy[i] < m and temp_x + dx[i] >= 0 and temp_x + dx[i] < n :
                if tomatos[temp_h][temp_y + dy[i]][temp_x + dx[i]] == 0 :
                    tomatos[temp_h][temp_y + dy[i]][temp_x + dx[i]] = 1
                    q.append( ( temp_h , temp_y + dy[i] , temp_x + dx[i] , temp_days+1) )
                    answer = max(temp_days+1 , answer)
        for i in range(2) : # 3차원 이동
            if temp_h + dh[i] >= 0 and temp_h + dh[i] < height :
                if tomatos[temp_h+dh[i]][temp_y][temp_x] == 0 :
                    tomatos[temp_h+dh[i]][temp_y][temp_x] = 1
                    q.append( (temp_h+dh[i] , temp_y , temp_x , temp_days+1 ) )
                    answer = max(temp_days+1 , answer)
        
def checking_no_tomatos() :
    vfs()
    for h in range( height ) :
        for y in range ( m ) :
            for x in range( n ) :
                if tomatos[h][y][x] == 0 :
                    return False
    return True

for h in range( height ) :
    for y in range ( m ) :
        temp = map( int , input().rstrip().split() )
        for x , value in enumerate ( temp ) :
            tomatos[h][y][x] = value
            if value == 1 :
                q.append( (h,y,x,0) )

if len(q) == n*m*height :
    print( '0' )
    exit()

if not checking_no_tomatos() :
    print('-1')
    exit()

print ( answer )