# BOJ 1197번 - 최소 스패닝 트리

import sys
input = sys.stdin.readline

V , E = map ( int , input().split() )
Edge_list = []
parent_list = [i for i in range(V+1)]
answer = 0
cnt = 0

def find ( node ) :
    if parent_list[node] != node :
        return find(parent_list[node])
    return node

def union ( a , b ) :
    a = find(a)
    b = find(b)
    if a == b :
        return False
    
    if a < b :
        parent_list[b] = a
    else :
        parent_list[a] = b
    return True

for _ in range ( E ) :
    start , end , cost = map ( int , input().split() )
    Edge_list.append([start,end,cost])

Edge_list = sorted ( Edge_list , key = lambda x : x[2])

for Edge in Edge_list :
    start , end , cost = Edge
    if union( start , end ) :
        answer += cost
        cnt += 1
    if cnt == V-1 :
        break

print ( answer )
    