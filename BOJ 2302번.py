#BOJ 2302번

vips = []
n = int(input())
m = int(input())
answer , dev = 1 , 0

for _ in range(m) :
    vips.append(int(input()))
vips.append(n+1)

dp = [1,1,2] + [0]*(n+1)

for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]

if m >= 0 :
    for vip in vips :
        answer *= dp[vip-1-dev]
        dev = vip
    #answer *= dp[n-dev]

else :
    answer = dp[n]

print(answer)