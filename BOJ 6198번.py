# BOJ 6198번

import sys
input = sys.stdin.readline

n = int ( input() )
building_list = [0]

for _ in range(n) :
    building_list.append( int(input()) ) 
answer = [ n-i for i in range(n) ] 
stack = []

for i in range( 1 , n ) :
    stack.append( [building_list[i] , i] )
    while ( stack ) :
        if stack[-1][0] <= building_list[i+1] :
            answer[stack[-1][1]] = i - stack[-1][1]
            stack.pop()
        else :
            break

print ( sum( answer[1:] ) )

