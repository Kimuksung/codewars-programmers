#BOJ 12100번

#상하좌우 움직이는 경우
from copy import deepcopy

n = int(input())
maps = [ list ( map(int , input().split() ) )for _ in range(n) ]
answer = 0

def change_data ( datas ) :
    stack = []
    value , check = 0 , 1
    for data in datas :
        if data == 0 :
            continue

        if stack :
            if not stack[-1][check] and stack[-1][value] == data :
                stack.pop()
                stack.append( (data*2,1) )
            else :
                stack.append( ( data ,0 ) )
        else :
            stack.append( (data,0) )
    return [stacks[value] for stacks in stack] + [0]* ( len(datas)  - len(stack) )

def move_right( maps ) :
    for row , map in enumerate( maps ) :
        for col , temp in enumerate ( change_data(map[::-1])[::-1] ) :
            maps[row][col] = temp
    return maps

def move_left( maps ) :
    for row , map in enumerate( maps ) :
        for col , temp in enumerate ( change_data(map) ) :
            maps[row][col] = temp
    return maps

def move_up( maps ) :
    for col in range( n ) :
        data = []
        for j in range ( n ) :
            data.append ( maps[j][col] )
        for row , temp in enumerate ( change_data( data ) ) :
            maps[row][col] = temp
    return maps

def move_down( maps ) :
    for col in range( n ) :
        data = []
        for j in range ( n ) :
            data.append ( maps[j][col] )      
        for row , temp in enumerate ( change_data( data[::-1] )[::-1] ) :
            maps[row][col] = temp
    return maps

def recursion( number , maps) :
    global answer
    if number == 5 :
        answer = max ( answer , max(map(max, maps))  )
        return
    
    recursion(number+1 , move_left( deepcopy(maps) ) )
    recursion(number+1 , move_right( deepcopy(maps) ) )
    recursion(number+1 , move_up( deepcopy(maps) ) )
    recursion(number+1 , move_down(maps) )

recursion( 0 , maps )

print ( answer )