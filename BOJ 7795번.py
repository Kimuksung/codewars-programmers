import sys
input = sys.stdin.readline


N = int ( input() )

for T in range ( N ) :
    cnt = 0
    A , B = map ( int , input().split(' ') )
    caseA = sorted ( list ( map ( int , input().split(' ') ) ) , reverse = 1 )
    caseB = sorted ( list ( map ( int , input().split(' ') ) ) , reverse = 1)

    #print ( caseA )
    #print ( caseB )
    
    for i in caseA :
        for index , j in enumerate ( caseB ) :
            if i <= j :
                continue
            else :
                cnt += ( B - index )
                break
    '''
    for i in caseA :
        cnt += len ( list ( filter ( lambda x : x < i , caseB ) ) )
    '''
    print ( cnt )
