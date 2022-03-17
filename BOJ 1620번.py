import sys
input = sys.stdin.readline

n , m = map ( int , input().split() )

pocketmon = dict()

for i in range( 1, n+1 ) :
    data = input().rstrip()
    pocketmon[data] = i
    pocketmon[i] = data

for _ in range ( m ) :
    data = input().rstrip()
    if  data.isdigit() :
        data = int ( data )
        print ( pocketmon[data] )
    else :
        print(pocketmon[data])

