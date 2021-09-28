def solution(lottos, win_nums):
    lottos = list ( filter(lambda x : x!= 0 , lottos) )
    rank = [6 ,6 ,5,4,3,2,1]
    zero_cnt = 6 - len(lottos)
    cnt = 0
    for data in win_nums :
        if data in lottos :
            cnt += 1 
    answer = [ rank[zero_cnt + cnt] , rank[cnt] ]
    return answer

print ( solution([0, 0, 0, 0, 0, 0] , [38, 19, 20, 40, 15, 25] ) ) 