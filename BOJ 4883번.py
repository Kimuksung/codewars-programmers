#BOJ 4883번

from copy import deepcopy

def test_case( temp_datas ) :
    temp_datas[1][0] = temp_datas[1][0]+temp_datas[0][1]
    temp_datas[1][1] = min(temp_datas[1][0], temp_datas[0][1],temp_datas[0][1]+temp_datas[0][2])+temp_datas[1][1]
    temp_datas[1][2] = min(temp_datas[1][1],temp_datas[0][1],temp_datas[0][1]+temp_datas[0][2]) + temp_datas[1][2]

    for i in range(2,n) :
        for j in range(3) :
            if j == 0 :
                temp_datas[i][j] = min( temp_datas[i-1][j],temp_datas[i-1][j+1] ) + temp_datas[i][j]

            elif j == 1 :
                temp_datas[i][j] = min( temp_datas[i-1][j-1],temp_datas[i-1][j],temp_datas[i][j-1],temp_datas[i-1][j+1] ) + temp_datas[i][j]
        
            else :
                temp_datas[i][j] = min( temp_datas[i-1][j-1],temp_datas[i-1][j],temp_datas[i][j-1] ) + temp_datas[i][j]
    return temp_datas[n-1][1]

cnt = 0
while True :
    answer = []
    n = int(input())
    if n==0 :
        break
    temp_datas = [[] for _ in range(n)]

    for i in range(n) :
        temp_datas[i] = list(map(int,input().split()))

    cnt+=1
    print( f'{cnt}. {test_case( temp_datas )}')
    