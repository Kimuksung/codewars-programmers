# Programmers-순위
def solution(n, results):    
    # Init
    win_graph = [ set() for _ in range(n+1)]
    lose_graph = [ set() for _ in range(n+1)]
    
    for start,end in results:
        win_graph[start].add(end)
        lose_graph[end].add(start)
        
    for i in range(1,n+1):
        # 1. i번 Node가 이기는 Node들은 i가 진 Node들과 다 연결
        for winner in lose_graph[i]:
            win_graph[winner].update(win_graph[i])
        
        # 2. i번 Node가 지는 Node들은 i가 이긴 Node들과 다 연결
        for loser in win_graph[i]:
            lose_graph[loser].update(lose_graph[i])
    
    # Edge가 n-1개로 연결되어 있다면 순위로 나타나는 것이 가능
    return sum( [1 for i in range(1,n+1) if len(win_graph[i])+len(lose_graph[i])==n-1 ] )