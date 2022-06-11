#BOJ  11660번

import sys
input = sys.stdin.readline

answer = []
n , m = map(int,input().split())

maps = [[0]*(n+1) for _ in range(n+1)]
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n) :
    maps[i+1]=[0]+list(map(int,input().split()))

for i in range(1,n+1):
    sum_value = 0
    for j in range(1,n+1) :
        sum_value += maps[i][j]
        dp[i][j] = sum_value

for _ in range(m) :
    x1,y1,x2,y2 = map(int,input().split())
    temp = 0
    for i in range(x1,x2+1):
        temp += dp[i][y2]-dp[i][y1-1]
    answer.append(temp)

print(*answer)