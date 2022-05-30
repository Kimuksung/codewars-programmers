#BOJ 2457번

import sys
input = sys.stdin.readline

n = int(input())
datas = []

for _ in range(n) : 
    temp = list(map(int,input().split()))
    datas.append( (temp[0]*100+temp[1],temp[2]*100+temp[3]) )

datas.sort(key=lambda x:(x[0],x[1]))
start , end = 0,1
answer = 0
target = 301

while datas :
    #종료 조건
    if target >= 1201 or target < datas[0][start]:
        break  
    
    temp = 0
    for _ in range(len(datas)) :
        if datas[0][start] <= target :
            temp = max(temp , datas[0][end])
            datas.remove(datas[0])
        else :
            break
    target = temp
    answer += 1

if target < 1201:
    answer = 0
print(answer)