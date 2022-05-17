#BOJ 10844번

# IDEA
# [자릿수][나올숫자] 
# 0인 경우 / 9인 경우는 전의 특정 자릿수만 보면됨

n = int(input())
dp = [ [0] * 10 for _ in range(n)]

for i in range(1,10) :
    dp[0][i] = 1

for i in range(1,n) :
    for j in range( 0 , 10 ) :
        if j == 0 :
            dp[i][j] = dp[i-1][1]
        elif j == 9 :
            dp[i][j] = dp[i-1][8]
        else :
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

answer = 0
for temp in dp[n-1] :
    answer += temp % 1000000000
print( answer % 1000000000 )