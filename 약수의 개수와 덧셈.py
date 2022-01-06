def solution ( left , right ) :
    answer = 0
    temp = [1]*1001
    for i in range ( 31 ) :
        temp[i*i] = -1

    for data in range ( left, right + 1) :
        answer +=  data * temp[data] 
    #print (temp)
    return answer

print ( solution ( 1 , 4) )
