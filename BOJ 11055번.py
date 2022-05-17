#BOJ 11055번

n = int ( input() )
number_list = list ( map(int , input().split() ) )
dp = [0] * n
dp[0] = number_list[0]
temp = dp[0]

for index , value in enumerate( number_list ) :
    dp[index] = number_list[index]
    for before_index in range( index ) :
        if number_list[before_index] < value :
            dp[index] = max( dp[index] , dp[before_index]+value )

print ( max(dp) )