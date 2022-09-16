from collections import defaultdict
def solution(tickets):
    stack = ['ICN']
    path = []
    route = defaultdict(list)
    # edge 표현
    for start,end in tickets:
        route[start].append(end)
    # edge가 갈 수 있는 값들 중 작은 값을 뒤에 두어 적용
    for value in route.values():
        value=value.sort(reverse=True)
    
    while stack :
        current=stack[-1]
        if not route[current]:
            path.append(stack.pop())
            
        else:
            stack.append(route[current].pop())
            
    return path[::-1]

#tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN","B"],["ICN","C"],["C","ICN"]]
print( solution(tickets) )