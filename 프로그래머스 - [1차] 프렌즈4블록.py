#프로그래머스 - [1차] 프렌즈4블록

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
#board = ["---DE", "---DE", "CCBBF", "CCBBF"]
answer = 0
maps = [['0']*n for _ in range(m)]
dx , dy = [0,1,1] , [1,0,1]

#init
for i in range(m) :
    for j,data in enumerate(board[i]) :
        maps[i][j] = data
            
while True :  
    delete_arr = set()
    #find_delete_xy 
    for x in range(m-1) :
        for y in range(n-1) :
            if maps[x][y] == '-':
                continue
            check = True
            for t in range(3) :
                nx,ny= x+dx[t],y+dy[t]
                if maps[nx][ny] != maps[x][y] :
                    check = False
                    break
            
            if check :
                delete_arr.add((x,y))
                for t in range(3) :
                    nx,ny= x+dx[t],y+dy[t]
                    delete_arr.add((nx,ny))

    #종료조건                
    if not delete_arr :
        break
    #explose block
    for arr in delete_arr :
        maps[arr[0]][arr[1]]='0'
    answer += len(delete_arr)

    for y in range(n) :
        for x in range(m-1,-1,-1) :
            while maps[x][y] == '0' :
                for t in range(x,0,-1) :
                    maps[t][y] = maps[t-1][y]
                maps[0][y] = '-'        

print(answer)