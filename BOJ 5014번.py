# BOJ 5014번

from collections import deque

maps , start ,destination ,  up_value , down_value = map ( int , input().split())

answer = 0
visited = [False] * (maps+1)
q = deque()
q.append( (start , 0 ) )
visited[start] = True

while q :
    current , move = q.popleft()
    if current == destination :
        print ( move )
        exit(0)
    if current + up_value <= maps and not visited[current+up_value] :
        q.append( ( current + up_value , move + 1) )
        visited[ current+up_value ] = True

    if current - down_value > 0 and not visited[current - down_value] :
        q.append( ( current - down_value , move+1 ))
        visited[ current - down_value ] = True

print ( 'use the stairs' )