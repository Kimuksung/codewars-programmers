#BOJ 9084번

import sys
input = sys.stdin.readline

answer = []
k = int(input())
for _ in range(k) :
    n = int(input())
    money = list(map(int,input().split()))
    target = int(input())
    dp = [[0]*(target+1) for _ in range(len(money)+1)]
    dp[0][0] = 1

    for i in range(1,n+1) :
        devide = money[i-1]
        if devide > target+1 :
            devide = target+1
        for j in range(devide) :
            dp[i][j] = dp[i-1][j]
        for j in range(devide,target+1) :
            dp[i][j] = dp[i][j-devide]+dp[i-1][j]

    answer.append(dp[-1][-1])

print(*answer)
