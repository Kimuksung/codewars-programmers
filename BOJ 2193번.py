#BOJ 2193번

#IDEA
#전에 단계에서 0으로 끝나는 값은 -> 0 , 1 둘다 가능
#             1로 끝나는 값은 -> 0만 가능

n = int(input())
dp = [[0] * 2 for _ in range(91) ]

dp[1][1] = 1
dp[2][0] = 1

for i in range( 3, n+1) :
    dp[i][0] = dp[i-1][0]+dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print( sum( dp[n]) )