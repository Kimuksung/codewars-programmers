#Programmers-최솟값 만들기
import heapq
def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    heapq.heapify(B)
    
    for a in A :
        answer+=a*heapq.heappop(B)
    return answer