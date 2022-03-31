# 무방향이면서 , 싸이클이 없는 그래프
'''
7 6
5 4
5 1
4 2
4 3
1 7
6 7
'''

import sys
from collections import deque
input = sys.stdin.readline

n , m = map ( int , input().split() )
adj = [[] for _ in range( n+1 ) ]
for _ in range ( m ) :
    first , second = map ( int , input().split() )
    adj[first].append( second )
    adj[second].append( first )

parent_list = [0 for _ in range( n+1 ) ]
depth_list = [0 for _ in range( n+1 ) ]

def bfs_parent ( root ) :
    queue = deque()
    queue.append( root )

    while ( queue ) :
        temp = queue.popleft()
        # print  ( temp ) -- validation
        for target in adj[temp] :
            if parent_list[temp] == target :
                continue
            queue.append(target)
            parent_list[target] = temp
            depth_list[target] = depth_list[temp] + 1
            
    return parent_list , depth_list

print ( bfs_parent( 5 ) )
