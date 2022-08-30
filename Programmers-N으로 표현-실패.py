# Programmers-N으로 표현 2

from collections import deque
import sys
size = 300000
def solution(N, number):
    answer = -1
    dp = [sys.maxsize]*(size+1)
    dp[N] = 1 

    q = deque()
    q.append((N,1))
    if N==number:
        return 1

    while q :
        current,cnt=q.popleft()
        
        if current==number:
            return cnt
        if cnt>=8:
            continue
        
        #1. 곱셈
        if current*N <= size and dp[current*N]>cnt+1 :
            q.append((current*N,cnt+1))
        #2. 나눗셈
        if current%N == 0 and dp[current//N]>cnt+1 :
            q.append((current//N,cnt+1))
        #3. 빼기
        if current-N >= 0 and dp[current-N]>cnt+1:
            q.append((current-N,cnt+1))
        #4. 덧셈
        if current+N <= size and dp[current+N]>cnt+1:
            q.append((current+N,cnt+1))
        #5. 숫자 붙이기
        if int(str(current)+str(N)) <= size and dp[int(str(current)+str(N))]>cnt+1:
            q.append((int(str(current)+str(N)),cnt+1))
    return answer

N=5
number=80
print( solution(N,number) )