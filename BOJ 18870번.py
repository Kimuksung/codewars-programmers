import sys
input = sys.stdin.readline

n = int ( input() )
arrs = list ( map ( int , ( input().split(' ') )) )
real_data = list ( set(arrs) )
answer = dict()

real_data.sort()
for i , v in enumerate( real_data ) :
    answer[v] = i

[ print ( answer[arr] ) for arr in arrs ]
    