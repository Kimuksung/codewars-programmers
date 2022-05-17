#BOJ 10815번

answer = []
n = int( input() )
sangun = list( map( int , input().split() ) )
m = int( input() )
targets = list( map( int , input().split() ) )
sangun.sort()

def check( start , end , target) :
    mid = (start+end) // 2
    if start >= end :
        return 0
    elif sangun[mid] == target :
        return 1

    if sangun[mid] < target :
        start = mid+1
    else :
        end = mid
    return check(start,end,target)

for target in targets :
    answer.append( check( 0 , n , target ) )

print(*answer)
