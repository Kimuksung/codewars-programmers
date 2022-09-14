def solution(routes):
    answer = 0
    start = -30001

    routes = sorted( routes , key = lambda x:x[1])
    for route in routes :
        if start < route[0] :
            answer+=1
            start = route[1]
    return answer