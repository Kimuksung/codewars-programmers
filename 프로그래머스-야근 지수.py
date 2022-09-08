# Idea = Heap 을 이용한 Max 시간을 제거

import heapq
def solution(n, works):
    answer = 0
    works = [-work for work in works ]
    heapq.heapify( works )

    for _ in range(n) :
        time = -heapq.heappop(works)
        if time == 0 :
            break
        heapq.heappush(works,-(time-1))
    
    return sum(list(map(lambda x:x*x , works)))

works = [4, 3, 3]
n = 4 
print( solution(n, works) )