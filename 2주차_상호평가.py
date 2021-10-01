def solution(scores):
    answer = ''
    n = len(scores)
    data = [0 for i in range(n)]

    for i in range (n) :
        temp = []
        cnt = 0
        for j in range (n) :
            if i!=j :
                temp.append( scores[j][i] )

        if scores[i][i] <= max(temp) and scores[i][i] >= min(temp) :
            temp.append( scores[i][i] )
            cnt += 1
        data[i] = sum(temp) / (n + cnt -1)
        
    for i in data :
        if i >= 90 :
            answer += 'A'
        elif i >= 80 :
            answer += 'B'
        elif i >= 70 :
            answer += 'C'
        elif i >= 50 :
            answer += 'D'
        else:
            answer += 'F'
    return answer
