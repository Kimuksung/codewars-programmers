import sys
input = sys.stdin.readline

N = int ( input() )
S = [[0] * 3 for _ in range ( N )]
data = [[0] * 3 for _ in range ( N )]


for i in range ( N ) :
    temp = list ( map ( int, input().split(' ') ) )
    for j in range(3) :
        S[i][j] = temp[j]

data[0][0] = S[0][0]
data[0][1] = S[0][1]
data[0][2] = S[0][2]

#print( S )
#print ( '-' *10)
#print( data )

for i in range( 1, N ) :
    for j in range ( 3 ) :
        if j == 0 :
            data[i][j] = min( data[i-1][1] , data[i-1][2] ) + S[i][j]
        elif j == 1 :
            data[i][j] = min( data[i-1][0] , data[i-1][2] ) + S[i][j]
        elif j == 2 :
            data[i][j] = min( data[i-1][0] , data[i-1][1] ) + S[i][j]

print ( min( data[N-1][0] , data[N-1][1] , data[N-1][2] ))
