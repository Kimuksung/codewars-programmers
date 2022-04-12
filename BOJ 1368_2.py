# BOJ 1368 - 물대기
# 최소의 비용으로 각 노드별로 연결하기
# 크루스칼
import sys
input = sys.stdin.readline

def find( node ) :
    if parent[node] != node :
        return find(parent[node])
    return node

def union( a , b ) :
    a = find(a)
    b = find(b) 
    if a == b :
        return False
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
    return True

n = int(input()) 
edge_list = []
parent = [i for i in range(n+1)]
cnt , answer = 0 , 0

for i in range( 1 , n+1 ) :
    cost = int(input())
    edge_list.append( [0,i,cost] )
    edge_list.append( [i,0,cost] )

for i in range( n ) :
    for index , value in enumerate(  map(int, input().split())  ) :
        if value == 0 :
            continue
        edge_list.append( [i+1,index+1,value])

edge_list = sorted( edge_list , key = lambda x : x[2] )

for edge in edge_list :
    if cnt > n-1 :
        break
    start , end , cost = edge
    if union ( start , end ) :
        answer += cost
        cnt += 1

print ( answer )