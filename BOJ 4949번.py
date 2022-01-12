
while True :
    commands = input()
    if commands == '.' :
        break
    stack = []
    answer = 'yes'
    for data in commands :
        if data in ['(' , '['] :
            stack.append(data)

        elif data == ')' :
            if not stack or stack[-1] != '(': # stack.pop() != '(': #stack[-1] != '(':
                answer = 'no'
                break
            stack.pop()

        elif data == ']' :
            if len(stack) == 0 or stack.pop() != '[':
                answer = 'no' 

        #print ( data , stack , answer)
    if len(stack) != 0 :
        answer = 'no'
        
    #print ( stack )
    print ( answer ) 