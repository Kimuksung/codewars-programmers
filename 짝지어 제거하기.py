def solution(s):
    stack = []
    for data in s :
        if len(stack) != 0 :
            temp = stack.pop()
            if temp != data :
                stack.append(temp)
                stack.append(data)
        else:
            stack.append(data)
    if stack == [] :
        return 1
    return 0
