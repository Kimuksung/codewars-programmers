# BOJ 5430번
# Idea 입력을 받아 Deque로 풀이
# 주의점 : reverse를 매번 하여 주면 O(N) 이 계속 처리 되어 차후에 한번에 처리
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
answer = []

for _ in range( n ) :
    reverse_check = False
    stop_check = False
    commands = input().rstrip()
    number = input()
    list_data = deque( input().rstrip().replace('[' , '').replace(']','').split(',') ) 

    if list_data[0] == '' :
        list_data.pop()

    for command in commands :
        if command == 'R' :
            reverse_check = not reverse_check
        elif command == 'D' :
            if list_data :
                if reverse_check :
                    list_data.pop()
                else :
                    list_data.popleft()
            else :
                answer.append( 'error')
                stop_check = True
                break

    if stop_check :
        continue

    if reverse_check :
        list_data.reverse()
        answer.append ( '['+ ','.join( list_data ) + ']' )
    else :
        answer.append( '[' + ','.join(list_data ) + ']' )

print ( *answer )