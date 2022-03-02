import sys
input = sys.stdin.readline

N , M  = map ( int , ( input().split(' ') ) ) 

data = list ( map(int , input().split(' ') ) )
sum_data  = [0]

for i in range ( N ) :
    sum_data.append(sum_data[-1] + data[i])

for _ in range ( M ) :
    start , end  = map ( int , ( input().split(' ') ) )
    print ( sum_data[end] - sum_data[start-1] )
    