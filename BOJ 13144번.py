#BOJ 13144번

import sys
input = sys.stdin.readline

n = int(input())
datas = list(map(int,input().split()))

answer = 0
right = 0
number = [0]*(100001)

for i in range(n) : # i = left
    for j in range(right,n) :
        if number[datas[j]] :
            break
        else :
            number[datas[j]] = 1
            right += 1
    answer += right-i
    number[datas[i]]=0

print(answer)