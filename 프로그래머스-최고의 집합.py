def solution(n, s):
    balance = s//n
    
    if balance == 0 :
        return [-1]
    
    answer = [balance]*(n)
    move = s-sum(answer)
    answer = [balance]*(len(answer)-move) + [balance+1]*move
    #for i in range( len(answer)-1,len(answer)-move-1,-1):
        #answer[i] += 1
    
    return answer