
from collections import deque
from tabnanny import check

def dfs ( target ) :
    stack = []
    stack.append( maps[target] )
    visited = [False] *(n+1)
    visited[maps[target]] =True

    while stack :
        current = stack.pop()
        if current == target :
            for index , visit in enumerate( visited ) :
                if visit :
                    check_list[index] = True
            return True

        if not visited[maps[current]] :
            visited[maps[current]] = True
            stack.append( maps[current])
        else : 
            break

    return False

m = int(input())
for _ in range( m ) :
    n = int( input() )
    maps = [list( map ( int , input().split() ) )

    check_list = [False] * (n+1)

    cnt = 0
    for i in range( 1, n+1 ) :
        if not check_list[i] :
            if not dfs(i) :
                print ( 'i:' , i )
                cnt += 1

    print ( cnt )
