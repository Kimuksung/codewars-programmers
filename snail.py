def solution(array):
    direction = [ [0,1] , [1,0] , [0,-1] , [-1 ,0] ] # 동남서북으로 움직인다 생각 
    answer = []
    
    # 없는 경우
    if array == []:
        return []
    
    n = len(array)
    check = [[0 for i in range(n)] for i in range(n)] # 확인용
    idx , cnt , x, y = 0 , 1 , 0 , 0
    check[x][y] = 1
    answer.append(array[x][y])

    while ( cnt < n*n ) :
        if n > x + direction[idx][0] >= 0 and n > y + direction[idx][1] >= 0 and check[x + direction[idx][0]][y + direction[idx][1]] == 0: # 범위 + 확인
            x , y = x + direction[idx][0] , y + direction[idx][1]
            check[x][y] = 1
            answer.append( array[x][y] )
            cnt += 1
        else :
            idx += 1
            idx = idx % 4

    return answer
solution ( [[1,2,3],
         [8,9,4],
         [7,6,5]])

