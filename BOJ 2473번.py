#BOJ 2473번

import sys
input = sys.stdin.readline

n = int(input())
datas = list(map(int,input().split()))
datas.sort()
answer = []
current = 3000000001

for i in range(n) :
    temp = datas[:i]+datas[i+1:]
    start , end = 0 , n-2
    while start < end :
        target = datas[i]+temp[start]+temp[end]
        if current > abs(target) :
            answer = [datas[i],temp[start],temp[end]]
            current = abs(target)

        if target > 0 :
            end -= 1
        else :
            start += 1

answer.sort()
print(*answer)