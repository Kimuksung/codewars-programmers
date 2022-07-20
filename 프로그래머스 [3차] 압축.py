#프로그래머스 [3차] 압축

def solution(msg):
    answer = []       
    index = { chr(e+64) : e for e in range(1,27)}

    current = 27
    temp = 0
    left = 0
    n = len(msg) 
    
    while left <= n :
        check = False
        for right in range(left+1,n+1):
            target = msg[left:right]
            if target in index :
                check = True
                temp = index[target]
            else :
                check=False
                answer.append(temp)
                index[target]=current
                current+=1
                left = right-1
                break
        
        if check :
            answer.append(index[msg[left:]])
            break

    return answer

msg = "TOBEORNOTTOBEORTOBEORNOT"
solution(msg)