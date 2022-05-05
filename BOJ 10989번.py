#BOJ 10989번

import sys
input = sys.stdin.readline

n = int( input() )
datas = [0] * 10001

for _ in range( n ) :
    datas[int(input())] += 1

for index , data in enumerate ( datas ) :
    if data == 0 :
        continue
    for _ in range( data ) :
        print( index )
