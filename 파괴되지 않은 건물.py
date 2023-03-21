def solution(board, skill):
    answer = 0
    
    #누적합
    n = len(board)
    m = len(board[0])
    mapping = [[0]*(m+1) for _ in range(n+1)]
    
    for type,x1,y1,x2,y2,degree in skill:
        mapping[x1][y1]+= -degree if type==1 else degree
        mapping[x1][y2+1]+= degree if type==1 else -degree
        mapping[x2+1][y1]+= degree if type==1 else -degree
        mapping[x2+1][y2+1]+= -degree if type==1 else +degree

    #row sum
    for x in range(n):
        for y in range(1,m):
            mapping[x][y]+=mapping[x][y-1]
    
    #col sum
    for y in range(m):
        for x in range(1,n):
            mapping[x][y]+=mapping[x-1][y]

    for x in range(n):
        for y in range(m):
            board[x][y]+=mapping[x][y]
            if board[x][y]>0:
                answer+=1   
    
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
solution(board, skill)