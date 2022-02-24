import sys
input = sys.stdin.readline

N = int ( input() )

if N == 0 :
    print ( 0 )
    exit()

arr = [9999] * (N+1)
arr[1] = 0

for i in range( N ) :
    temp = arr[i] + 1
    if i*3 <= N :
        arr[i*3] = min ( temp , arr[i*3])
    if i*2 <= N :
        arr[i*2] = min ( temp , arr[i*2])
    arr[i+1] = min ( temp , arr[i+1])

print ( arr[N] )