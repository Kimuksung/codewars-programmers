#BOJ 16401번

import sys
input = sys.stdin.readline

n , m = map ( int , input().split() )
num_list = list( map(int,input().split()))
dp = [0]*1000001

left , right = 0 , max(num_list)
while left < right :
    middle = (left+right) // 2 + 1
    if sum( [num//middle for num in num_list]) >= n :
        left = middle
    else :
        right = middle-1

print(left)