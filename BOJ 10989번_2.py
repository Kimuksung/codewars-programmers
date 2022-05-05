#BOJ 10989번

import heapq
import sys
input = sys.stdin.readline

n = int(input())
num_list = [0] * 10001
heap = []
for _ in range(n) :
    num_list[int(input())] += 1

for index , value in enumerate(num_list) :
    if value == 0 :
        continue
    heapq.heappush( heap , (index , value) )

while heap :
    index , value = heapq.heappop(heap)
    for _ in range( value ) :
        print(index)