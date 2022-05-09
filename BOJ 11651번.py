#BOJ 11651번

import sys
input = sys.stdin.readline

n = int ( input() )
datas = []
for _ in range(n) :
    datas.append( tuple(map(int,input().split() )))

datas = sorted ( datas , key = lambda x : ( x[1] , x[0]) )

[ print ( *data ) for data in datas ]
