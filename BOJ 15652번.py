#BOJ 15652번

n , m = map( int , input().split() )

datas = [ i for i in range(1 , n+1) ]
answer = []

def recursion ( number ) :
    if number == m :
        print( *answer )
        return
        
    for data in datas :
        if not answer or ( answer and answer[-1] <= data ) :
            answer.append(data)
            recursion( number+1 )
            answer.pop()

recursion( 0 )