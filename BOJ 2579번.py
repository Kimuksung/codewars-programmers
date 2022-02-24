import sys
input = sys.stdin.readline

arr = [0]
N = int ( input() )
for i in range( N ) :
    temp = int ( input() )
    arr.append( temp )

if N == 1:
    print(arr[1])
    exit()

dp_data = [ [0] * (N+1) for _ in range ( N+1 ) ]
dp_data[1][1] = arr[1]
dp_data[1][2] = 0
dp_data[2][1] = arr[2]
dp_data[2][2] = arr[1] + arr[2]

for i in range( 3 , N+1 ) :
    dp_data[i][1] = max( dp_data[i-2][2] , dp_data[i-2][1] ) + arr[i]
    dp_data[i][2] = dp_data[i-1][1] + arr[i]

print ( max(dp_data[N][1] , dp_data[N][2] ) )



