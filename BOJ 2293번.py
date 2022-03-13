import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int( input() )
arr = []
for _ in range(n) :
    arr.append ( int(input()) )

arr.sort()
two = list ( set ( [first+second for first in arr for second in arr ] ) )
two.sort()

#idea
# x + y = k - z
# k - z 의 값이 x+y에 값에서 있는지 여부
def binarysearch_check ( target , number ) :
    return bisect_right( target , number ) - bisect_left( target , number ) > 0 
#print ( two )
#check_data = [ ( target , target-third ) for target in arr[::-1] for third in arr ]

for target in arr[::-1] :
    for third in arr :
        trace = target-third
        if binarysearch_check( two , trace) :
            print(target)
            exit()