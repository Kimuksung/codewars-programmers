import sys
input = sys.stdin.readline

N = int ( input() )
for i in range ( N ) :
    data = int(input())

    arr = [0] * ( data+1 )
    if data in [1,2,3] :
        temp = [0,1,2,4]
        print(temp[data])
        continue
    if data >= 4 :
        arr[1] = 1
        arr[2] = 2
        arr[3] = 4

    for i in range ( 4 , data+1 ) :
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

    print ( arr[data] )