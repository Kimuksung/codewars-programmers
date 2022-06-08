def solution(brown, yellow):
    answer = []
    plus = (brown+4)//2
    multiple = brown+yellow

    for i in range(1,plus) :
        if i*(plus-i) == multiple :
            answer=[plus-i,i]
            break
    return answer