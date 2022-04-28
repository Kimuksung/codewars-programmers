#BOJ 9663번

import sys
input = sys.stdin.readline 

n = int( input() )
visited = [0] * n 
cnt = 0

def checking ( index ) :
    for i in range(index) :
        if visited[i] == visited[index] :
            return False
        if index - i == abs ( visited[index] - visited[i] ) :
            return False
    return True

def dfs ( number ) :
    global cnt 
    if number == n : # 종료 조건
        cnt += 1
        return

    for i in range ( n ) :
        visited[number] = i
        if checking( number ) :
            dfs( number + 1 )

dfs ( 0 )

print ( cnt )