import sys
def result(start,end,devide):
    answer=0
    #start,end in Q1
    if start<=devide and end<=devide:
        answer+=end+1
        answer+=devide+1
        answer+=start
    #start in Q1 and end in Q2
    elif start<=devide and devide<=end:
        answer+=start
        answer+=end-devide
    
    #start in Q2 and end in Q1
    elif devide<=start and end<=devide:
        answer+=end-devide-1
        answer+=start+1
    
    #start,end in Q2
    else:
        answer+=end-devide
        answer+=devide+1
        answer+=start-devide-1
    
    return answer

def solution(queue1, queue2):
    answer = []
    n = len(queue1)
    all_queue = queue1+queue2
    if sum(all_queue)%2==1:
        return -1
    
    target = sum(all_queue)//2
    
    for i in range(2*n):
        temp=0
        
        for right in range(i,2*n):
            temp+=all_queue[right]
            if temp==target:
                answer.append((i,right,result(i,right,n-1)))
                break
                
        for right in range(i):
            temp+=all_queue[right]
            if temp==target:
                answer.append((i,right,result(i,right,n-1)))
                break
                
    if answer==sys.maxsize:
        answer=-1
        
    return answer

print( solution( [3, 2, 7, 2] , [4, 6, 5, 1] ) )