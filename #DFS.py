#DFS
answer = 0
def dfs ( start , end , cnt , k , visited , adj ) :
    global answer
    if start == end :
        answer += 1
        visited[start] = 0
        return
    
    if cnt > k :
        return
    
    for temp in adj[start] :
        if visited[temp] :
            continue
        visited[temp] = 1
        dfs( temp , end , cnt+1 , k , visited , adj )

def solution(n, edges, k, a, b):
    adj = [[] for _ in range(n)]
    visited = [0] * n
    visited[a] = 1
    for edge in edges :
        first , second = edge
        adj[first].append(second)
        adj[second].append(first)

    dfs( a , b , 0 , k , visited , adj )

    return answer

print ( solution( 8 , [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]] , 4 , 0 , 3 ) )