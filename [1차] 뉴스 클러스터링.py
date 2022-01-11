def solution(str1, str2):
    answer = 0
    str1_data = dict()
    str2_data = dict()
    
    same_data = 0

    for data1 ,data2 in zip(str1 , str1[1:] ) :
        if data1.isalpha() and data2.isalpha():
            temp = data1.upper() + data2.upper()
            if temp in str1_data.keys() :
                str1_data[temp] += 1
            else :
                str1_data[temp] = 1
    
    for data1 ,data2 in zip(str2 , str2[1:] ) :
        if data1.isalpha() and data2.isalpha():
            temp = data1.upper() + data2.upper()
            if temp in str2_data.keys() :
                str2_data[temp] += 1
            else :
                str2_data[temp] = 1
    
    for key , value in str1_data.items() :
        if key in str2_data.keys() :
            same_data += min ( value , str2_data[key] )
    
    sum_data = sum(str1_data.values() ) + sum(str2_data.values() ) - same_data
    #print (same_data , sum_data)
    if sum_data < 1 :
        return 65536
    answer = 65536 * same_data  // sum_data
    return answer

print ( solution ( 'E=M*C^2',	'e=m*c^2' ) )