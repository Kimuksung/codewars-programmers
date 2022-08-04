# Programmers-교점에 별 만들기
import sys

# 교점
def intersect(a1,b1,c1,a2,b2,c2):
    if (a1*b2-a2*b1)==0 or (a2*b1-a1*b2)==0 or not ((b1*c2-b2*c1)/(a1*b2-a2*b1)).is_integer() or not ((a1*c2-a2*c1)/(a2*b1-a1*b2)).is_integer(): #or a1*b2-b1*c2==0:
        return False
    return (b1*c2-b2*c1) / (a1*b2-a2*b1) , (a1*c2-a2*c1)/(a2*b1-a1*b2)

def solution(line):
    answer = []
    intersect_list = set()
    #교점 경우의 수 추출
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            temp = intersect(*tuple(line[i]+line[j]))
            if temp :
                intersect_list.add(tuple(map(int,temp)))

    # 추출된 값들 중 영역 확인
    max_x ,max_y,min_x,min_y = -sys.maxsize,-sys.maxsize ,sys.maxsize,sys.maxsize
    for a,b in intersect_list :
        max_x,max_y,min_x,min_y=max(max_x,a),max(max_y,b),min(min_x,a),min(min_y,b)
        
    #print(intersect_list,min_x,max_x,min_y,max_y)
    
    for i in range(min_y,max_y+1):
        temp = ''
        for j in range(min_x,max_x+1) :
            if (j,i)in intersect_list :
                temp+='*'
            else:
                temp+='.'
        answer.append(temp)
    return answer[::-1]

answer = solution([[0,1,-100],[1,0,-100]])
#test
[print(answers) for answers in answer]
#solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
#solution([[1, -1, 0], [2, -1, 0]])
#solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]])