def solution(citations):
    answer = 0
    citations.sort()
    citations=citations[::-1]
    n = len(citations)

    for i in range(n,-1,-1):
        if i <= len(list(filter(lambda x:x>=i , citations) )) :
            answer = i
            break
            
    return answer