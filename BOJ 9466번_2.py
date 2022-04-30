#BOJ 9466번

import sys
sys.setrecursionlimit(100000*2)

def dfs( start ) :
        global result
        visited[start] = True
        cycle.append(start)
        next = maps[start]

        if visited[next] :
            if next in cycle :
                result += cycle[cycle.index(next):] 
            else :
                return
        else :
            dfs(next)

answer = []
m = int( input() )

for _ in range(m) :
    n = int( input() )
    maps = ['0'] + list( map( int, input().split() ) )
    visited = [True] + [False]*n 
    cnt = n

    for i in range( 1, n+1) :
        result = []
        if not visited[i]:
            cycle = []
            dfs(i)
        cnt -= len(result)

    answer.append(cnt)
print( *answer )