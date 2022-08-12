# Programmers-N-Queen
def recursion(temp,number,n):
    cnt=0
    if number==n:
        return 1
    for j in range(n):
        check=True
        #세로
        if j in list(map(lambda x:x[1],temp)):
            check=False

        for x,y in temp:
            if abs(y-j)==number-x:
                check=False
                break
        if check:
            temp.append(((number,j)))
            cnt+=recursion(temp,number+1,n)            
    
    return cnt
def solution(n):
    answer = 0
    temp=[]
    
    for y in range(n):
        temp=[(0,y)]
        print( recursion(temp[:],1,n) ) 
    return answer

#test
print( solution(4) )