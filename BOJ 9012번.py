# BOJ 9012번

import sys
input = sys.stdin.readline

n = int(input())
answer = []

for _ in range ( n ) :
    stack = []
    check = False
    char_datas = input().rstrip()
    for char_data in char_datas :
        if char_data == '(' :
            stack.append( '(' )
        elif stack and stack[-1] == '(' :
            stack.pop()
        else :
            check = True
            break

    if stack or check :
        answer.append('NO')
        continue
    answer.append('YES')

print ( *answer )