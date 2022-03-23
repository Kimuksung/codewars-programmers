import sys
import heapq
input = sys.stdin.readline

n , k = map ( int , input().split() )
bosuks = []
bags = []

answer = 0
target = []

for _ in range ( n ) :
    weight , value = map ( int , input().split() )
    heapq.heappush ( bosuks , ( weight , value ) )

bags = [int(input()) for _ in range ( k )] 
bags.sort()

for bag in bags :
    while bosuks and bag >= bosuks[0][0] :
        heapq.heappush( target , - heapq.heappop ( bosuks )[1] )
    if target :
        answer -= heapq.heappop ( target )
    elif not bosuks :
        break

print ( answer )