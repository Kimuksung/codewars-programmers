#Programmers-성격 유형 검사하기2

def solution(surveys, choices):
    targets = {"RT":0,"CF":0,"JM":0,"AN":0}

    for survey,choice in zip(surveys,choices) :
        if not survey in targets :
            targets[survey[::-1]] -= choice-4
        else :
            targets[survey] += choice-4
    print(targets)
    return ''.join([key[0] if value<=0 else key[1] for key,value in targets.items() ])

survey=["AN", "CF", "MJ", "RT", "NA"] 
choices=[5, 3, 2, 7, 5]

print( solution(survey,choices) )
