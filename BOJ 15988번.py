#BOJ 15988번
import sys
input = sys.stdin.readline

answer = []
dp = [0,1,2,4] + [0] * 1000001
for i in range(4,1000001) :
        dp[i] = sum(dp[i-3:i]) %1000000009

m = int(input())
for _ in range(m) : 
    n = int(input())
    answer.append(dp[n])

print(*answer)