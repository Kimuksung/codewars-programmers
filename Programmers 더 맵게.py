#Programmers 더 맵게

import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2 :
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first >= k and second >= k :
            break

        heapq.heappush(scoville,first+second*2)
        answer+=1

    if scoville and scoville[0] < k :
        answer=-1
    return answer

print(solution(scoville, K))