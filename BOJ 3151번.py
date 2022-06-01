#BOJ 3151번
from bisect import bisect_left
import sys
input = sys.stdin.readline
answer = 0

n = int(input())
datas = list(map(int,input().split()))
datas.sort()

for i in range(n-2) :
    left , right = i+1 , n-1
    while left < right :
        temp = datas[i] + datas[left] + datas[right]
        if temp > 0 :
            right -= 1
        else :
            if temp == 0 :
                if datas[left] == datas[right] :
                    answer += right - left
                else :
                    answer += right - bisect_left( datas , datas[right]) + 1
            left += 1
            
print(answer)