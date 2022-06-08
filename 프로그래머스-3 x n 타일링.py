def solution(n):
    answer = 0
    dp = [1,0,3]+[0]*5000
    devide = 1000000007
    for i in range(4,n+1,2) :
        dp[i] += (dp[i-2]*3)%devide
        
        for j in range(i-4,-1,-2) :
            dp[i] += (dp[j]*2)%devide
        
    return dp[n]%devide