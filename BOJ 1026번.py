import sys
input = sys.stdin.readline

n = int( input() )
A , B = [] , []
answer = 0


A.extend ( list ( map( int , input().split(' ')) ) )
B.extend ( list ( map( int , input().split(' ')) ) )

A.sort( reverse=True)
B.sort()

for index , value in enumerate ( A ) :
    answer += int(value) * B[index]
#print ( A )
#print ( B )
print ( answer )