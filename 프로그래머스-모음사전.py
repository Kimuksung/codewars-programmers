#프로그래머스-모음사전
def solution(word):
    from itertools import product

    alphas = ['A','E','I','O','U']
    word_data = []
    for i in range(1,6):
        for data in list( product(alphas, repeat=i) ) :
            word_data.append( ''.join(data) )

    word_data.sort()
    return word_data.index(word)+1
