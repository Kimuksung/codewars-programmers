def solution(str1, str2):
    answer = 0
    
    # 다중집합
    str1_data , str2_data = [] , []
    
    for a, b in  zip(str1 ,str1[1:]) :
        if a.encode().isalpha() and b.encode().isalpha() :
            str1_data.append( a.lower()+b.lower() )
    for a, b in  zip(str2 ,str2[1:]) :
        if a.encode().isalpha() and b.encode().isalpha() :
            str2_data.append( a.lower()+b.lower() )
    
    sum_set = list(set(str1_data) | set(str2_data))
    intersect_set = list(set(str1_data) & set(str2_data))

    first_cnt_sum  , first_cnt_intersect = 0,0
    second_cnt_sum  , second_cnt_intersect = 0,0
    for first in str1_data :
        if first in sum_set :
            first_cnt_sum += 1
        if first in intersect_set :
            first_cnt_intersect += 1
    
    for second in str2_data :
        if second in sum_set :
            second_cnt_sum += 1
        if second in intersect_set :
            second_cnt_intersect += 1
    print ( min(first_cnt_intersect , second_cnt_intersect))
    print ( max(second_cnt_sum , second_cnt_intersect))
    print ( sum_set , intersect_set )
    return answer

solution ( 'aa1+aa2' , 'AAAA12')