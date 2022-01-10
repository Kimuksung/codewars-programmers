import sys

from collections import deque
N = int(sys.stdin.readline())

answer = deque()
number = 0
for i in range( N ) : 
    command = sys.stdin.readline().split()
    if command[0] == 'push' :
        answer.append(command[1])
        number += 1

    if command[0] == 'pop' :
        if number == 0 :
            print(-1)
        else :
            print ( answer.pop() )
            if number > 0 :
                number -= 1
            
    if command[0] == 'size' :
        print ( number )
    if command[0] == 'empty' :
        if number == 0 :
            print(1)
        else:
            print(0)
    if command[0] == 'top' :
        if number ==0 :
            print( -1)
        else:
            temp = answer.pop()
            print(temp)
            answer.append(temp)

