# BOJ 1368 물대기
# https://intrepidgeeks.com/tutorial/bai-jun-1368-irrigation
'''
4
5
4
4
3
0 2 2 2
2 0 3 3
2 3 0 4
2 3 4 0
'''
import sys
import heapq
input = sys.stdin.readline

n = int( input() )
umul = [ int(input())for _ in range(n) ]
adj = [[] for _ in range(n) ]
real_answer = 30000001
for _ in range( n ) :
    edge_start , edge_end , cost_start_end , cost_end_start = map(int , input().split())
    adj[edge_start].append([cost_start_end , edge_end ])
    adj[edge_end].append([cost_end_start , edge_start ])

def solution( start ) :
    heapq_list = []
    answer = umul[start]
    chk = [False] * n 
    chk[start] = True
    cnt = 0

    for temp in adj[start] :
        cost , edge = temp
        heapq.heappush(heapq_list , (cost , edge) )

    while heapq_list :
        cost , edge = heapq.heappop(heapq_list)
        if cnt > n :
            break
        if chk[edge] :
            continue
        
        chk[edge] = True
        cnt += 1

        if cost > umul[edge] :
            answer += umul[edge]
            continue

        answer += cost
        for temp in adj[edge] :
            target_cost , target_edge = temp
            heapq.heappush ( heapq_list , ( target_cost , target_edge))
        
    for index ,value in enumerate(chk) :
        if not value :
            answer += umul[index]

    return answer

for i in range(n) :
    real_answer = min ( real_answer , solution(i) )

print ( real_answer )
