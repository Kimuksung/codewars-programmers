#BOJ 11650번

import sys
input = sys.stdin.readline

n = int(input())
datas = []

for _ in range(n) :
    datas.append( tuple (map(int,input().split() ) ))

datas.sort()
[ print ( *data ) for data in datas ]