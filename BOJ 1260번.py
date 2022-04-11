# 실수한 부분
# Dict 접근 시 Index 설정값 안주었다!
# 백준인데 프로그래머스 출력 식으로 해버림 ㅇㅅㅇ;
import sys
from collections import deque
input = sys.stdin.readline

dfs_answer = []

def dfs ( graph , visited , start ) :
    dfs_answer.append(start)
    visited[start] = 1
    if start in graph :
        graph[start].sort()
        for data in graph[start] :
            if visited[data] :
                continue
            dfs ( graph , visited , data )  

    return dfs_answer

def bfs ( graph , start , visited) :
    answer = []
    queue = deque()
    queue.append( start )
    visited[start] = True

    while ( queue ) :
        temp = queue.popleft()
        answer.append( temp )

        if temp in graph :
            for data in graph[temp] :
                if visited[data] :
                    continue
                visited[data] = True
                queue.append(data)
            
    return answer

def solution( ) :
    n , m , start = map ( int , input().split() )
    graph = dict()
    
    for _ in range( m ) :
        u , v = map ( int ,input().split() )
        if u in graph :
            graph[u].append( v )
        else :
            graph[u] = [v]
        
        if v in graph :
            graph[v].append( u )
        else :
            graph[v] = [u]

    #DFS
    print ( ' '.join ( str(x) for x in dfs ( graph , [False]* ( n + 1 ) , start ) ) )
    #VFS
    print ( ' '.join ( str(x) for x in bfs ( graph , start , [False]* ( n + 1 ) ) ) )

solution()
