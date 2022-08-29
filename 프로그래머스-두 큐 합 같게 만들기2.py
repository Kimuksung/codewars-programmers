from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1=deque(queue1)
    queue2=deque(queue2)
    q1 = sum(queue1)
    q2 = sum(queue2)
    while queue2 and queue1 :
        if answer > 600000:
            return -1
        if q1==q2:
            return answer
            
        elif q1 < q2 :
            q1+=queue2[0]
            q2-=queue2[0]
            queue1.append(queue2.popleft())
        else:
            q2+=queue1[0]
            q1-=queue1[0]
            queue2.append(queue1.popleft())
        answer+=1
    
    if not queue1 or not queue2:
        answer=-1
    return answer