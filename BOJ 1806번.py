import sys
input = sys.stdin.readline

n , m = map ( int , input().split(' ') )

arr = [0]
arr.extend( list ( map ( int , input().split(' ') ) ) )
arr.append(0)
arr_sum = [arr[0]]
for i in range(1, n+2) :
    arr_sum.append( arr_sum[i-1] + arr[i]  )

#print ( arr )
#print ( arr_sum )

if m == 0 :
    print ( min( arr[1:-1] ) )
    exit()

end = 1
min_value = n + 1

for start in range ( 1 , n+1 ) :
    while ( end < n and arr_sum[end] - arr_sum[start-1] < m ):
        end += 1
        if end == n :
            break
    if arr_sum[end] - arr_sum[start-1] >= m :
        min_value = min ( min_value , end - start + 1)

if min_value == n + 1 :
    print ( 0 )
    exit()
print ( min_value )
