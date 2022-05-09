#BOJ 1600번

#IDEA 
#말처럼 이동하는 것은 Z 좌표로 나타낸다.

from collections import deque
import sys
input = sys.stdin.readline

q = deque()
q.append( (0,0,0,0))
answer = -1
dx , dy = [0,0,-1,1] , [-1,1,0,0]
dx_h , dy_h = [-2,-2,-1,-1,1,1,2,2] , [1,-1,2,-2,2,-2,1,-1]

k = int ( input() )
w , h = map ( int , input().split() )
maps = [ list ( map ( int , input().split() ) )  for _ in range (h) ] 
visited = [[[False] * w for _ in range(h) ] for _ in range(k+1) ]
visited[0][0][0] = True

def bfs () :
    while q :
        x , y , z , move_cnt = q.popleft()
        if x == h-1 and y == w-1 :
            return move_cnt 
        for i in range(4) :
            temp_x , temp_y = x+dx[i] , y+dy[i]
            if 0 <= temp_x < h and 0 <= temp_y < w and not visited[z][temp_x][temp_y] and maps[temp_x][temp_y] == 0 :
                visited[z][temp_x][temp_y] = True
                q.append( (temp_x,temp_y,z,move_cnt+1))

        for i in range(8) :
            temp_x , temp_y = x+dx_h[i] , y+dy_h[i]
            if 0 <= temp_x < h and 0 <= temp_y < w and 0<= z+1 < k+1  and not visited[z+1][temp_x][temp_y] and maps[temp_x][temp_y] == 0 :
                visited[z+1][temp_x][temp_y] = True
                q.append( (temp_x,temp_y,z+1,move_cnt+1))
            
    return -1

print ( bfs() )
