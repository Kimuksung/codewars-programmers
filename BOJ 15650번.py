#BOJ 15650번

n , m = map( int, input().split() )

data = [i for i in range(1 , n+1 )] 
visited = [False] * n 
answer = []

def backtracking ( number ) :
    if number == m : #종료 조건
        print ( *answer )
        return

    for i in range( n ) :
        if not visited[i] and ( not answer or ( answer and answer[-1] < data[i] ) ) :
            answer.append( data[i] ) 
            visited[i] = True
            backtracking ( number + 1 )
            answer.pop()
            visited[i] = False
        
backtracking( 0 )
