import sys
input = sys.stdin.readline
N = int( input() )
A = list ( map ( int , input().split(' ') ) )

M = int( input() )
B = list ( map ( int , input().split(' ') ) )

A.sort()
def check_data ( arr , start , end , n) :
    temp = ( start+end ) // 2
    
    #종료 조건
    if start==end :
        return arr[start]

    if n <= arr[temp] :
        return check_data ( arr , start , temp , n )    
    else : 
        return check_data ( arr , temp+1 , end , n ) 

for data in B :
    if data == check_data ( A , 0 , N-1 , data ) :
        print ( '1' )
    else :
        print ( '0')
