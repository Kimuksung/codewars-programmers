def change2(data , number ):
    data = bin(data).replace ( '0b' , '')
    n = len(data)
    if n < number :
        data = '0' * ( number - n) + data
    return data

def solution( n , arr1 , arr2 ) : 
    answer = []
    for data1 , data2 in zip(arr1, arr2) : 
        #print(data1,data2)      
        data1 , data2 = change2(data1 , n) , change2(data2 , n )
        #print(data1,data2)
        temp = ''
        for i in range(n):
            if data1[i] == '0' and data2[i] == '0' :
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer

print ( solution( 	6 , [46, 33, 33 ,22, 31, 50] , [27 ,56, 19, 14, 14, 10] ) )