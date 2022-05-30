#BOJ 2467번

import sys
input = sys.stdin.readline

n = int(input())
datas = list(map(int,input().split()))

current , answer = sys.maxsize , ()
left , right = 0 , n-1

while left < right :
    temp = datas[left]+datas[right]
    if abs(temp) < current :
        current = abs(temp)
        answer = (datas[left],datas[right])

    if temp < 0 :
        left += 1
    else :
        right -= 1

print( *answer )