import sys
input = sys.stdin.readline

n = int(input())
answer = dict()
for i in range ( n ) :
    key , value = map ( str , input().split()  )
    if value == 'enter' :
        answer[key] = 1
    else :
        answer[key] -= 1
        
for data in sorted( list ( filter (lambda x:x[1] > 0 , answer.items() ) ) , reverse = True ):
    print ( data[0])
    