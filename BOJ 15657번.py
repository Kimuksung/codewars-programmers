#BOJ 15657번

answer = []
n , m = map (int , input().split() )

datas = list ( map ( int, input().split() ) )
datas.sort()

def recursion ( number ) :
    if number == m :
        print ( *answer )
        return
    
    for data in datas :
        if not answer or ( answer and answer[-1] <= data ) :
            answer.append(data)
            recursion(number+1)
            answer.pop()

recursion(0)