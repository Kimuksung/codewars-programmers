#BOJ 9461번

k = int(input())

for _ in range(k) :
    n = int(input())
    dp = [0,1,1,1,2,2] + [0] * (n-5)

    for i in range( 6, n+1 ) :
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[n])    
