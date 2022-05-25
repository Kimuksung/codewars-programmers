#BOJ 1788번

n = int(input())

dp = [0]*2000001
devide_zero = 1000000
dp[devide_zero+1] = 1
dp[devide_zero-1] = 1
devision = 1000000000

if n < -1 :
    for i in range(-2,n-1,-1):
        temp = dp[i+2+devide_zero]-dp[i+1+devide_zero]
        if temp < 0 :
            dp[i+devide_zero] = (dp[i+2+devide_zero]-dp[i+1+devide_zero]) % -devision
        else :
            dp[i+devide_zero] = (dp[i+2+devide_zero]-dp[i+1+devide_zero]) % devision

else :
    for i in range( 2,n+1) :
        dp[i+devide_zero] = (dp[i-1+devide_zero]+dp[i-2+devide_zero]) % devision

#print( dp[n+devide_zero] , dp[999998:1000001] , n+devide_zero)

if dp[n+devide_zero] == 0 :
    print(0)
elif dp[n+devide_zero] < 0 :
    print(-1)
else :
    print(1)

print( abs(dp[n+devide_zero]) )