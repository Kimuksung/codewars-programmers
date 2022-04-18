#BOJ 2493번
import sys
input = sys.stdin.readline

n = int( input() )
data = map(int , input().split() )
stack1 = []
stack2 = []
answer = [0] * (n+1)
for index  , value in enumerate ( data ) :
    stack1.append( [index+1,value] )

while stack1 :
    stack2.append( stack1.pop() )
    while ( stack1 and stack2 ) :
        if stack2[-1][1] <= stack1[-1][1] :
            index , value = stack2.pop()
            answer[index] = stack1[-1][0]
        else:
            break

print ( *answer[1:] )