#BOJ 11052번

n = int(input())
datas = list(map(int,input().split()))
datas = [0]+datas
dp = [[0]*(n+1) for _ in range(n+1)]
dp[1][1] = datas[1]

for i in range(2,n+1) :
    dp[i][i] = datas[i]
    for j in range(1,i) :
        dp[i][j] = dp[i-1][j]
    for j in range(1,i) :
        dp[i][i] = max( dp[i][j]+datas[i-j] , dp[i][i] )

print( max(dp[-1]) )