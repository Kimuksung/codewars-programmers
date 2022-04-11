# BOJ 2252번 - 줄 세우기
# Idea - 두 학생의 키를 보고 정렬 시켜야 한다.
# Edge간의 선후 관계 -> 위상 정렬

import sys
from collections import deque
input = sys.stdin.readline

n , m = map( int , input().split() )
adj = [[] for _ in range( n+1 )]
indegree = [0] * (n+1)
queue = deque()
answer = []

for _ in range( m ) :
    small , big = map ( int , input().split() )
    adj[small].append(big)
    indegree[big] += 1

for index , data in enumerate ( indegree[1:] ) :
    if not data :
        queue.append(index+1)

#print ( adj , indegree , queue )

while ( queue ) :
    temp = queue.popleft()
    answer.append(temp)
    for data in adj[temp] :
        indegree[data] -= 1
        if not indegree[data] :
            queue.append(data)
    
[print(temp) for temp in answer]
