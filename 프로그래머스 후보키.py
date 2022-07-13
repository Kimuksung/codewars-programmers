#프로그래머스 후보키
from itertools import combinations
def solution(relation):
    answer = 0

    rows , columns = len(relation) , len(relation[0])
    # 경우의 수
    combination = []
    for i in range(1,columns+1) :
        combination.extend(combinations(range(columns),i))

    # 유일성
    unique = []
    for combi in combination :
        temp = [tuple([items[i] for i in combi ]) for items in relation]
        if len(set(temp)) == rows :
            unique.append(combi)

    answer = set(unique)
    for i in range(len(unique)) :
        for j in range(i+1,len(unique)) :
            if set(unique[i]) == set(unique[i])&set(unique[j]):
                answer.discard(unique[j])
    return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)