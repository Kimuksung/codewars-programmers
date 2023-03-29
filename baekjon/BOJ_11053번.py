import sys
input = sys.stdin.readline

n = int(input())
number_list = [-1]+list(map(int,input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    temp = -1
    for j in range(i):
        if number_list[j]<number_list[i]:
            temp = max(dp[j]+1,temp)
    dp[i]=temp

print(max(dp))