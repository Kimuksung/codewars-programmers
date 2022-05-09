#BOJ 10825번

import sys
input = sys.stdin.readline

n = int(input())
datas = []

for _ in range(n) :
    datas.append ( tuple( map ( str , input().split() ) ) )

datas.sort( key = lambda x : ( -int(x[1]) , int(x[2]) , -int(x[3]) , x[0] ) )
[print ( data[0] ) for data in datas ]