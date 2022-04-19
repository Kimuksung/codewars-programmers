# BOJ 4949번

import sys
input = sys.stdin.readline
answer = []

while ( True ) :
    stack = []
    check = False
    char_list = input().rstrip()

    if char_list[0] == '.' :
        break

    for char_data in char_list :
        if char_data == '.' :
            break
        elif char_data == '(' :
            stack.append( '(' )
        elif char_data == '[' :
            stack.append( '[' )
        elif char_data == ')' :
            if stack and stack[-1] == '(' :
                stack.pop()
            else :
                check = True
                answer.append('no')
                break
        elif char_data == ']' :
            if stack and stack[-1] == '[' :
                stack.pop()
            else :
                check = True
                answer.append('no')
                break

    if check :
            continue

    if stack :
        answer.append( 'no' )
        continue
    answer.append( 'yes' )

print( *answer )