import sys
input = sys.stdin.readline

#idea two pointer
n , m = map ( int , input().split(' ') )

arr = [int(input()) for i in range(n) ]
end  =  0
min_value = 2000000001
arr.append( min_value)

arr.sort()

for start in range ( n ) :
    while end < n and arr[end] - arr[start] < m :
        end += 1
        if end == n :
            break
        
    min_value = min ( min_value , arr[end] - arr[start] )

print ( min_value )
