#프로그래머스 - 거스름돈
def solution(n, moneys):
    moneys.sort()
    dp = [1]+[0]*n
    #dp = [0]*(n+1)
    #dp[0]=1 
    
    for money in moneys :
        for i in range(money,n+1):
            dp[i]+= dp[i-money]
            
    return dp[-1]