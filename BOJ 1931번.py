import sys
input = sys.stdin.readline

n = int(input())

arrs = []
start = 0
cnt = 0

for i in range( n ) :
    arrs.append( list ( map(int , input().split( ' ' ) ) ) )

arrs = sorted( arrs , key = lambda x : ( x[1] , x[0] ) )
#print ( arrs )
for arr in arrs :
    first , second  = arr
    if first >= start :
        cnt +=1 
        start = second

print ( cnt )