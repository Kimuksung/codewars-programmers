#BOJ 15688번

import sys
input = sys.stdin.readline 

n = int ( input() )
datas = [0] * 2000001

for _ in range ( n ) :
    datas[int(input())+1000000 ] += 1

for index , value in enumerate ( datas ) :
    if value == 0 :
        continue
    for _ in range( value ) :
        print( index-1000000 )
