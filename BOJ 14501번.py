#BOJ 14501번

import sys
input = sys.stdin.readline
n = int ( input() )

take_time = [0]
value_data = [0]
dp = [0] * (n+2)

for _ in range( n ) :
    time , value = map ( int , input().split() )
    take_time.append( time )
    value_data.append( value )

for index , time in enumerate ( take_time ) :
    if index ==0 :
        continue

    move_time = take_time[index]+index
    if dp[index] < dp[index-1] :
        dp[index] = dp[index-1]

    if move_time <= n+1 :
        dp[move_time] = max( dp[move_time] , dp[index]+value_data[index] )
    
print( max(dp) )
