#BOJ 20922번

import sys
input = sys.stdin.readline 

n , k = map(int,input().split())
datas = list(map(int,input().split()))
a = [0]*100001

right , answer = 0 , 0

for i in range(n) :
    while right < n and a[datas[right]] < k :
        answer = max(answer,right-i+1)
        a[datas[right]] += 1
        right += 1

    a[datas[i]] -= 1
    
print(answer)