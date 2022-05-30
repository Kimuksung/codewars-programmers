# BOJ 11501번
# Idea
# 뒤에서부터 보면서 시작

import sys
input=sys.stdin.readline
k= int(input())

for _ in range(k) :
    answer = 0
    n = int(input())
    datas = list(map(int,input().split()))
    
    max_value = datas[-1]
    for index in range(n-2,-1,-1):
        if datas[index] > max_value :
            max_value = datas[index]
        else :
            answer += max_value-datas[index]
    
    print(answer )