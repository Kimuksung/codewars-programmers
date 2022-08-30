# Programmers-N으로 표현
def solution(N, number):
    dp = [ set() for _ in range(9) ]

    for i in range(1,9):
        temp=set()
        temp.add( int(str(N)*i) )
        
        for j in range(i):
            for x in dp[j]:
                for y in dp[i-j]:
                    temp.add(x*y)
                    temp.add(x+y)
                    temp.add(x-y)
                    if y!=0:
                        temp.add(x//y)
        if number in temp:
            return i
        dp[i]=temp
    
    return -1

N=5
number=31168
print( solution(N,number) )