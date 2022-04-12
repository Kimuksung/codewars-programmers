# BOJ 3273번

import sys
input = sys.stdin.readline

num_list = [False] * 1000001
n = int( input() )
data = map(int , input().split())
x = int(input() )
answer = 0

for i in data :
    num_list[i] = True

for index , value in enumerate( num_list ) :
    if x-index <= 1000000 and value and num_list[x-index] :
        answer += 1

print ( answer//2 )