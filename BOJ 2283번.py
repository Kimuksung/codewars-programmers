#BOJ 2283번
import sys
input = sys.stdin.readline

#init
answer = [0,0]
n , k = map(int,input().split())
number = [0]*1000001
right ,sum_value = 0 , 0

#input
for _ in range(n) :
    temp = tuple(map(int,input().split()))
    for i in range(temp[0],temp[1]):
        number[i]+=1

#two pointer
for i in range(1000001) : 
    #right 범위 지정
    while sum_value < k and right <= 1000000: 
        sum_value+=number[right]
        right+=1

    if sum_value == k :
        answer = [i,right]
        break
    sum_value-=number[i]

print(*answer)