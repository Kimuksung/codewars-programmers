#BOJ 1520번

dx , dy = [0,0,-1,1] , [1,-1,0,0]
n , m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1

#[print(map) for map in maps]
[print(dps) for dps in dp]

for i in range(n) :
    for j in range(m) :
        current = maps[i][j]

        for t in range(4):
            x , y =i+dx[t] , j+dy[t]
            if 0<=x<n and 0<=y<m and current < maps[x][y]:
                dp[i][j] += dp[x][y]

print('-'*10)
[print(dps) for dps in dp]

for i in range(n) :
    for j in range(m) :
        if i==0 and j ==0 :
            continue
        current = maps[i][j]

        for t in range(4):
            x , y =i+dx[t] , j+dy[t]
            if 0<=x<n and 0<=y<m and current < maps[x][y]:
                dp[i][j] += dp[x][y]

print('-'*10)
[print(dps) for dps in dp]