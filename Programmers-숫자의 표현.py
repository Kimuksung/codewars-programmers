# Programmers-숫자의 표현
import bisect
def solution(n):
    answer = 0
    cnt = 0
    datas=[]
    for i in range(n+1):
        cnt+=i
        datas.append(cnt)
    for right in range(1,n+1):
        target=datas[right]-n
        if target<0:
            continue
            
        if datas[bisect.bisect_left(datas,target)]==target:
            answer+=1
    return answer

def solution(n):
    answer = 0
    datas = [i for i in range(n+1)]
    left=0
    current=0
    for right in range(1,n+1):
        current+=datas[right]
        if current==n:
            answer+=1
            continue
        while current > n :
            current-=datas[left]
            if current==n:
                answer+=1
            left+=1

    return answer