def solution(clothes):
    answer = 1
    data=dict()
    
    for items in clothes :
        if items[1] not in data :
            data[items[1]] = 1
        data[items[1]] += 1
    
    for t in data.values() :
        answer*=t
    
    return answer-1