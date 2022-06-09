#BOJ 1520번

import heapq

dx , dy = [0,0,-1,1] , [1,-1,0,0]
n , m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0]=1
q = []

heapq.heappush( q , (-maps[0][0] ,0,0) )

while q :
    current,x,y= heapq.heappop(q)
    current = -1*current
    for i in range(4):
        nx , ny = x+dx[i] , y+dy[i]
        if 0<=nx<n and 0<=ny<m and maps[nx][ny] < current :
            if dp[nx][ny]==0 :
                heapq.heappush( q , (-maps[nx][ny],nx,ny))
            dp[nx][ny] += dp[x][y]

print(dp[-1][-1])