from itertools import combinations_with_replacement
from collections import Counter
def solution(n, info):
    answer = []
    info = info[::-1]
    win_jumsu = 0
    value = [i for i in range(11)]
    
    for case in combinations_with_replacement(value,n):
        temp = [0]*11
        cnt = 0
        for key,value in Counter(case).items():
            temp[key]=value
        for index,(apeach,ryan) in enumerate(zip(info,temp)):
            if apeach==0 and ryan==0:
                continue
            elif apeach>=ryan:
                cnt-=index
            else:
                cnt+=index
        if win_jumsu < cnt :
            answer=temp
            win_jumsu=cnt
    if not answer:
        return [-1]
    return answer[::-1]