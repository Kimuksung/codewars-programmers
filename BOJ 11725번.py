import sys
from collections import deque
input = sys.stdin.readline

n = int( input() )
adj = [[] for _ in range (n+1)]
parent = [0 for _ in range (n+1)]

for _ in range(n-1) :
    first , second = map(int , input().split() )
    adj[first].append(second)
    adj[second].append(first)

def bfs ( start ) :
    queue = deque()
    queue.append(start)

    while queue :
        temp = queue.popleft()
        for target in adj[temp] :
            if parent[temp] == target :
                continue
            parent[target] = temp
            queue.append(target)
    return parent

[print(temp) for temp in bfs ( 1 )[2:] ]