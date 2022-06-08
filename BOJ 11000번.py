#BOJ 11000번

import sys
input = sys.stdin.readline
import heapq

n = int(input())
datas = [ tuple( map(int,input().split())) for _ in range(n) ]
datas.sort()
q = []

for data in datas :
    if q :
        top = heapq.heappop(q)
        if top[0] > data[0] :
            heapq.heappush( q , top )
            heapq.heappush( q , (data[1] ,data[0]) )
        else :
            heapq.heappush( q , (data[1] ,data[0]) )
    else :
        heapq.heappush( q , (data[1] ,data[0]) )

print( len(q) )