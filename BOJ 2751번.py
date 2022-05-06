#BOJ 2751번

import sys
input = sys.stdin.readline

n = int( input() )
data = [ 0 ] * 2000001

for _ in range(n) :
    data[int(input()) + 1000000 ] += 1

for index ,value in enumerate( data ) :
    if value > 0 :
        print( index - 1000000 )
