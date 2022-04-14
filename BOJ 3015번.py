#BOJ 3015번
# IDEA1. STACK을 이용
# Case1. 스택이 없는 경우 추가
# Case2. 스택이 있지만, 스택에 있는 값보다 작은 경우
# Case3. 스택이 있지만, 스택에 있는 값보다 큰 경우
# Case4. 스택이 있지만, 스택에 있는 값과 동일한 경우
# 참고 : https://velog.io/@morphine/BOJ.-3015-%EC%98%A4%EC%95%84%EC%8B%9C%EC%8A%A4-%EC%9E%AC%EA%B2%B0%ED%95%A9
import sys
input = sys.stdin.readline

answer = 0
n = int(input())
stack = []
height , cnt = 0 , 1
for _ in range( n ) :
    temp = int( input() )

    while stack and temp > stack[-1][height]:
        if temp > stack[-1][height] :
            answer += stack[-1][cnt]
            stack.pop()

    if not stack :
        stack.append( [temp,1] )
        continue

    elif temp < stack[-1][height] :
        answer += 1
        stack.append( [temp , 1])
    
    else :
        duplicate_cnt = stack[-1][cnt]
        answer += duplicate_cnt
        stack.pop()
        if stack :
            answer += 1
        stack.append( [temp,duplicate_cnt+1])
  
print ( answer )