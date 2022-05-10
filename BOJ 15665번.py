#BOJ 15665번

import sys
from copy import deepcopy
input = sys.stdin.readline

answer = set()
data_list = []
n , m = map( int , input().split() )
datas = list( map ( int , input().split() ) )

def recursion( number )  :
    if number == m :
        answer.add( deepcopy( tuple(data_list) ) )
        return

    for data in datas :
        data_list.append(data)
        recursion(number+1)
        data_list.pop()

recursion(0)
answer = sorted( list(answer) )
[ print ( *answers ) for answers in answer ] 
