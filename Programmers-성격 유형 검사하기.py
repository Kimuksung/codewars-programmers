from collections import defaultdict

def solution(surveys, choices):
    answer = defaultdict( lambda : 0 )
    weight = [1,2,3]
    targets=["RT","CF","JM","AN"]
    for survey,choice in zip(surveys,choices) :
        #print(survey,choice)
        if choice == 4 :
            continue
        
        elif choice > 4 :
            answer[survey[1]]+=weight[abs(choice-5)]
        else :
            answer[survey[0]]+=weight[abs(choice-3)]
        
    return ''.join([target[1] if answer[target[0]]<answer[target[1]] else target[0] for target in targets ])

survey=["AN", "CF", "MJ", "RT", "NA"] 
choices=[5, 3, 2, 7, 5]

print( solution(survey,choices) )
