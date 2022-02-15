
#idea = 치킨 집 나타낼 수 있는 모든 경우의 수를 표현 -> 모든 경우에 대해 치킨 거리를 구해본다.
from itertools import combinations
def chicken_street( x2 , y2 , x1 , y1 ) :
    return abs(x2-x1) + abs(y2-y1)

N , M = map ( int , input().split(' ') )

maps = [ [0] * N for _ in range ( N ) ]
homes = []
chicken = []
chicken_cnt = 0
answer = []

#preprocessing
for i in range( N ) :
    datas = list( map( int , input().split(' ') ) )
    for j in range( N ) :
        maps[i][j] = datas[j]
        if datas[j] == 1 :
            homes.append( [i,j] )
        if datas[j] == 2 :
            chicken.append( [i,j] )

# 치킨집 경우의 수
for j in range( 1 , M + 1 ) :
    for check_datas in list ( map ( list  , combinations( chicken , j) )  )  :
        min_datas = []
        for home in homes :
            min_data = 9999
            for check_data in check_datas :
                min_data = min ( min_data , chicken_street ( home[0] , home[1] , check_data[0] , check_data[1]) )
            min_datas.append(min_data)
        answer.append( sum(min_datas) )

print ( min ( answer ) )