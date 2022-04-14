# BOJ  17298번

import sys
input = sys.stdin.readline

n = int(input())
number_list = [0]
number_list.extend ( map ( int , input().split() ) )
stack = []
answer = [-1] * (n+1)

for i in range( 1 , n ) :
    stack.append( [i , number_list[i]] )
    while ( stack ) :
        if stack[-1][1] < number_list[i+1] :
            answer[stack[-1][0]] = number_list[i+1]
            stack.pop()
        else :
            break

print ( *answer[1:] )
