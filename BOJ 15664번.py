#BOJ 15664번

from copy import deepcopy

answer = set()
number_list = []
n , m = map( int , input().split() )

datas = list ( map ( int , input().split() ) )

def recursion ( number , datas) :
    if number == m :
        answer.add( tuple( deepcopy( number_list ) ) )
        return
    
    for index , data in enumerate( datas ) :
        if not number_list or ( number_list and number_list[-1] <= data ) :
            number_list.append( data )
            recursion ( number+1 , deepcopy( datas[:index] + datas[index+1:]))
            number_list.pop()

recursion( 0 , datas )

answer = sorted( answer )
[ print( *answers ) for answers in answer ]