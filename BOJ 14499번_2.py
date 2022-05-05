#BOJ 14499번
# 주사위의 index 1번이 윗면

from copy import deepcopy
from collections import deque

dice = [0]*6
dx , dy = [0,0,0,-1,1] , [0,1,-1,0,0]

n , m , x , y ,k = map( int , input().split() )
maps = [ list ( map( int , input().split() ) ) for _ in range(n) ]
dice_commands = deque ( map( int , input().split() ) )

def move ( direction ) :
    if direction == 1 : #동쪽
        dice[5] , dice[4] , dice[1] , dice[3] = dice[1] , dice[3] , dice[4] , dice[5]
    elif direction == 2 : #서쪽
        dice[4] , dice[5] , dice[3] , dice[1]  = dice[1] , dice[3] , dice[4] , dice[5]
    elif direction == 3 :
        dice[:4] = dice[1:4] + dice[0:1]
    elif direction == 4 : # 남쪽
        dice[:4] = dice[3:4] + dice[:3] 

while dice_commands :
    move_data = dice_commands.popleft()
    if 0<= x+dx[move_data] < n and 0 <= y+dy[move_data] < m :
        move(move_data)
        print( dice[1] )
        x , y = x+dx[move_data] , y+dy[move_data]
        if maps[x][y] == 0 :
            maps[x][y] = dice[3]
        else :
            dice[3] = maps[x][y]
            maps[x][y] = 0