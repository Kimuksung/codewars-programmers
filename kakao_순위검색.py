import bisect
from itertools import combinations

def solution(infos, querys):
    answer = []    
    info_data  = dict()
    
    for info in infos :
        info = info.split()
        info , info_exam = info[:4] , int(info[-1])
        
        for j in range(5) :
            for case_info in combinations(info , j) :
                case_info = ''.join(case_info)
                if case_info not in info_data :
                    info_data[case_info] = []
                info_data[case_info].append(info_exam)
        
    for value in info_data.values() :
        value.sort()

    for query in querys :
        cnt = 0

        query = query.split()
        query = list( filter( lambda x:x not in ['and','-'] , query) )
        query_info , query_exam = ''.join(query[:-1]) , int(query[-1])

        if query_info in info_data :
            temp = info_data[query_info]
            index = bisect.bisect_left( temp , query_exam )
            cnt += len(temp) - index
        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print ( solution(info, query) )