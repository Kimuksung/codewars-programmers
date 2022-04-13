#BOJ 5397번

def answer ( datas ) :
    word = []
    stack = []
    for data in datas :
        if data == '<' and word :
            stack.append( word.pop() )
        if data == '>' and stack :
            word.append( stack.pop() )
        if data == '-' and word :
            word.pop()
        if data not in ( ['<' , '>' , '-']) :
            word.append(data)
    
    while stack :
        word.append( stack.pop() )
    
    return ''.join( word )

n = int( input() )
for _ in range( n ) :
    temp = input()
    print ( answer(temp) )

