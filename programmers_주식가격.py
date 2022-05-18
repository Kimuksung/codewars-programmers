def solution(prices):
    answer = []
    stack = []
    n = len(prices)
    answer = [0] * n
    
    for index , price in enumerate(prices) :
        if not stack or (stack and stack[-1][0] < price) :
            stack.append( (price , index))
            continue
        
        while ( stack ) :
            if stack[-1][0] <= price :
                break
            stack_price , stack_index = stack.pop()
            answer[stack_index] = index-stack_index
        stack.append( (price , index))
            
    while ( stack ) :
        stack_price , stack_index = stack.pop()
        answer[stack_index] = n-1-stack_index
            
    return answer