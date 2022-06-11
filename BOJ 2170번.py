#BOJ 2170번

import heapq
import sys
input = sys.stdin.readline

answer = 0
start , end = -1000000001 , -1000000001

n = int(input())
q = []

for _ in range(n) :
    x1,x2 = map(int,input().split())
    heapq.heappush(q,(x1,x2))

while q :
    x1 , x2 = heapq.heappop(q)
    if x1 > end :
        answer += end-start
        start , end = x1 , x2
        continue
    if start > x1 :
        start = x1
    if end < x2 :
        end = x2

answer += end-start
print(answer )
