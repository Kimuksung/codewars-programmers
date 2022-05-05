#BOJ 14499번
from copy import deepcopy
from collections import deque

#dice = [0]*6
dice = [i for i in range(6)]
dx , dy = [0,0,0,-1,1] , [0,1,-1,0,0]
answer = []

n , m , x , y ,k = map( int , input().split() )
maps = [ list ( map( int , input().split() ) ) for _ in range(n) ]
dice_commands = deque ( map( int , input().split() ) )

def move ( direction ) :
    print ( 'direction :' , direction )
    if direction == 1 : #동쪽
        dice[4] , dice[5] , dice[3] , dice[1]  = dice[1] , dice[3] , dice[4] , dice[5]
    elif direction == 2 : #서쪽
        dice[5] , dice[4] , dice[1] , dice[3] = dice[1] , dice[3] , dice[4] , dice[5]
    elif direction == 3 :
        dice[:4] = dice[3:4] + dice[:3]
    elif direction == 4 : # 남쪽
        dice[:4] = dice[1:4] + dice[0:1]


move(4)
print ( dice )
'''
while dice_commands :
    print ( 'while :' , dice[1] , dice_commands[0] , x , y , dice )
    answer.append( ( dice[1] , dice_commands[0] , x , y , dice ) )
    if dice[3] == 0 :
        dice[3] = maps[x][y]
    command = dice_commands.popleft() 
    x , y = x+dx[command] , y+dy[command]
    move(command)

[ print(answers) for answers in answer ] 
'''