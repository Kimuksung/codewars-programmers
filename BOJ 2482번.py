#BOJ 2482번

n = int(input())
k = int(input())
devide = 1000000003
dp = [[0]*(n+1) for _ in range(k+1)]

for i in range(1,n+1):
    dp[1][i] = i

for i in range(2,k+1) :
    for j in range(i*2 , n+1) :
        print(i,j)
        dp[i][j] = dp[i-1][j-2]%devide + dp[i][j-1]%devide

print('-'*10)
[print(dps) for dps in dp]
print(dp[-1][-1]%devide)