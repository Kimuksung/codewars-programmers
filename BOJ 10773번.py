# BOJ 10773번

import sys
input = sys.stdin.readline

stack = []
n = int ( input() )
for _ in range ( n ) :
    temp = int(input())
    if not temp :
        stack.pop()
        continue
    stack.append(temp)

print ( sum(stack) )
