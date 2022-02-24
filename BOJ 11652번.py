import sys
input = sys.stdin.readline

N = int ( input())

answer = dict()

for i in range ( N ) :
    temp = int ( input() )
    if temp in answer :
        answer[temp] += 1
    else :
        answer[temp] = 1


data = sorted ( answer.items() , key= lambda x : ( - x[1] , x[0] ) )
print ( data[0][0] )