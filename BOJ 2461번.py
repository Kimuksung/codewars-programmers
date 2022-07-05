#BOJ 2461번

import heapq
import sys

n , m = map(int,input().split())
check_list = [1]*(1001)
max_value = 0
all_number = []
datas = []
answer = sys.maxsize

for i in range(n) :
    temp = sorted(list(map(int,input().split())))
    max_value=max(temp[0],max_value)
    datas.append([])
    datas[i]=temp

    heapq.heappush(all_number,(temp[0],i))

while all_number :
    number , idx = heapq.heappop(all_number)
    min_value = number

    #print(number , max_value , min_value )
    answer = min(answer,max_value-min_value)
    if check_list[idx] == m :
        break
    heapq.heappush(all_number,(datas[idx][check_list[idx]],idx))
    max_value = max(max_value,datas[idx][check_list[idx]])
    check_list[idx]+=1

print(answer)