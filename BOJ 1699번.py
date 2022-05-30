#BOJ 1699번

n = int(input())
sqaured_num = []
dp = [9999]*100001

for i in range(1,316) :
    if i*i > n :
        break
    sqaured_num.append(i*i)
    dp[i*i] = 1

for i in range(1,n+1) :
    for j in sqaured_num :
        #print(i,j)
        if i-j <= 0 :
            break
        dp[i] = min(dp[i-j]+1,dp[i])

print(dp[:n+1])