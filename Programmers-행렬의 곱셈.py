# Programmers-행렬의 곱셈

def solution(A, B):
    answer = []
    for a_row in A:
        temp = []
        for b_col in zip(*B):
            #print( "a_row : {} ".format(a_row))
            #print( "b_col : {} ".format(b_col))
            temp.append(sum([ a*b for a,b in zip(a_row,b_col) ]))
        answer.append(temp)

    return answer

solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])