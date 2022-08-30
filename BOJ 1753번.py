#BOJ 1753번

import sys
import heapq
input = sys.stdin.readline

#init
V,E = map(int,input().split())
start = int(input())
graphs = [[] for _ in range(V+1)]
table = [float('INF')]*(V+1)
table[start]=0
q = []
heapq.heappush(q,(0,start))

#Graph
for _ in range(E):
    st,en,value = map(int,input().split())
    graphs[st].append((en,value))

while q:
    value,node = heapq.heappop(q)
    # 1. Check
    if table[node]!=value :
        continue

    # 2. table 갱신 및 heapq 추가
    for end,value in graphs[node]:
        if table[end] > table[node]+value :
            table[end] = table[node]+value
            heapq.heappush(q,(table[node]+value,end))

[ print('INF') if data==float('INF') else print(data) for data in table[1:] ]