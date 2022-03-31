import sys
input = sys.stdin.readline

n = int(input())
left_list = [0] * 26
right_list = [0] * 26
preorder_answer = []
inorder_answer = []
post_answer = []

for _ in range( n ) :
    start , left , right = map( str , input().split() )
    if left != '.' :
        left_list[ord(start)-65] = ord(left)-65
    if right != '.' :
        right_list[ord(start)-65] = ord(right)-65

#print ( left_list , right_list )

def preorder( start ) :
    preorder_answer.append(chr(start+65))
    if left_list[start] != 0 :
        preorder ( left_list[start] )
    if right_list[start] != 0 :
        preorder ( right_list[start] )

def inorder( start ) :
    if left_list[start] != 0 :
        inorder ( left_list[start] )
    inorder_answer.append(chr(start+65))
    if right_list[start] != 0 :
        inorder ( right_list[start] )

def postorder( start ) :
    if left_list[start] != 0 :
        postorder ( left_list[start] )
    if right_list[start] != 0 :
        postorder ( right_list[start] )
    post_answer.append(chr(start+65))

preorder( 0 )
inorder( 0 )
postorder( 0 )
print ( ''.join( preorder_answer ) )
print ( ''.join( inorder_answer ) )
print ( ''.join( post_answer ) )