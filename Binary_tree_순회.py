import sys
input = sys.stdin.readline
from collections import deque
'''
8 4 1
1 2 3
2 4 5
5 0 8
3 6 7
'''
n , m , start = map ( int , input().split() )
left_data = [0] * (n+1)
right_data = [0] * (n+1)

for _ in range ( m ) :
    parent , left , right = map ( int , input().split() )
    left_data[parent] = left
    right_data[parent] = right

# Level 순회
# BFS와 동일하게 설정 ( 단, Left / right 만 주의 )
def Level_Traversal ( start ) :
    queue = deque()
    queue.append(start)
    while queue :
        temp = queue.popleft()
        print ( temp )
        if left_data[temp] != 0 :
            queue.append( left_data[temp])
        if right_data[temp] != 0 :
            queue.append( right_data[temp])

# 전위 순회
# 중 -> 좌 -> 우
def Preorder_Traversal ( start ) :
    print  ( start )
    if left_data[start] != 0 :
        Preorder_Traversal(left_data[start])
    if right_data[start] != 0 :
        Preorder_Traversal(right_data[start])

# 중위 순회
# 이진탐색 트리였다면, 크기 순으로 보여졌을 것
# 좌 -> 중 -> 우
def Inorder_Traversal ( start ) :
    if left_data[start] != 0 :
        Inorder_Traversal(left_data[start])
    print  ( start )
    if right_data[start] != 0 :
        Inorder_Traversal(right_data[start])

# 후위 순회
# 좌 -> 우 -> 중
def Postorder_Traversal ( start ) :
    if left_data[start] != 0 :
        Postorder_Traversal(left_data[start])
    if right_data[start] != 0 :
        Postorder_Traversal(right_data[start])
    print  ( start )

#Level_Traversal ( start )
#Preorder_Traversal ( start )
#Inorder_Traversal ( start )
Postorder_Traversal ( start ) 