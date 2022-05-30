#BOJ 11501번
from copy import deepcopy
n = int(input())
jusik = list(map(int,input().split()))
dp = [[(0,[])]*3 for _ in range(n+1)]

no_move , buy , sell = 0 , 1, 2
for i in range(1,n+1) :
    dp[i][no_move] = max ( dp[i-1][no_move] , dp[i-1][buy] , dp[i-1][sell] )
    
    money , buy_jusik = dp[i-1][buy]
    dp[i][buy] = (money-jusik[i-1] , buy_jusik+[jusik[i-1]])

    money , sell_jusiks = dp[i-1][buy]
    temp_jusiks = []
    for sell_jusik in sell_jusiks :
        if sell_jusik < jusik[i-1] :
            money+= jusik[i-1]
            #sell_jusiks.remove(sell_jusik)
        else:
            temp_jusiks.append(sell_jusik)


    dp[i][sell] = (money , temp_jusiks)

[print(dps) for dps in dp]
