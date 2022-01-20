from collections import deque
def check_bfs ( start_x , start_y , maps) :
    que = deque()
    dx , dy = [0,0,-1,1] , [-1,1,0,0]
    que.append( [start_x,start_y,0])
    
    while(que) :
        x , y , num = que.popleft()
        for i in range ( 4 ) :
            nx , ny , nnum = x + dx[i] , y + dy[i] , num + 1
            if 0<= nx < 5 and 0<= ny < 5 and ( nx != start_x or ny!= start_y ) and nnum <= 2 :
                if maps[nx][ny] == 'X' : 
                    continue
                elif maps[nx][ny] == 'P' :
                    return False
                else :
                    que.append([nx,ny,nnum])
    return True

def solution ( places ) :
    answer = []
    for place in places :
        answer_bool = True
        for i in range(5) :
            for j in range(5) :
                if place[i][j] == 'P' :
                    answer_bool = answer_bool and check_bfs ( i , j , place)
        answer.append(1 if answer_bool else 0)
    return answer
