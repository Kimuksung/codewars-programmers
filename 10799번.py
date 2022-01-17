datas = str(input() )
stack = []
answer = 0
N = 0
for index , data in enumerate ( datas ) :
    if data =='(' :
        stack.append( '(')
    elif stack : 
        if datas[index-1] == '(' :
            stack.pop()
            answer += len(stack)
        else :
            answer += 1
            stack.pop()

print (answer)