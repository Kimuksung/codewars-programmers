#BOJ 2110번

import sys
input = sys.stdin.readline

n , target = map(int,input().split())
datas = sorted( [int(input()) for _ in range(n)] )

left , right = 1 , datas[-1]
answer = 1

# 신호 떨어지는 값을 이분탐색
while left <= right :
    gap = (left+right)//2

    cnt = 1
    before = datas[0]
    #갯수 세기
    for data in datas[1:]:
        if data-before >= gap :
            cnt += 1
            before = data
    #갯수는 들어오지만 범위안에 있을 수 있다.
    if cnt >= target :
        left = gap+1
        answer = gap
    else :
        right = gap-1

print(answer)