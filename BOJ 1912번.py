#BOJ 1912번

n = int(input())
num_list = list(map ( int ,input().split() ))

dp = [0]*n
dp[0] = num_list[0]

for index in range( 1, n ) :
    dp[index] = max(dp[index-1]+num_list[index] , num_list[index])

print( max( dp) )