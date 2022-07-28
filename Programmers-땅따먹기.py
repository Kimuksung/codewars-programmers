# Programmers - 땅따먹기

def solution(land):
    answer = 0
    n = len(land)
    dp = [[0]*4 for _ in range(n)]
    dp[0] = land[0]
    
    for i in range(1,n):
        for j in range(4):
            dp[i][j] = max(dp[i-1][:j]+dp[i-1][j+1:])+land[i][j]
    
    return max(dp[-1])