#BOJ 15666번

import sys
input = sys.stdin.readline

answer= set()
number_list = []
n , m = map ( int , input().split() )
datas = list ( set( map ( int , input().split() ) ) )

def recursion(number) :
    if number == m :
        answer.add( tuple( number_list) )
        return

    for data in datas :
        if not number_list or (number_list and number_list[-1] <= data ):
            number_list.append(data)
            recursion(number+1)
            number_list.pop()

recursion(0)
answer = sorted(list(answer))
[ print( *answers ) for answers in answer ]