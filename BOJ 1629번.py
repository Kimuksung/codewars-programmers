#import sys
#sys.setrecursionlimit(10**6)

N , M , P = map ( int , input().split(' ') )

def solution ( N , M , P ) :
    #print ( N , M , P )
    if M == 1 :
        return N % P
    
    data = solution ( N , int ( M / 2 ) , P )
    data = data * data % P 
    if ( M%2 == 0 ) : 
        return data
    return data * N % P

print ( solution(N,M,P) ) 