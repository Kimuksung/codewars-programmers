# Programmers-행렬의 곱셈

def solution(A, B):
    answer = []
    print( [[(A_row,B_col) for B_col in zip(*B)] for A_row in A] )
    for a_row in A:
        for a_data in a_row :
            for b_col in zip(*B):
                print( "a_row : {} ".format(a_row))
                print( "b_col : {} ".format(b_col))
                print(sum([ a*b for a,b in zip(a_data,b_col) ]))

            #for a,b in zip(a_row,b_col) :
                #print(a_row,b_col)
                #print(a,b)

    return answer

solution([[[1, 4], [3, 2], [4, 1]]], [[6,7], [8,9]])