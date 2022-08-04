# Programmers-k진수에서 소수 개수 구하기
import math
def check(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):        
        if n%i==0:
            return False
    return True

def sosu(n,k):
    answer=''
    
    while n>0:
        answer+= str(n%k)
        n = n//k
    return answer[::-1]
    
def solution(n, k):
    answer = 0

    for data in sosu(n,k).split('0'):
        if data and check(int(data)) :
            answer+=1

    return answer