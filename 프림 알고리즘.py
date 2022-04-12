# 프림 알고리즘
'''
5 7
1 2 4
1 3 3
1 4 3
2 5 8
3 5 5
3 4 4
4 5 6
'''

import sys
import heapq
input = sys.stdin.readline

v , e = map( int , input().split() )
adj = [ [] for _ in range(v+1) ]
heapq_list = []
start = 1
answer = [False] * (v+1)
answer[start] = True
cnt = 0

for _ in range ( e ) :
    edge_start , edge_end , cost = map ( int , input().split() )
    adj[edge_start].append( [edge_end,cost])
    adj[edge_end].append( [edge_start,cost])

for temp in adj[start] :
    edge_end , cost = temp
    heapq.heappush(heapq_list , ( cost , start , edge_end ))

print ( start )
while(cnt < v-1) :
    cost ,edge_start , edge_end = heapq.heappop(heapq_list)

    if answer[edge_end] :
        continue

    print ( edge_end )
    answer[edge_end] = True
    cnt += 1
    for temp in adj[edge_end] :
        edge_end , cost = temp
        heapq.heappush(heapq_list , ( cost , edge_start , edge_end ))
