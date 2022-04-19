#BOJ  5430번
'''
1
DDR
1
[2]

1
DDR
2
[2,1]

1
R
0
[]

1
D
0
[]
'''
from collections import deque

n = int(input())
answer = []

for _ in range( n ) :
    data = deque()
    check = True
    commands = input()
    num = int( input() )
    list_data = input()

    commands = commands.replace('RR' , '')
    #print ( 'test : ' , list_data.replace('[' , '').replace(']' , '').rstrip().split(','))
    data = deque( map ( str , list_data.replace('[' , '').replace(']' , '').split(',') ) )
    if data[0] == '' :
        data.popleft()

    for command in commands :
        if command == 'R' :
            data.reverse()
        elif command == 'D' :
            if len(data) > 0 :
                data.popleft()
            else :
                answer.append('error')
                check = False
                break

    if check :
        answer.append ( '[' + ','.join(data) +']' )

print ( *answer )