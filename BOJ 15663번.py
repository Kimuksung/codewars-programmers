#BOJ  15663번

from copy import deepcopy

answer = set()
temp_data = []

n , m = map ( int , input().split() ) 
datas = list ( map ( int , input().split() ) )
datas.sort()

def recursion( number , datas ) :
    global answer
    if number == m :
        answer.add ( tuple ( deepcopy( temp_data ) ) )
        return
    
    for index , data in enumerate( datas ):
        temp_data.append( data )
        recursion( number+1 , deepcopy( datas[:index] + datas[index+1:]) ) 
        temp_data.pop()

recursion( 0 , datas )
answer = sorted ( answer )
[ print ( *answers ) for answers in answer ]           