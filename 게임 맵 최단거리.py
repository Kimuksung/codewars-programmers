from collections import deque
def solution(maps):
    N , M = len(maps) , len(maps[0])

    Visited = [ [0] * M for _ in range ( N )]
    Visited[0][0] = 1
    dx , dy = [0 , 0 , 1, -1] , [ 1 , -1 , 0 ,0]
    
    que = deque()
    que.append([0,0])
    
    while(que) :
        x,y = que.popleft()
        for i in range(4) :
            nx , ny = x + dx[i] , y + dy[i]
            if nx == N and ny == M :
                break
            if 0<= nx < N and 0<= ny < M and maps[nx][ny] :
                if Visited[nx][ny] == 0 :
                    Visited[nx][ny] = Visited[x][y] + 1
                    que.append([nx,ny])
    if Visited[N-1][M-1] == 0 :           
        return -1
    
    return Visited[N-1][M-1]