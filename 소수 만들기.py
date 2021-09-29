from itertools import combinations
import math
def check(num) :
    if num == 0 :
        return False
    elif num == 1:
        return True
    for i in range ( 2, int ( math.sqrt (num) ) + 1) :
        if num % i == 0 :
            return False
    return True

def solution(nums):
    answer = -1
    
    datas = list(combinations(nums, 3))
    answer = len ( list ( filter ( lambda x : check(x) , [sum(data) for data in datas ] ) ) ) 

    return answer

print ( solution( [1,2,7,6,4] )  )