from collections import deque

def solution(routes):
    answer = 0
    x,y = 0,1
    n = len(routes)
    start = [-30001,-30001]
    
    routes=deque(sorted( routes , key = lambda x:(x[0],x[1])))
    #print(routes)
    while routes :
        if start[y] < routes[0][x] :
            answer+=1
            start = routes.popleft()
        else:
            temp_x,temp_y = routes.popleft()
            start[y] = min(temp_y , start[y])
            
    return answer