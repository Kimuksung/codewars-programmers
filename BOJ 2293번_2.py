#BOJ 2293번

n , k = map(int,input().split())
datas = [int(input()) for _ in range(n) ] 
dp = [1] + [0]*(k)
for data in datas :
    for i in range(data,k+1) :
        dp[i] = dp[i-data]+dp[i]

print(dp[k])