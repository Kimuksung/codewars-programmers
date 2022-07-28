# 숫자 블록
import math
def yaksu(num):
    if num == 1:
        return 0
    for i in range(2,int(math.sqrt(num))+1):
        if num//i<10000000 and num%i==0 :
            return i
    return num

def solution(begin, end):
    answer =[]
    for i in range(begin,end+1):
        block=yaksu(i)
        if block==0:
            answer.append(0)
        else:
            answer.append(i//block)
    return answer
