#BOJ 14891번

answer = 0
traps = [ list ( map ( int , input()) ) for _ in range(4) ]

def turn_clock ( datas ) :
    return datas[-1:] + datas[:-1]

def turn_dclock( datas ) :
    return datas[1:] + list ( datas[:1] )

def sum_traps() :
    global answer
    for i in range( 4 ) :
        if traps[i][0]  : 
            answer += 2**i

k = int ( input() )

for _ in range( k ) :
    target , move_clock = map ( int , input().split() )

    turn_list = [0,0,0,0]
    if move_clock == -1 :
        turn_list[target-1] = -1
    else :
        turn_list[target-1] = 1

    # 좌측 부터
    current_clock = move_clock
    for i in range( target-1 , 0 , -1) :
        if not traps[i][-2] == traps[i-1][2] :
            if current_clock == -1 :
                turn_list[i-1] = current_clock *-1
            else :
                turn_list[i-1] = current_clock *-1
            current_clock *= -1
        else :
            break

    #우측
    current_clock = move_clock
    for i in range ( target-1 , 3 ) :
        if not traps[i][2] == traps[i+1][-2] :
            if current_clock == -1 :
                turn_list[i+1] = current_clock *-1
            else :
                turn_list[i+1] = current_clock *-1
            current_clock *= -1
        else :
            break
    
    for i in range( 4 ) :
        if turn_list[i] == -1 :
            traps[i] = turn_dclock(traps[i])
        elif turn_list[i] == 1 :
            traps[i] = turn_clock(traps[i])

sum_traps()
print ( answer )    
