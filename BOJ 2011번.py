#BOJ 2011번

datas = input()
n = len(datas)

if datas[0]=='0' :
    print(0)
    exit()
if n == 1 :
    if int(datas[0]) > 0 :
        print(1)
    else :
        print(0)
    exit()

dp = [[0]*2 for _ in range(n+1) ]
dp[1][0] = 1
dp[2][0] = 1 
temp = int(datas[0]+datas[1])
if 0 < temp < 27 :
    dp[2][1] = 1
if datas[1] == '0' :
    dp[2][0]=0

for i in range(3,n+1):
    #case zero
    if datas[i-1] == '0' :
        dp[i][0] = 0
        if datas[i-2] in ['1','2'] :
            dp[i][1] = sum(dp[i-2])%1000000

    #case one to nine
    else :
        dp[i][0] = sum(dp[i-1])%1000000

        if datas[i-2]=='0' :
            continue
        temp = int(datas[i-2]+datas[i-1])
        if 0 < temp < 27 :
            dp[i][1] = sum(dp[i-2])%1000000
        else :
            dp[i][1] = 0 

#[print(dps) for dps in dp ]
#answer
print(sum(dp[-1])%1000000)