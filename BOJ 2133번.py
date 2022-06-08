#BOJ 2133번

n = int(input())
dp = [1] + [0,3]*n

for i in range(4,n+1,2) :
    dp[i] = dp[i-2]*3

    for j in range(i-4,-1,-2):
        dp[i] += dp[j]*2

print(dp[n])