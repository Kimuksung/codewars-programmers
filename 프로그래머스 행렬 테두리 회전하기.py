import copy
def rotate90 ( map , x1 , y1 , x2 , y2 ) :
    start = map[x1][y1]
    min_data = start

    for i in range ( x1 , x2 ) : #좌측
        map[i][y1] = map[i+1][y1]
        min_data = min ( min_data , map[i+1][y1] )
    for i in range ( y1 , y2 ) : #하단
        map[x2][i] = map[x2][i+1]
        min_data = min ( min_data , map[x2][i+1] )
    for i in range ( x2 , x1 , -1 ) : #우측
        map[i][y2] = map[i-1][y2]
        min_data = min ( min_data , map[i-1][y2] )
    for i in range ( y2, y1 , -1 ) : #상단
        map[x1][i] = map[x1][i-1]
        min_data = min ( min_data , map[x1][i-1] )

    map[x1][y1+1] = start
    return map , min_data

def solution(rows, columns, queries) :
    answer = []
    maps = [[0] * columns for _ in range (rows ) ]
    cnt = 1
    for row in range ( rows ) :
        for column in range ( columns ) :
            maps[row][column] = cnt
            cnt += 1

    for query in queries :
        x1 , y1 , x2 , y2 = query
        maps , min_data = rotate90 ( maps , x1-1 , y1-1 , x2-1 , y2-1 )
        answer.append(min_data)

    return answer
