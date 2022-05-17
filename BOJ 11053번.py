#BOJ 11053번

n = int( input() )
num_list = list( map ( int , input().split() ) )
dp = [1] * n

for index , value in enumerate( num_list ) :
    for j in range( index ) :
        if num_list[j] < value :
            dp[index] = max( dp[index] , dp[j]+1 )

print( max( dp ) )