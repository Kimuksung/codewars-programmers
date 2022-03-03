import sys
input = sys.stdin.readline

N , K = map ( int , input().split() )
arr = []
cnt = 0

for i in range ( N ) :
    arr.append(  int ( input() ) )

for i in range ( N-1 , 0-1 , -1 ) :
    temp = K // arr[i]
    if temp > 0 :
        cnt += temp
        K -= ( temp ) * arr[i]
    else :
        continue

print ( cnt )