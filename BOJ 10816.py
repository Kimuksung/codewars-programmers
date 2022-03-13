import sys
input = sys.stdin.readline

n = int ( input() )
arr = list( map ( int , input().split(' ')))
m = int ( input() )
targets = list( map ( int , input().split(' ')))

arr.sort()

def max_binary_search ( number ) :
    start , end  = 0 , n
    mid = ( start + end ) // 2

    while ( start < end ) :
        mid = ( start + end ) // 2
        
        if arr[mid] > number :
            end = mid
        else :
            start = mid + 1
    return start
    
def min_binary_search ( number ) :
    start , end  = 0 , n
    mid = ( start + end ) // 2

    while ( start < end ) :
        #print ( start ,end , mid , number )
        mid = ( start + end ) // 2
        
        if arr[mid] >= number :
            end = mid
        else :
            start = mid + 1    
    return start

[print ( max_binary_search ( target ) - min_binary_search( target )  )for target in targets ]


