import bisect

def solution(A, B):
    answer = 0
    B.sort()
    for a in A :
        i = bisect.bisect_right(B,a)
        if i>len(B)-1:
            del B[0]
        else :
            if B[i]>a:
                answer+=1
            del B[i]
            
    return answer