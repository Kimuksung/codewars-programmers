#프로그래머스 - [3차] n진수 게임

def change_data(n,q):
    #datas = [str(i) for i in range(10)]+['A','B','C','D','E','F']
    datas=list('0123456789ABCDEF')
    digits = ''
    
    if n == 0 :
        return '0'
    while n>0:
        n , mod = n//q , n%q
        digits+=datas[mod]

    return digits[::-1]


def solution(n,t,m,p):
    answer = ''
    num = 0
    p -= 1
    while len(answer) < t*m :
        answer+=change_data(num,n)
        num+=1

    return answer[p::m][:t]

print( solution(16,16,2,2) ) 
