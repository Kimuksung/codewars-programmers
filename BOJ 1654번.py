import sys
input = sys.stdin.readline

n , k = map( int , input().split() )

arr = [ int(input()) for _ in range(n) ]

def devide_count ( number ) :
    return sum( [i//number for i in arr] )

# binary search 
start , end = 1 , arr[0]
while ( start < end ) :
    mid = ( start + end + 1 ) // 2 
    if devide_count(mid) >= k :
        start = mid
    else :
        end = mid-1

print ( start )
