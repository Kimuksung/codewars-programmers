def check_data ( datas ) :
    answer = True
    stack = []

    for data in datas :
        if data.isalpha() :
            continue
        elif data in ['[' , '(' , '{'] :
            stack.append(data)
            continue  
        elif data == ']' and stack :
            temp = stack.pop()
            if temp != '[' :
                answer = False
                break
        elif data == ')' and stack :
            temp = stack.pop()
            if temp != '(' :
                answer = False
                break
        elif data == '}' and stack:
            temp = stack.pop()
            if temp != '{' :
                answer = False
                break
        else :
            answer = False
            break

    if stack != [] :
        answer = False
    return answer

def solution ( s ) :
    answer = 0

    if len(s) == 1 :
        return 0
    for i in range( len(s) ) :
        #print ( s )
        if check_data(s) :
            answer += 1
        s = s[1:] + s[0]

    return answer
    
    
print (  solution( '[](){}') )
#print (  solution( '{{{{{{{') )
