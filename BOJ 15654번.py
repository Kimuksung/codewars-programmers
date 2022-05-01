#BOJ 15654번

n , m = map( int , input().split() )

datas = list ( map(int , input().split() ) ) 
datas.sort()
answer = []

def recursion ( number ) :
    if number == m :
        print ( *answer )
        return
    
    for data in datas :
        if data not in answer  :
            answer.append(data)
            recursion( number + 1 )
            answer.pop()

recursion(0)