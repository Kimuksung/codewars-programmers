import copy
N , M =  map ( int , input().split(' ') )

# map , cctv 설정
maps = [ [0] * M for _ in range(N) ]
cctv_cnt = 0 
answer_list = []

for i in range ( N ) :
    data = list ( map ( int , input().split(' ') ) ) 
    for j in range( M ) :
        maps[i][j] = data[j]
        if data[j] in ( 1,2,3,4,5 ) :
            cctv_cnt += 1

# 모든 CCTV는 4가지의 경우의 수
# 4^k
def all_target ( cctv_cnt ) :
    answer = []
    for i in range ( 1<<cctv_cnt*2 ) :
        temp = i
        target_data = ''
        for j in range( cctv_cnt ) :
            target_data = str ( temp % 4 ) + target_data
            temp //= 4
        answer.append( target_data )
    return answer

def move_up ( x , y , maps ) :
    for i in range ( x , 0 - 1 , -1 ) :
        if maps[i][y] == 0 :
            maps[i][y] = '#'
        elif maps[i][y] == 6 :
            break
    return maps

def move_down ( x , y , maps ) :
    for i in range ( x , N ) :
        if maps[i][y] == 0 :
            maps[i][y] = '#'
        elif maps[i][y] == 6 :
            break

def move_right ( x, y , maps ) :
    for j in range ( y , M ) :
        if maps[x][j] == 0 :
            maps[x][j] = '#'
        elif maps[x][j] == 6 :
            break

def move_left ( x, y , maps ) :
    for j in range ( y , 0 -1 , -1 ) :
        if maps[x][j] == 0 :
            maps[x][j] = '#'
        elif maps[x][j] == 6 :
            break        

# 경우의 수와 현재 리스트를 던져주어 몇개의 output인지 출력
def sum_zero ( N , M , maps , target ) :
    target_cnt = 0 
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if maps[i][j] in (1,2,3,4,5) :
                # 여기서부터 찾아 들어가는 구문 만들면 된다
                if target[target_cnt] == '0' :
                    if maps[i][j] == 1 : # 상
                        move_up( i , j , maps )
                    elif maps[i][j] == 2 : # 상하
                        move_up( i , j , maps )
                        move_down( i , j , maps )
                    elif maps[i][j] == 3 : # 상우
                        move_up( i , j , maps )
                        move_right( i , j , maps )
                    elif maps[i][j] == 4 : #좌상우
                        move_left( i , j , maps )
                        move_up( i , j , maps )
                        move_right( i , j , maps )
                    elif maps[i][j] == 5 : # 모두
                        move_left( i , j , maps )
                        move_up( i , j , maps )
                        move_right( i , j , maps )
                        move_down( i , j , maps )
                if target[target_cnt] == '1' :
                    if maps[i][j] == 1 : # 하
                        move_down( i , j , maps )
                    elif maps[i][j] == 2 : # 상하
                        move_up( i , j , maps )
                        move_down( i , j , maps )
                    elif maps[i][j] == 3 : # 우하
                        move_right( i , j , maps )
                        move_down( i , j , maps )
                    elif maps[i][j] == 4 : #상우하
                        move_up( i , j , maps )
                        move_right( i , j , maps )
                        move_down( i , j , maps )
                    elif maps[i][j] == 5 : # 모두
                        move_left( i , j , maps )
                        move_up( i , j , maps )
                        move_right( i , j , maps )
                        move_down( i , j , maps )
                if target[target_cnt] == '2' :
                    if maps[i][j] == 1 : # 좌
                        move_left( i , j , maps )
                    elif maps[i][j] == 2 : # 좌우
                        move_left( i , j , maps )
                        move_right( i , j , maps )
                    elif maps[i][j] == 3 : # 좌하
                        move_left( i , j , maps )
                        move_down( i , j , maps )
                    elif maps[i][j] == 4 : #좌우하
                        move_left( i , j , maps )
                        move_right( i , j , maps )
                        move_down( i , j , maps )
                    elif maps[i][j] == 5 : # 모두
                        move_left( i , j , maps )
                        move_up( i , j , maps )
                        move_right( i , j , maps )
                        move_down( i , j , maps )
                if target[target_cnt] == '3' :
                    if maps[i][j] == 1 : # 우
                        move_right( i , j , maps )
                    elif maps[i][j] == 2 : # 좌우
                        move_left( i , j , maps )
                        move_right( i , j , maps )
                    elif maps[i][j] == 3 : # 좌상
                        move_left( i , j , maps )
                        move_up( i , j , maps )
                    elif maps[i][j] == 4 : #좌상하
                        move_left( i , j , maps )
                        move_up( i , j , maps )
                        move_down( i , j , maps )
                    elif maps[i][j] == 5 : # 모두
                        move_left( i , j , maps )
                        move_up( i , j , maps )
                        move_right( i , j , maps )
                        move_down( i , j , maps )
                target_cnt += 1
    return ( sum ( [1 for i in range(N) for j in range(M) if maps[i][j] == 0 ] ) )

for data in all_target(cctv_cnt) :
    answer_list.append( sum_zero ( N , M , copy.deepcopy(maps) , data ) )

print ( min( answer_list ) )
    