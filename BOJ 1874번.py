# BOJ 1874번

import sys
from collections import deque
input = sys.stdin.readline

n = int ( input() )
origin = [i for i in range(1 , n+1)]
target_data = deque()
stack = []
answer = []

for _ in range( n ) :
    target_data.append( int(input()) )

for temp in origin :
    stack.append(temp)
    answer.append('+')

    while stack and target_data :
        if stack[-1] == target_data[0] :
            answer.append('-')
            stack.pop()
            target_data.popleft()
        else :
            break

if target_data :
    print ( 'NO')
    exit()

print ( *answer )

