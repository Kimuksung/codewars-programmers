#BOJ 1932번

import sys
input = sys.stdin.readline

n = int(input())
datas = [ list( map(int , input().split() )) for _ in range(n) ]

answer = -1
dp = [ [0]*i for i in range(1,n+1) ]
dp[0][0] = datas[0][0]

for i in range(1,n) :
    for j in range(i+1) :
        if j == 0 :
            dp[i][j] = dp[i-1][j] + datas[i][j]
        elif j == i :
            dp[i][j] = dp[i-1][j-1] + datas[i][j]
        else :
            dp[i][j] = max ( dp[i-1][j-1]+datas[i][j] , dp[i-1][j]+datas[i][j] )

print( max(dp[-1]))