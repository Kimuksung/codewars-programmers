import sys
import heapq
input = sys.stdin.readline

n , k = map ( int , input().split() )
bosuks = []
bag = []
visitied = [False]*n
answer = 0

for index in range( n ) :
    weight , value = map ( int , input().split() )
    bosuks.append ( [weight , value , index ] )

bosuks = sorted ( bosuks , key = lambda x : (-x[1] , x[0] ) )

for _ in range( k ) :
    heapq.heappush ( bag , int(input() ) )

while bag :
    target = heapq.heappop ( bag )
    for bosuk in bosuks :
        if target >= bosuk[0] and not visitied[bosuk[2]] :
            answer += bosuk[1]
            visitied[bosuk[2]] = True
            break

print ( answer )