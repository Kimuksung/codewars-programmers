import sys
from collections import deque

N = int(sys.stdin.readline())

deque_data = deque()

for i in range( N ) : 
    command = sys.stdin.readline().split()
    number = len(deque_data)
    if command[0] == 'push_front' :
        deque_data.appendleft(command[1])
    elif command[0] == 'push_back' :
        deque_data.append(command[1])
    elif command[0] == 'pop_front' :
        if  number != 0 :
            print ( deque_data.popleft() )
        else :
            print('-1')
    elif command[0] == 'pop_back' :
        if number != 0 :
            print ( deque_data.pop() )
        else :
            print('-1')
    elif command[0] == 'size' :
        print ( number )
    elif command[0] == 'empty' :
        if number == 0 :
            print ( '1' )
        else :
            print ( '0')
    elif command[0] == 'front' :
        if number != 0:
            temp = deque_data.popleft() 
            print ( temp )
            deque_data.appendleft ( temp )
        else :
            print ( '-1')
    elif command[0] == 'back' :
        if number != 0:
            temp = deque_data.pop() 
            print ( temp )
            deque_data.append ( temp )
        else :
            print ( '-1')