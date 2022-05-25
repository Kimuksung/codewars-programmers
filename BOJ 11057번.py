#BOJ 11057번

n = int(input())
#datas= [i for i in range(10,-1,-1)]
dp = [[0]*10 for _ in range(n)]
dp[0] = [1]*10

for i in range(1,n) :
    for j in range(10) :
        dp[i][j] += sum(dp[i-1][j:])

print( sum(dp[-1])%10007 )