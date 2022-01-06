def solution ( left , right ) :
    answer = 0
    temp = [1]*1001
    for i in range ( 32 ) :
        temp[i*i] = -1

    for data in range ( left, right + 1) :
        answer +=  data * temp[data] 
    return answer

print ( solution ( 1 , 4) )
