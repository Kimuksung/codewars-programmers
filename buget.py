def solution(d, budget):
    answer = 0
    money = 0
    d = sorted ( d )
    for data in d:
        if money + data > budget:
            break
        money += data
        answer += 1
    return answer