def solution(datas):
    answer = True
    stack=[]
    
    for data in datas:
        if data == ')':
            if stack and stack[-1]=='(':
                stack.pop()
            else :
                answer = False
                break
        else :
            stack.append('(')
            
    if stack :
        answer=False

    return answer

print(solution(")()("))