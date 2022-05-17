#BOJ 2240번

t , w = map( int , input().split() )

dp = [ [[0] * (w+1) for _ in range( 2 ) ] for _ in range(t) ]
datas = [0] * (t+1)

for i in range(1,t+1) :
    datas[i] = int(input())

dp[1][0][0] = 1
dp[1][1][1] = 1

for current in range( 1 , t ) :
    choice_one , choice_two = int ( datas[current]==1 ) , int ( datas[current] == 2 )
    for j in range(w+1) :
        if j == 0 :
            dp[current][0][j] = dp[current-1][0][j] + choice_one
            dp[current][1][j] = dp[current-1][1][j] + choice_two
        else :
            dp[current][0][j] = max ( dp[current-1][1][j-1] , dp[current-1][0][j] ) + choice_one
            dp[current][1][j] = max ( dp[current-1][0][j-1] , dp[current-1][1][j] ) + choice_two

[print(dps) for dps in dp]
print ( max( max(dp[-1][0]) , max(dp[-1][1])) )