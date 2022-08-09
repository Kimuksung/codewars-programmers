# Programmers-방문길이
def solution(dirs):
    answer= set()
    move=dict(zip(['U','L','R','D'],[(0,-1),(-1,0),(1,0),(0,1)]))

    x,y=0,0
    
    for dir in dirs :
        dx,dy=move[dir]
        nx,ny=x+dx,y+dy
        if -5<=y+dy<=5 and -5<=x+dx<=5:
            answer.add( (x,y,nx,ny) )
            answer.add( (nx,ny,x,y) )
            x,y=nx,ny

    return len(answer)//2

solution("ULURRDLLU")