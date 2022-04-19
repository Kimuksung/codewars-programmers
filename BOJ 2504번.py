#BOJ 2504번

char_datas = input()
stack = []

try :
    for index , char_data in enumerate ( char_datas ) :
        if char_data in ['(' , '[' ] :
            stack.append(char_data)

        elif char_data == ')' :
            if char_datas[index-1] == '(' : #step1
                stack.pop()
                stack.append(2)
            elif stack and str(stack[-1]).isnumeric() : 
                if stack[-2] == '(' : #step3
                    temp = stack[-1] * 2
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
            else :
                raise('1')
        elif char_data == ']' :
            if char_datas[index-1] == '[' : #step2
                stack.pop()
                stack.append(3)
            elif stack and str(stack[-1]).isnumeric() :
                if stack[-2] == '[' :
                    temp = stack[-1] * 3
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
            else :
                raise('1')

        if len(stack) >= 2 :
            if str(stack[-1] ).isnumeric() and str(stack[-2] ).isnumeric() :
                temp = stack[-1]+stack[-2]
                stack.pop()
                stack.pop()
                stack.append(temp)

    if len(stack) != 1 or not str(stack[0]).isnumeric():
        raise('1')
    print ( stack[0] )
except :
    print (0)