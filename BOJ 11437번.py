#BOJ 11437번
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

answer = []
n = int(input())
graphs = [[] for _ in range(n+1)]
depth = [0] * (n+1)
parent = [0] * (n+1)
visited = [0] * (n+1)

for _ in range(n-1) :
    start,end = map(int,input().split() )
    graphs[start].append(end)
    graphs[end].append(start)

# depth and parent set
def dfs(start,level):
    visited[start]=1
    depth[start]=level

    for move in graphs[start]:
        if not visited[move] :
            parent[move]=start
            visited[move]=1
            depth[move]=level+1
            dfs(move,level+1)

dfs(1,0)

def lca(a,b):
    # level을 맞추어 준다.
    while depth[a] != depth[b]:
        if depth[a]<depth[b]:
            b=parent[b]
        else:
            a=parent[a]
    # 상위 Node 탐색
    while a!=b:
        a , b = parent[a] , parent[b]
    return a     

m = int(input())
for _ in range(m) :
    a,b = map(int,input().split())
    answer.append( lca(a,b) )

print( *answer)
