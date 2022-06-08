#BOJ 1253번

import bisect

n=int(input())
datas = list(map(int,input().split()))
datas.sort()

answer = 0
i = 0
while i < n :
    left , right , target  = 0 , n-1 , datas[i]
    temp = 1
    while left < right :
        #예외 마이너스인경우
        # 5 / -4 -3 -2 -1 0
        if left == i :
            left += 1
            continue
        if right == i :
            right -= 1
            continue
        
        current = datas[left]+datas[right]
        if current == target :
            temp = bisect.bisect_right(datas,target) - i
            answer += temp
            break
        elif current > target :
            right -= 1
        else :
            left += 1
    i+=temp

print(answer)