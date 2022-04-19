#BOJ 3968번

import sys
input = sys.stdin.readline

n = int(input())
answer = 0

for _ in range( n ) :
    char_datas = input().rstrip()
    stack = []

    for char_data in char_datas :
        if stack and stack[-1] == char_data :
            stack.pop()
            continue
        stack.append(char_data)

    if not stack :
        answer += 1

print ( answer )
    