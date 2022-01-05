def solution(arr):
    answer = []
    
    for data in arr :
        if answer[-1:] != [data] :
            answer.append(data)
        
    return answer