#BOJ 21939번

import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

min_heap = []
max_heap = []
num_list = defaultdict(bool)
#answer = []

n = int(input())
for _ in range(n) :
    p , l = map(int,input().split())
    heapq.heappush(min_heap,(l,p))
    heapq.heappush(max_heap,(-l,-p))
    num_list[p] = True

m = int(input())
for _ in range(m) :
    cmd = input().split()
    if cmd[0] == 'add' :
        p , l = int(cmd[1]),int(cmd[2])

        while not num_list[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        while not num_list[min_heap[0][1]]:
            heapq.heappop(min_heap)

        heapq.heappush(min_heap,(l,p))
        heapq.heappush(max_heap,(-l,-p))
        num_list[p] = True

    elif cmd[0] == 'recommend' :
        if cmd[1] == '1' :
            while not num_list[-max_heap[0][1]] :
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
            #answer.append(-max_heap[0][1])

        else :
            while not num_list[min_heap[0][1]] :
                heapq.heappop(min_heap)
            print(min_heap[0][1])
            #answer.append(min_heap[0][1])

    elif cmd[0] == 'solved' :
        num_list[int(cmd[1])] = False
    
#print(answer)