import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    first_min = heapq.heappop(scoville)
    
    while first_min < K and scoville != []:
        answer = answer + 1
        second_min = heapq.heappop(scoville)
        heapq.heappush(scoville , first_min + second_min * 2 )
        first_min = heapq.heappop(scoville)
    
    if scoville == [] and first_min < K:
        return -1
    heapq.heappush(scoville , first_min )
    return answer

print ( solution( [1,1,100] , 4) )  