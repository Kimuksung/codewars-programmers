# 무방향이면서 , 싸이클이 없는 그래프
'''
7 6 5
5 4
5 1
4 2
4 3
1 7
6 7
'''

import sys
input = sys.stdin.readline

n , m , start = map ( int , input().split() )
adj = [[] for _ in range( n+1 ) ]
for _ in range ( m ) :
    first , second = map ( int , input().split() )
    adj[first].append( second )
    adj[second].append( first )

parent_list = [0 for _ in range( n+1 ) ]
depth_list = [0 for _ in range( n+1 ) ]

def dfs_parent ( root ) :
    stack = list()
    stack.append( root )
    parent_list = [0 for _ in range( n+1 ) ]
    depth_list = [0 for _ in range( n+1 ) ]

    while ( stack ) :
        temp = stack.pop()
        print ( temp )
        for target in adj[temp] :
            if parent_list[temp] == target :
                continue
            parent_list[target] = temp
            depth_list[target] = depth_list[temp] + 1
            stack.append(target)
    return parent_list , depth_list

def dfs_parent_recursion ( root ) :
    print( root )
    for target in adj[root] :
        if parent_list[root] == target :
            continue
        parent_list[target] = root
        depth_list[target] = depth_list[root] + 1
        dfs_parent_recursion(target)
    return parent_list , depth_list

def dfs_recursion_circuit ( cur , parent ) :
    print ( cur )
    for target in adj[cur] :
        if target == parent :
            continue
        dfs_recursion_circuit ( target , cur)


#print ( dfs_parent(start) )
#print ( dfs_parent_recursion ( start ) )
dfs_recursion_circuit ( start , 0 )