#BOJ 14921번

n = int(input())
datas = list(map(int,input().split()))

start , end = 0 , n-1
answer = datas[start]+datas[end]

while start < end :
    temp = datas[start]+datas[end]
    if abs(temp) < abs(answer) :
        answer = temp
    if temp > 0 :
        end -= 1
    else :
        start += 1

print(answer)