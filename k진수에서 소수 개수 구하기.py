import math
def solution(n, k):
    def change_basic(n,k):
        answer=''
        
        while n!=0:
            answer+=str(n%k)
            n = n//k
        return answer[::-1]
    
    def prime(n):
        if n=='' or n=='1':
            return False
        n=int(n)
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0:
                return False
        return True

    return sum( [prime(data) for data in change_basic(n,k).split('0')] )