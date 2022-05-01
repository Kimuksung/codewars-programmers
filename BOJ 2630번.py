#BOJ 2630번

import sys
input = sys.stdin.readline

n = int(input())
maps = [ list( map ( int , input().split() ) ) for _ in range( n ) ] 
white_space , blue_space = 0 , 0

def answer ( x , y , n ) :
    global white_space , blue_space
    
    check = maps[x][y]
    for i in range ( x , x+n ) :
        for j in range ( y , y+n ) :
            if maps[i][j] != maps[x][y] :
                answer( x , y , n//2 )
                answer( x , y + n//2 , n//2 )
                answer( x + n//2 , y , n//2 )
                answer( x + n//2 , y+ n//2 , n//2 )
                return

    if check :
        blue_space += 1
    else :
        white_space += 1

answer( 0 , 0 , n )
print ( white_space , blue_space)