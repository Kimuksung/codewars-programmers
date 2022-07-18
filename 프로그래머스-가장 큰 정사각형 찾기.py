# Dynamic Programming
# 작은 문제 = 정사각형은 전의 값의 대각선 / 좌 / 상 중에서 가장 작은 정사각형
def solution(board):
    answer = 0
    row , column = len(board) , len(board[0])
    maps = [[0]*column for _ in range(row)]
    
    for i in range(row):
        if board[i][0] :
            maps[i][0]=1
            answer = 1
    for j in range(column):
        if board[0][j] :
            maps[0][j]=1
            answer = 1

    for i in range(1,row) :
        for j in range(1,column) :
            if board[i][j] :
                maps[i][j] = min(maps[i][j-1] , maps[i-1][j] , maps[i-1][j-1])+1
                if maps[i][j] > answer :
                    answer = maps[i][j]

    return answer*answer

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))