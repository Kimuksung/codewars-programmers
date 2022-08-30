# Programmers-디스크 컨트롤러
from collections import deque
import heapq
def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs=deque( sorted(jobs,key=lambda x:(x[0],x[1])) )
    q = []
    current = 0
    
    while jobs :
        # current에 맞추어 Data 추가
        while jobs and jobs[0][0] <=current :
            start,time=jobs.popleft()
            heapq.heappush(q,(time,start))
        
        # 가장 빨리 실행되어야 할 Data
        if q :
            time,start= heapq.heappop(q)
            current+=time
            answer+=current-start
            
        # Q에 값이 없다면
        else :
            current=jobs[0][0]
    
    while q :
        time,start= heapq.heappop(q)
        current+=time
        answer+=current-start
        
    return answer//n