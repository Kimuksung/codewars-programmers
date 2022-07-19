#프로그래머스-줄서는 방법

import math

def solution(n, k):
    answer = []
    datas = [i for i in range(1,n+1)]
    k=k-1

    for _ in range(n) :
        fact = math.factorial(n-1)
        index = k//fact
        #answer.append(datas.pop(index))
        answer.append(datas[index])
        del datas[index]
        k=k%fact
        n-=1

    return answer

n,k = 3,5
print(solution(n,k))