import sys
input = sys.stdin.readline

n = int(input())
number_list = [0]+list(map(int,input().split()))

for i in range(1,n+1):
    number_list[i]=max(number_list[i-1]+number_list[i],number_list[i])

print(max(number_list[1:]))