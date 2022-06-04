#BOJ 2294번

n , target = map(int,input().split())
datas = list( int(input()) for _ in range(n) ) 
datas.sort()

dp = [[-1]*(target+1) for _ in range(n)]

#init
for j in range(target+1) :
    if j%datas[0] == 0 :
        dp[0][j] = j//datas[0]

for i in range(1,n) :
    for j in range(1, min( datas[i],target+1 )) :
        dp[i][j] = dp[i-1][j]

    dp[i][0] = 0

    for j in range(datas[i] , target+1) :
        if dp[i-1][j] != -1 and dp[i][j-datas[i]] != -1:
            dp[i][j] = min(dp[i-1][j] , dp[i][j-datas[i]]+1)
        elif dp[i-1][j] != -1 :
            dp[i][j] = dp[i-1][j]
        elif dp[i][j-datas[i]] != -1 :
            dp[i][j] = dp[i][j-datas[i]]+1

#[ print(dps) for dps in dp ]
print(dp[-1][-1])