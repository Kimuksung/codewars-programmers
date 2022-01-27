N = int ( input() )

maps = [ [0] * N for _ in range ( N ) ]
choice = [0] * N 
def solution ( num ) :
    if num == N :
        return
    
    for i in range ( N ) :
        if not maps[num][i] :
            choice[num] = 1
solution ( 0 )