#BOJ 2512번
import sys
input = sys.stdin.readline

n = int(input())
datas = list(map(int,input().split()))
max_value = int(input())

start , end = 0 , max(datas)

while start <= end : 
    mid = (start+end)//2
    sum_value = 0
    for data in datas :
        sum_value += min(data,mid)
    if sum_value > max_value :
        end = mid-1 
    else :
        start = mid+1
    
print(end)