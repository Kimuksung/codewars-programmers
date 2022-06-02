#BOJ 10942번

import sys
input = sys.stdin.readline

answer = []
n = int(input())
datas = list(map(int,input().split()))
dp = [[0]*n for _ in range(n) ]

#본인
for i in range(n):
    dp[i][i] = 1

#한칸
for i in range(n-1) :
    if datas[i] == datas[i+1] :
        dp[i][i+1] = 1

#두칸 이상
for i in range(2,n):
    for j in range(n-i) :
        if datas[j]==datas[j+i] and dp[j+1][j+i-1] == 1 :
            dp[j][j+i]=1

k = int(input())
for _ in range(k) :
    start , end = map(int,input().split())
    answer.append( dp[start-1][end-1] )

print(*answer)