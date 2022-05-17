# Programmers
# 2021 KAKAO BLIND RECRUITMENT
# 순위 검색

import bisect

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    
    infos = dict()
    temp = []
    for items in info :
        item = items.split()
        temp.append( ( tuple(item[:-1]) , item[-1] ) )

    temp.sort( key = lambda x : x[1] )

    for item , value in temp :
        if item not in infos :
            infos[item] = []
        infos[item].append(value)

    for item in query :
        item = item.split()
        item = list ( filter ( lambda x : x != 'and' , item ) )
        query_score = item[-1]
        item = item[:-1]

        query_key = list( infos.keys() )
    
        for current_q in item :
            if current_q == '-' :
                continue
            query_key = list(filter ( lambda x:current_q in x , query_key ) )
        
        query_infos = [infos[query_keys] for query_keys in query_key]
        
        temp_count = 0
        for query_info in query_infos :
            index = bisect.bisect_left( query_info , query_score )
            temp_count += len(query_info) - index
        print ( query_score , query_infos )
        answer.append(temp_count)
    return answer

print ( solution(info, query) )