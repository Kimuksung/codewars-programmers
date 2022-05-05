#BOJ 2910번

import heapq
import sys
input = sys.stdin.readline

dict_data = dict()
answer = []
n , c = map ( int , input().split() )
datas = list ( map ( int , input().split() ) )

for index , data in enumerate( datas ) :
    if data in dict_data :
        dict_data[data][1] += 1
    else :
        dict_data[data] = [data , 1 , index+1]

for index , value in dict_data.items() :
    heapq.heappush( answer , ( -value[1] , value[2] , value[0] ) )

while answer :
    frequency , _ , value =  heapq.heappop(answer)
    for _ in range( -1*frequency ) :
        print ( value )