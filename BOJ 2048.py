# idea = 재귀로 단계를 나타내어 풀어야 할듯
# 각 단계별로 0 , 1 , 2, 3 한번씩 호출하고 자기 자신 다시 호출

import copy

answer = []
N = int ( input() )

maps = [[0] * N for _ in range (N)]

for i in range( N ) :
    data = list(map ( int , input().split(' ') ) )
    for j in range ( N ) :
        maps[i][j] = data[j]
    
#[ print ( map) for map in maps ]

def move_map ( maps , direct ) :
    if direct == '0' : # 상
        for y in range ( N ) :
            for x in range( N -1 ) :
                for start_x in range( x + 1 , N ) :
                    if maps[start_x][y] == 0:
                        continue
                    
                    elif maps[x][y] == maps[start_x][y] :
                        maps[x][y] *= 2
                        maps[start_x][y] = 0
                        break
                    
                    if maps[x][y] == 0  :
                        maps[x][y] = maps[start_x][y]
                        maps[start_x][y] = 0
                        break


    if direct == '1' : # 하
        for y in range ( N ) :
            for x in range( N -1 , 1 -1 , -1 ) :
                for start_x in range( x - 1  , 0-1 , -1 ) :
                    if maps[start_x][y] == 0:
                        continue
                    if maps[x][y] == 0  :
                        maps[x][y] = maps[start_x][y]
                        maps[start_x][y] = 0
                        break
                    elif maps[x][y] == maps[start_x][y] :
                        maps[x][y] *= 2
                        maps[start_x][y] = 0
                        break
                    else :
                        break

    if direct == '2' : # 좌
        for x in range ( N ) :
            for y in range( N-1 ) :
                for start_y in range( y + 1 , N ) :
                    if maps[x][start_y] == 0:
                        continue
                    if maps[x][y] == 0  :
                        maps[x][y] = maps[x][start_y]
                        maps[x][start_y] = 0
                        break
                    elif maps[x][y] == maps[x][start_y] :
                        maps[x][y] *= 2
                        maps[x][start_y] = 0
                        break
                    else :
                        break
                    
    if direct == '3' : # 우
        for x in range ( N ) :
            for y in range( N-1 , 0 , -1 ) :
                for start_y in range( y-1, 0-1 ,-1) :
                    if maps[x][start_y] == 0:
                        continue
                    if maps[x][y] == 0  :
                        maps[x][y] = maps[x][start_y]
                        maps[x][start_y] = 0
                        break
                    elif maps[x][y] == maps[x][start_y] :
                        maps[x][y] *= 2
                        maps[x][start_y] = 0
                        break
                    else :
                        break
    return maps

def all_target ( cnt ) : #4진법 경우의 수 나타내기
    answer = []
    for i in range ( 1<<cnt*2 ) :
        temp = i
        target_data = ''
        for _ in range( cnt ) :
            target_data = str ( temp % 4 ) + target_data
            temp //= 4
        answer.append( target_data )
    return answer

#print ( all_target( 5 ) ) 

for targets in all_target( 5 ) :
    temps = copy.deepcopy(maps)
    for target in targets :
        temps = move_map(temps , target)

    max_data = temps[0][0]
    for i in range(N) :
        for j in range(N) :
            max_data = max(temps[i][j] , max_data )
    answer.append(max_data)

print ( max(answer) )
