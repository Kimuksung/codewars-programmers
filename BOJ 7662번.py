import sys
import bisect
from collections import deque
input = sys.stdin.readline

n = int(input())

def alu( m ) :
    arr = deque()

    for _ in range( m ) :
        query , data = map (str , input().rstrip().split() )
        data = int(data)

        if query == 'I' :
            bisect.insort( arr, data )
        elif not arr :
            continue
        elif query == 'D' and data == 1 :
            arr.pop()
        else :
            arr.popleft()
    if not arr :
        print ( 'EMPTY' )
        return
    print ( arr[-1] , arr[0] )

for _ in range( n ) :
    m = int(input())
    alu ( m )

