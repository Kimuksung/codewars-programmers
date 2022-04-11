# 크루스칼 알고리즘
# 최소 신장 트리를 알기 위함

'''
5 7
1 2 4
1 3 3
1 4 3
2 5 8
3 5 5
3 4 4
4 5 6
'''

node , edge = map ( int , input().split() )
edge_list = []
parent_node = [i for i in range( node+1 ) ]

# union_find algrorithm
# https://0x15.tistory.com/34
def find ( node ) :
    if parent_node[node] != node :
        return find(parent_node[node])
    return node

def union ( A , B ) :
    A = find(A)
    B = find(B)

    if A == B :
        return False
    
    if A < B :
        parent_node[B] = A
    else :
        parent_node[A] = B

    return True

# 크루스칼
for _ in range( edge ) :
    start , end , cost = map( int , input().split() )
    edge_list.append( [start , end , cost] )

edge_list = sorted ( edge_list , key = lambda x : x[2] )

for edges in edge_list :
    start , end , cost = edges
    if union( start ,end ) :
        print ( start , end )


