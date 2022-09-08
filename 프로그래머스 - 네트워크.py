from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0]*n
    graphs = [[] for _ in range(n) ]
    
    # Init graphs
    for i , computer in enumerate(computers) :
        for j , value in enumerate(computer) : 
            if i==j :
                continue
            if value == 1:
                graphs[i].append(j)
    #Node
    for i in range(n):
        # 방문 한적이 없는 경우 새로운 Network 연결
        if not visited[i] :
            answer+=1
            q = deque()
            visited[i]=1
            for data in graphs[i] :
                q.append(data)
            
            # Network 연결
            while q :
                data = q.popleft()
                if not visited[data] :
                    visited[data]=1
                    for value in graphs[data] :
                        q.append(value)     
    return answer