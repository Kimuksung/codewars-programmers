#BOJ 13549번

from collections import deque

start , end = map( int , input().split() )
q = deque()
q.append( ( start , 0 ) )
visited = [False] * 100001

while q :
    current , move  = q.popleft()
    if current == end :
        print ( move )
        break

    if current > end and not visited[current-1] :
        q.append( ( current-1 , move+1) )
        visited[current-1] = True
        continue

    if 2*current <= 100000 and not visited[2*current]:
        q.append( ( 2*current , move ) )
        visited[2*current] = True
    if 0 <= current-1 <= 100000 and not visited[current-1]:
        q.append( ( current-1 , move+1) )
        visited[current-1] = True
    if 0 <= current+1 <= 100000 and not visited[current+1]:
        q.append( ( current+1 , move+1) )
        visited[current+1] = True
