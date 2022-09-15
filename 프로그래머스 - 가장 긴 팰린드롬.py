# palindrome
def palin(data):
    if data == data[::-1]:
        return True
    return False

def solution(s):
    answer = 0
    n = len(s)
    # 1. 부분 문자열
    for i in range(n):
        for j in range(i+1,n+1):
            if palin(s[i:j]) :            
                answer = max(answer,j-i)

    return answer