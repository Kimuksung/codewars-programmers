#BOJ 11727번

n = int(input())

dp = [0,1,3] + [0] * 1000

for i in range( 3, n+1) :
    dp[i]= dp[i-1] + dp[i-2]*2

print(dp[n]%10007)